from src.userGit import UserGit
from src.apiGitHub import ApiGitHub

user = UserGit('QuincyLarson')
apiUser = ApiGitHub(user)
apiUser.getPullRequestUsers()

