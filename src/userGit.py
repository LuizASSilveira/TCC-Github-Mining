from src.apiGitHub import ApiGitHub


class UserGit:
    def __init__(self, loginUser):
        self.__loginUser = loginUser
        self.__id = ''
        self.__email = ''
        self.__name = ''
        self.__avatarUrl = ''
        self.__bio = ''
        self.__createdAt = ''
        self.__location = ''
        self.__company = ''
        self.__issues = ''
        self.__projects = ''
        self.__gists = ''
        self.__pullRequests = ''
        self.__commitComments = ''
        self.__issueComments = ''
        self.__watching = 0
        self.__followers = 0
        self.__following = 0
        self.__numberPullRequest = 0
        self.__totalRepositoryContributions = 0
        self.__totalPullRequestContributions = 0
        self.__totalCommitContributions = 0
        self.__totalIssueContributions = 0
        self.__gistComments = 0
        self.__organizationTotal = []
        self.__organizations = []
        self.__ContributionsForYear = {}

    def toDict(self):
        return self.__dict__
    @property
    def ContributionsForYear(self):
        return self.__ContributionsForYear

    @ContributionsForYear.setter
    def ContributionsForYear(self, ContributionsForYear):
        self.__ContributionsForYear = ContributionsForYear

    @property
    def organizationTotal(self):
        return self.__organizationTotal

    @organizationTotal.setter
    def organizationTotal(self, organizationTotal):
        self.__organizationTotal = organizationTotal

    @property
    def loginUser(self):
        return self.__loginUser

    @property
    def numberPullRequest(self):
        return self.__numberPullRequest

    @numberPullRequest.setter
    def numberPullRequest(self, number):
        self.__numberPullRequest = number

    @property
    def totalRepositoryContributions(self):
        return self.__totalRepositoryContributions

    @totalRepositoryContributions.setter
    def totalRepositoryContributions(self, totalRepositoryContributions):
        self.__totalRepositoryContributions = totalRepositoryContributions

    @property
    def totalPullRequestContributions(self):
        return self.__totalPullRequestContributions

    @totalPullRequestContributions.setter
    def totalPullRequestContributions(self, totalPullRequestContributions):
        self.__totalPullRequestContributions = totalPullRequestContributions

    @property
    def totalCommitContributions(self):
        return self.__totalCommitContributions

    @totalCommitContributions.setter
    def totalCommitContributions(self, totalCommitContributions):
        self.__totalCommitContributions = totalCommitContributions

    @property
    def totalIssueContributions(self):
        return self.__totalIssueContributions

    @totalIssueContributions.setter
    def totalIssueContributions(self, totalIssueContributions):
        self.__totalIssueContributions = totalIssueContributions

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location):
        self.__location = location

    @property
    def company(self):
        return self.__company

    @company.setter
    def company(self, company):
        self.__company = company

    @property
    def issues(self):
        return self.__issues

    @issues.setter
    def issues(self, issues):
        self.__issues = issues

    @property
    def organizations(self):
        return self.__organizations

    @organizations.setter
    def organizations(self, organizations):
        self.__organizations = organizations

    @property
    def projects(self):
        return self.__projects

    @projects.setter
    def projects(self, projects):
        self.__projects = projects

    @property
    def gists(self):
        return self.__gists

    @gists.setter
    def gists(self, gists):
        self.__gists = gists

    @property
    def pullRequests(self):
        return self.__pullRequests

    @pullRequests.setter
    def pullRequests(self, pullRequests):
        self.__pullRequests = pullRequests

    @property
    def commitComments(self):
        return self.__commitComments

    @commitComments.setter
    def commitComments(self, commitComments):
        self.__commitComments = commitComments

    @property
    def issueComments(self):
        return self.__issueComments

    @issueComments.setter
    def issueComments(self, issueComments):
        self.__issueComments = issueComments

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def createdAt(self):
        return self.__createdAt

    @createdAt.setter
    def createdAt(self, createdAt):
        self.__createdAt = createdAt

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def avatarUrl(self):
        return self.__avatarUrl

    @avatarUrl.setter
    def avatarUrl(self, avatarUrl):
        self.__avatarUrl = avatarUrl

    @property
    def bio(self):
        return self.__bio

    @bio.setter
    def bio(self, bio):
        self.__bio = bio

    @property
    def gistComments(self):
        return self.__gistComments

    @gistComments.setter
    def gistComments(self, gistComments):
        self.__gistComments = gistComments

    @property
    def watching(self):
        return self.__watching

    @watching.setter
    def watching(self, watching):
        self.__watching = watching

    @property
    def followers(self):
        return self.__followers

    @followers.setter
    def followers(self, followers):
        self.__followers = followers

    @property
    def following(self):
        return self.__following

    @following.setter
    def following(self, following):
        self.__following = following
