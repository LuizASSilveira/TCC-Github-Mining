from src.apiGitHub import ApiGitHub
from src.userGit import UserGit
import pandas as pd
import json
import sys

try:
    token = sys.argv[1]
except:
    print('Insira o tokem GitHub')
    exit(0)

def getInfoUser():
    user = UserGit('luizSilveira')
    apiUser = ApiGitHub(user, 'token ' + token)
    mostPopularLanguages2 = ['JavaScript', 'Python', 'Java', 'PHP']
    apiUser.getUserFromRep(mostPopularLanguages2)


def proInfoUser():
    data = pd.read_json('ProjWithUser.json')
    arrayContribuidores = []
    for language in data:
        for array in data[language]:
            for proj in array:
                for contributors in array[proj]:
                    print(contributors)

                    user = UserGit(contributors)
                    apiUser = ApiGitHub(user, 'token ' + token)
                    info = apiUser.getUserInf(user)
                    user.location = info["data"]["user"]["location"]
                    user.email = info["data"]["user"]["email"]
                    user.name = info["data"]["user"]["name"]
                    user.createdAt = info["data"]["user"]["createdAt"]
                    user.company = info["data"]["user"]["company"]
                    user.issues = info["data"]["user"]["issues"]["totalCount"]
                    user.organizationTotal = info["data"]["user"]["organizations"]["totalCount"]
                    user.projects = info["data"]["user"]["projects"]["totalCount"]
                    user.gists = info["data"]["user"]["gists"]["totalCount"]
                    user.pullRequests = info["data"]["user"]["pullRequests"]["totalCount"]
                    user.commitComments = info["data"]["user"]["commitComments"]["totalCount"]
                    user.issueComments = info["data"]["user"]["issueComments"]["totalCount"]
                    user.organizations = [name["name"] for name in info["data"]["user"]["organizations"]["nodes"]]
                    arrayContribuidores.append(user)

                    infoByYear = apiUser.getUserInfByYear(user)
                    teste = open(r"C:\Users\luiz_\OneDrive\Área de Trabalho\testeUserTime.json", "w", encoding='UTF-8')
                    json.dump(infoByYear, teste, indent=4)
                    teste.close()
                    exit(0)




    file = open(r'C:\Users\luiz_\OneDrive\Área de Trabalho\infoUsers.csv', 'w', encoding='UTF-8')
    file.write("language; " + "loginName; "+"location; " + "email; " +"name; " +"createdAt; " +"company; " +"issues; " +"organizationTotal; " +"projects; " +"gists; " +"pullRequests; " +"commitComments; " +"issueComments; " +"organizations\n")
    for Contribuidor in arrayContribuidores:

        file.write(
            language+"; " +
            str(Contribuidor.loginUser)+"; " +
            str(Contribuidor.location)+"; " +
            str(Contribuidor.email)+"; " +
            str(Contribuidor.name)+"; " +
            str(Contribuidor.createdAt)+"; " +
            str(Contribuidor.company)+"; " +
            str(Contribuidor.issues)+"; " +
            str(Contribuidor.organizationTotal)+"; " +
            str(Contribuidor.projects)+"; " +
            str(Contribuidor.gists)+"; " +
            str(Contribuidor.pullRequests)+"; " +
            str(Contribuidor.commitComments)+"; " +
            str(Contribuidor.issueComments)+"; " +
            str(Contribuidor.organizations)+"\n"
        )
    file.close()

def repositoryUser(username):
    user = UserGit(username)
    apiUser = ApiGitHub(user, 'token ' + token)
    apiUser.getPullRequestUsers()

def getCommitUser():
    user = UserGit("username")
    apiUser = ApiGitHub(user, 'token ' + token)
    data = apiUser.getUserCommitContribution()
    teste = open(r"C:\Users\luiz_\OneDrive\Área de Trabalho\UserCommit.json", "w", encoding='UTF-8')
    json.dump(data, teste, indent=4)
    teste.close()


getCommitUser()
# proInfoUser()
# repositoryUser('QuincyLarson')
