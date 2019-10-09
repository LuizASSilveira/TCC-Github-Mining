class Repository:
    def __init__(self, RepositoryAffiliation, user, data):
        self.__userLogin = user.loginUser
        self.__userId = user.id
        self.__RepositoryAffiliation = RepositoryAffiliation
        self.__nameWithOwner = data['nameWithOwner']
        self.__url = data['url']
        self.__diskUsage = data['diskUsage']
        self.__licenseInfo = data['licenseInfo']
        self.__isFork = data['isFork']
        self.__isLocked = data['isLocked']
        self.__isMirror = data['isMirror']
        self.__isPrivate = data['isPrivate']
        self.__isArchived = data['isArchived']
        self.__forkCount = data['forkCount']
        self.__labels = data['labels']['totalCount']
        self.__stargazers = data['stargazers']["totalCount"]
        self.__issues = data['issues']["totalCount"]
        self.__collaborators = data['collaborators']["totalCount"] if data['collaborators'] else 0
        self.__releases = data['releases']['totalCount']
        self.__assignableUsers = data['assignableUsers']['totalCount']
        self.__commitComments = data['commitComments']['totalCount']
        self.__watchers = data['watchers']['totalCount']
        self.__primaryLanguage = data["primaryLanguage"]['name'] if data['primaryLanguage'] else ''
        self.__descriptions = data['description']









