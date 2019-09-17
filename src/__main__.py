from src.apiGitHub import ApiGitHub
from src.userGit import UserGit

# try:
#     token = sys.argv[1]
# except:
#     print('Insira o tokem GitHub')
#     exit(0)


token = '********************'
user = UserGit('QuincyLarson')
apiUser = ApiGitHub(user, 'token ' + token)
apiUser.getPullRequestUsers()

