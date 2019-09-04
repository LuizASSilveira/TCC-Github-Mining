from userGit import UserGit
from apiGitHub import ApiGitHub

user = UserGit('QuincyLarson')
apiUser = ApiGitHub(user)

apiUser.getPullRequestUsers()

