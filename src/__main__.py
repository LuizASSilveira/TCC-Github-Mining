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
    print('userInfo')
    apiUser.getUserInf()
    FileControl.saveJson(user.toDict(), diretorioPadrao, 'UserInfo.json', 'w')
    print('userInfoByYear')
    FileControl.saveJson(apiUser.getUserInfByYear(), diretorioPadrao, 'UserInfoByTime.json', 'w')


def repositoryUser(user):
    apiUser = ApiGitHub(user, 'token ' + token)
    print('Repositorys')
    OWNER, COLLABORATOR = apiUser.repositoryUser(user.loginUser)
    repOwner = [owner.__dict__ for owner in OWNER] + [collab.__dict__ for collab in COLLABORATOR]
    FileControl.saveJson(repOwner, diretorioPadrao, 'RepositoryOwner.json', 'w')
    # apiUser.getUserRepositoryIssues() #descontinuar ???????
    print('commit')
    resp = apiUser.getUserRepositoryCommit(OWNER + COLLABORATOR)
    FileControl.saveJson([r.__dict__ for r in resp], diretorioPadrao, 'Commit2.json', 'a')



def getCommitUser():
    user = UserGit("username")
    apiUser = ApiGitHub(user, 'token ' + token)
    data = apiUser.getUserCommitContribution()
    teste = open(r"C:\Users\luiz_\OneDrive\Área de Trabalho\UserCommit.json", "w", encoding='UTF-8')
    json.dump(data, teste, indent=4)
    teste.close()


FileControl.saveJson('', diretorioPadrao, 'Commit2.json', 'w')
user = UserGit('rafaelfranca')
proInfoUser(user)
repositoryUser(user)


# getCommitUser()
