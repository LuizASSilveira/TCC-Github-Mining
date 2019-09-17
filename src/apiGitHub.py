import math
import time

import requests
from controlDir import ControlDir


class ApiGitHub:
    def __init__(self, user, token):
        headers = {"Authorization": token}
        self.__user = user
        self.__headers = headers
        self.__queryCommitFull = """
            {
                user(login: "userName"){
                    name,
                    avatarUrl,
                    createdAt,    
                    pullRequests(pullRequestsConfig){
                        pageInfo{
                            endCursor,
                            hasNextPage,
                        }
                        totalCount,
                        nodes{
                            commits(last:100){
                                totalCount,
                                pageInfo{
                                    endCursor,
                                    hasNextPage 
                                }, 
                                nodes{
                                     resourcePath,
                                     commit{
                                        abbreviatedOid
                                     },
                                    pullRequest{
                                        number
                                    }
                                }
                            }
                        }
                    }
                },
                viewer {
                    login
                },
                rateLimit {
                    limit
                    cost
                    remaining
                    resetAt
                }
            }
            """
        self.__queryCommitBig = """
            {
                user(login: "userName"){
                    name,
                    avatarUrl,
                    createdAt,    
                    pullRequests(first:1, states: stateQueryCommit){
                        nodes{
                            repository{
                            pullRequest(number:NumberPull){
                                commits(commitInfo){
                                totalCount,
                                pageInfo{
                                    endCursor,
                                    hasNextPage 
                                }, 
                                nodes{
                                resourcePath
                                commit{
                                    abbreviatedOid
                                }
                                }
                                }
                            }
                        } 
                        }
                    }
            },
            viewer {
                login
            }
            rateLimit {
                limit
                cost
                remaining
                resetAt
            }
        }
        
            """

    @staticmethod
    def performRequest(self, url, numTentativas=10):
        tentativas = 0
        while (True):
            try:
                request = requests.get(url, headers=self.headers)
                if (request.status_code == 200):
                    return request
                elif (tentativas > numTentativas):
                    return False
                else:
                    tentativas += 1
                    time.sleep(60)
            except requests.exceptions.RequestException as e:
                print(e)
                time.sleep(10)

    def requestApiGitHubV4(self, query, numTentativas=10):
        request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=self.headers)

        if request.status_code == 200:
            return request.json()
        else:
            raise Exception("Query failed to run by returning code of {}. {}".format(request.status_code, query))

    def getAlterateCommitPull(self, nodeCommit, perPage, state, dc, pwdCurrent):
        allPatchs = []
        totalCommit = nodeCommit['commits']['totalCount']
        numberPull = nodeCommit['commits']['nodes'][0]['resourcePath'].split('/')[4]

        if totalCommit < perPage:  # no caso de mais 100 commits em um pullrequest
            allPatchs = nodeCommit['commits']['nodes']
        else:
            commitInfo = 'first:{}'.format(perPage)
            for i in range(math.ceil(totalCommit / perPage)):  # arredonda flutuante pra cima (interio)
                try:
                    url = self.queryCommitBig.replace('userName', self.__user.loginUser).replace('NumberPull',
                                                                                                 numberPull).replace(
                        'commitInfo', commitInfo).replace('stateQueryCommit', state)
                    result = self.requestApiGitHubV4(url)
                    endCursor = result['data']['user']['pullRequests']['nodes'][0]['repository']['pullRequest']['commits']['pageInfo']['endCursor']
                    commitInfo = 'first:{}, after:"{}"'.format(perPage, endCursor)
                    allPatchs += result['data']['user']['pullRequests']['nodes'][0]['repository']['pullRequest']['commits']['nodes']
                except:
                    # api v4 nao econtra alguns pulls closed
                    pass

        for i, node in enumerate(allPatchs):
            print('\tCommit', str(i + 1) + '/' + str(totalCommit))
            url = 'https://github.com' + node['resourcePath'] + '.patch'
            pwd = pwdCurrent + '\\' + url.split('/')[6]
            if i == 0:
                dc.newDirectory(pwd)

            req = self.performRequest(self, url)  # obtem raw alteração
            if req:
                file = open(pwd + '\\' + node['commit']['abbreviatedOid'] + '.txt', 'w', encoding="utf-8")
                file.write(req.text)
                file.close()

    def getPullRequestUsers(self, perPage=100):
        states = ['MERGED', 'OPEN', 'CLOSED']
        user = self.user
        dc = ControlDir(user.loginUser)  # cria arquivo user

        for state in states:
            pullRequestsConfig = 'first:{}, states:{}'.format(perPage, state)
            cont = 0
            pwdCurrent = dc.userDirectory + '\\' + state
            dc.newDirectory(pwdCurrent)  # adiciona Status ao diretorio
            print(user.loginUser)
            print(state)

            while True:
                url = self.queryCommitFull.replace('userName', user.loginUser).replace('pullRequestsConfig', pullRequestsConfig)
                result = self.requestApiGitHubV4(url)  # Execute the query
                pullRequests = result["data"]["user"]['pullRequests']
                user.numberPullRequest = pullRequests['totalCount']
                for nodeCommit in pullRequests['nodes']:
                    cont += 1
                    print('pull nº ', str(cont) + '/' + str(user.numberPullRequest))
                    self.getAlterateCommitPull(nodeCommit, perPage, state, dc, pwdCurrent)

                endCursorPull = pullRequests['pageInfo']['endCursor']
                asNextPagePull = pullRequests['pageInfo']['hasNextPage']

                if asNextPagePull:
                    pullRequestsConfig = 'first:{}, after:"{}", states:{}'.format(perPage, endCursorPull, state)
                else:
                    break

    @property
    def user(self):
        return self.__user

    @property
    def queryCommitFull(self):
        return self.__queryCommitFull

    @property
    def headers(self):
        return self.__headers

    @property
    def queryCommitBig(self):
        return self.__queryCommitBig
