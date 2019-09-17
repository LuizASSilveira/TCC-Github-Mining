class UserGit:
    def __init__(self, loginUser):
        self.__loginUser = loginUser
        self.__numberPullRequest = 0
        
    @property
    def loginUser(self):
        return self.__loginUser

    @property
    def numberPullRequest(self):
        return self.__numberPullRequest

    @numberPullRequest.setter
    def numberPullRequest(self, number):
        self.__numberPullRequest = number

