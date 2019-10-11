class Commit:
    def __init__(self, user, repository, totalCountCommit, data):
        self.__userLogin = user.loginUser
        self.__userId = user.id
        self.__repositoryName = repository.nameWithOwner
        self.__totalCountCommit = totalCountCommit
        self.__url = data['url']
        self.__committedDate = data['committedDate']
        self.__authoredDate = data['authoredDate']
        self.__pushedDate = data['pushedDate']
        self.__authoredByCommitter = data['authoredByCommitter']
        self.__status = data['status']
        self.__changedFiles = data['changedFiles']
        self.__additions = data['additions']
        self.__deletions = data['deletions']
        self.__comments = data['comments']['totalCount']
        self.__deployments = data['deployments']['totalCount']
        self.__author = data['author']['user']['login']
        self.__committer = data['committer']['user']['login'] if data['committer']['user'] else data['committer']['user']
        self.__message = data['message']
        self.__messageBody = data['messageBody']
