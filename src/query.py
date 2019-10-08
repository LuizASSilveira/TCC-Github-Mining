class Query:
    @staticmethod
    def userCommitContribution():
        query = """
        {
            rateLimit{
                cost
                remaining
                resetAt
                }
          user(login:"QuincyLarson"){
            id
            url
            repositories(ownerAffiliations:OWNER, first:15){
              pageInfo{hasNextPage,endCursor}
              totalCount
              nodes{
                licenseInfo{name, nickname }
                stargazers{
                        totalCount
                }
                pullRequests{
                        totalCount
                }
                # collaborators{
                    # totalCount
                # }
                watchers{
                        totalCount
                        }
                forkCount
                issues(first:100){
                  totalCount
                  nodes{
                    title
                    bodyText
                    closed
                    createdAt
                    closedAt
                    number
                    url
                    labels(first:100){
                      totalCount
                      nodes{
                        name
                        description
                        
                      }
                    }
                  }
                }
                languages(first:100){
                        totalCount,
                        nodes{
                                name
                                }
                        }
        
                nameWithOwner
                isFork
                defaultBranchRef{
                  associatedPullRequests(first:100){
                    pageInfo{hasNextPage,endCursor}
                    nodes{
                      url,
                      number,
                      title,
                      body,
                      bodyText,
                    }
                    totalCount
                  }
                  target{
                    ... on Commit{
                      history(author:{id:"MDQ6VXNlcjk4NTE5Nw=="},first:100){
                        totalCount
                                nodes{
                        commitUrl
                        author{
                                user{
                                        login
                                }
                        }
                        committer{
                        user{
                                login
                                }
                        }
                        authoredByCommitter
                        changedFiles
                                    additions
                        deletions
                        message
                        messageBody
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
        """
        return query

    @staticmethod
    def getMax100CommitForPullRequests(loginUser, pullRequestsConfig):
        query = """
            {
                user(login: "userName"){
                    name,
                    avatarUrl,
                    createdAt,    
                    pullRequests(pullRequestsConfig){
                        pageInfo{
                            endCursor,
                            hasNextPage,
                        }
                        totalCount,
                        nodes{
                            commits(last:100){
                                totalCount,
                                pageInfo{
                                    endCursor,
                                    hasNextPage 
                                }, 
                                nodes{
                                     resourcePath,
                                     commit{
                                        abbreviatedOid
                                     },
                                    pullRequest{
                                        number
                                    }
                                }
                            }
                        }
                    }
                },
                viewer {
                    login
                },
                rateLimit {
                    limit
                    cost
                    remaining
                    resetAt
                }
            }
            """
        return query.replace('userName', loginUser).replace('pullRequestsConfig', pullRequestsConfig)

    @staticmethod
    def getAllCommitForPullRequest(userName, numberPull, commitInfo, state):
        query = """
        {
            user(login: "userName"){
                name,
                avatarUrl,
                createdAt,    
                pullRequests(first:1, states: stateQueryCommit){
                    nodes{
                        repository{
                            pullRequest(number:NumberPull){
                                commits(commitInfo){
                                    totalCount,
                                    pageInfo{
                                        endCursor,
                                        hasNextPage 
                                    }, 
                                    nodes{
                                        resourcePath
                                        commit{
                                            abbreviatedOid
                                        }
                                    }
                                }
                            }
                        } 
                    }
                }
            },
            viewer {
                login
            }
            rateLimit {
                limit
                cost
                remaining
                resetAt
            }
        }
            """
        return query.replace('userName', userName).replace('NumberPull', numberPull).replace('commitInfo',
                                                                                             commitInfo).replace(
            'stateQueryCommit', state)

    @staticmethod
    def userPerfilInfo(loginUser):
        query = """ 
             {
                  rateLimit {
                        cost
                        remaining
                        resetAt
                  }
                  user(login: loginUserName) {
                        id
                        avatarUrl
                        bio
                        url
                        websiteUrl
                        gistComments {
                            totalCount
                        }
                        watching {
                            totalCount
                        }
                        followers {
                            totalCount
                        }
                        following {
                            totalCount
                        }
                        location
                            email
                        name
                        createdAt
                        location
                        company
                        issues {
                            totalCount
                        }
                        organizations(first: 100) {
                        pageInfo {
                            endCursor
                            hasNextPage
                        }
                        nodes {
                            name
                        }
                        totalCount
                        }
                        projects {
                            totalCount
                        }
                        gists {
                            totalCount
                        }
                        pullRequests {
                            totalCount
                        }
                        commitComments {
                            totalCount
                        }
                        issueComments {
                            totalCount
                        }
                  }
             }
             """

        return query.replace('loginUserName', loginUser)

    @staticmethod
    def userInfoContributionsCollection(loginUser, year, month):
        query = """ 
            query { 
                user(login:"longinUser"){
                    contributionsCollection (from: "year-month-01T04:00:00Z", to: "year-month-31T23:59:59Z"){
                        totalRepositoryContributions,
                        totalPullRequestContributions,
                        totalCommitContributions,
                        totalIssueContributions,
                        totalPullRequestReviewContributions
                    }
                }
            }
            """
        return query.replace('longinUser', loginUser).replace("year", year).replace("month", month)

    @staticmethod
    def repInfo(after=''):
        query = """
        query repositroyInfo($numPage:Int!, $nameUser: String!, $RepositoryAffiliation : [RepositoryAffiliation!]){
          rateLimit {
            cost
            remaining
            resetAt
          }
          user(login: $nameUser) {
            repositories(ownerAffiliations: $RepositoryAffiliation, first: $numPage after) {
              pageInfo {
                endCursor
                hasNextPage
              }
              nodes {
                nameWithOwner
                url
                forkCount
                stargazers {
                  totalCount
                }
                issues {
                  totalCount
                }
                collaborators {
                  totalCount
                }
                primaryLanguage {
                  name
                }
                languages {
                  pageInfo{
                    endCursor
                    hasNextPage
                  }
                  nodes {
                    name
                  }
                }
                licenseInfo {
                  name
                  nickname
                }
                labels {
                  totalCount
                }
                releases {
                  totalCount
                }
                assignableUsers {
                  totalCount
                }
                commitComments {
                  totalCount
                }
                watchers {
                  totalCount
                }
                description
                diskUsage
                isFork
                isLocked
                isMirror
                isPrivate
                isArchived
              }
            }
          }
        }
        """

        if after:
            after = ', after: "'+after+'"'

        return query.replace('after', after)
