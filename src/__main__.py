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



def proInfoUser(user):
    apiUser = ApiGitHub(user, 'token ' + token)
    apiUser.getUserInf()
    FileControl.saveJson(user.toDict(), diretorioPadrao, 'UserInfo.json', 'w')
    FileControl.saveJson(apiUser.getUserInfByYear(), diretorioPadrao, 'UserInfoByTime.json', 'w')


def repositoryUser(user):
    apiUser = ApiGitHub(user, 'token ' + token)
    OWNER, COLLABORATOR, ORGANIZATION_MEMBER = apiUser.pullRequestContribution(user.loginUser)
    repOwner = [owner.__dict__ for owner in OWNER] + [collab.__dict__ for collab in COLLABORATOR] + [org.__dict__ for org in ORGANIZATION_MEMBER]
    FileControl.saveJson(repOwner, diretorioPadrao, 'RepositoryOwner.json', 'w')


def getCommitUser():
    user = UserGit("username")
    apiUser = ApiGitHub(user, 'token ' + token)
    data = apiUser.getUserCommitContribution()
    teste = open(r"C:\Users\luiz_\OneDrive\Área de Trabalho\UserCommit.json", "w", encoding='UTF-8')
    json.dump(data, teste, indent=4)
    teste.close()


user = UserGit('rafaelfranca')
proInfoUser(user)
# repositoryUser(user)


# getCommitUser()
