from src.fileControl import FileControl
from src.repository import Repository
from src.apiGitHub import ApiGitHub
from src.userGit import UserGit

import json
import sys

try:
    token = sys.argv[1]
except:
    print('Insira o tokem GitHub')
    exit(0)

diretorioPadrao = "C:\\Users\\luiz_\\OneDrive\\Área de Trabalho\\"


def getInfoUser():
    user = UserGit('luizSilveira')
    apiUser = ApiGitHub(user, 'token ' + token)
    mostPopularLanguages2 = ['JavaScript', 'Python', 'Java', 'PHP']
    apiUser.getUserFromRep(mostPopularLanguages2)


def proInfoUser(user):
    apiUser = ApiGitHub(user, 'token ' + token)
    info = apiUser.getUserInf()
    user.name = info["data"]["user"]["name"]
    user.id = info["data"]["user"]["id"]
    user.email = info["data"]["user"]["email"]
    user.avatarUrl = info["data"]["user"]["avatarUrl"]
    user.bio = info["data"]["user"]["bio"]
    user.watching = info["data"]["user"]["watching"]["totalCount"]
    user.followers = info["data"]["user"]["followers"]["totalCount"]
    user.following = info["data"]["user"]["following"]["totalCount"]
    user.location = info["data"]["user"]["location"]
    user.createdAt = info["data"]["user"]["createdAt"]
    user.company = info["data"]["user"]["company"]
    user.issues = info["data"]["user"]["issues"]["totalCount"]
    user.organizationTotal = info["data"]["user"]["organizations"]["totalCount"]
    user.projects = info["data"]["user"]["projects"]["totalCount"]
    user.gists = info["data"]["user"]["gists"]["totalCount"]
    user.pullRequests = info["data"]["user"]["pullRequests"]["totalCount"]
    user.commitComments = info["data"]["user"]["commitComments"]["totalCount"]
    user.issueComments = info["data"]["user"]["issueComments"]["totalCount"]
    user.gistComments = info["data"]["user"]["gistComments"]["totalCount"]
    user.organizations = [name["name"] for name in info["data"]["user"]["organizations"]["nodes"]]

    FileControl.saveJson(user.toDict(), diretorioPadrao, 'UserInfo.json', 'w')
    FileControl.saveJson(apiUser.getUserInfByYear(), diretorioPadrao, 'UserInfoByTime.json', 'w')


def repositoryUser(user):
    apiUser = ApiGitHub(user, 'token ' + token)

    OWNER, COLLABORATOR, ORGANIZATION_MEMBER = apiUser.pullRequestContribution(user.loginUser)

    print('O')
    for owner in OWNER:
        print(owner['nameWithOwner'])
        Repository('OWNER', user, owner)

    print('\n\nC')
    for collab in COLLABORATOR:
        print(collab['nameWithOwner'])
        Repository('COLLABORATOR', user, collab)

    print('\n\nORGANIZATION_MEMBER')
    for orgMem in ORGANIZATION_MEMBER:
        print(orgMem['nameWithOwner'])
        Repository('ORGANIZATION_MEMBER', user, orgMem)
    # print(repository.__dict__)



def getCommitUser():
    user = UserGit("username")
    apiUser = ApiGitHub(user, 'token ' + token)
    data = apiUser.getUserCommitContribution()
    teste = open(r"C:\Users\luiz_\OneDrive\Área de Trabalho\UserCommit.json", "w", encoding='UTF-8')
    json.dump(data, teste, indent=4)
    teste.close()

user = UserGit('rafaelfranca')
# proInfoUser(user)
repositoryUser(user)




# getCommitUser()

