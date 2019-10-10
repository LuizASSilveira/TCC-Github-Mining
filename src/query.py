class Query:
    @staticmethod
    def repCommit():
        query = """
        query userRepositoryCommit($idUser: ID!, $numPageIssues: Int!, $owner: String!, $name: String!) {
          rateLimit {
            cost
            remaining
            resetAt
          }
          repository(owner: $owner, name: $name) {
            defaultBranchRef {
              target {
                ... on Commit {
                  history(author: {id: $idUser}, first: $numPageIssues) {
                    totalCount
                    pageInfo {
                      endCursor
                      hasNextPage
                    }
                    nodes {
                      url
                      pushedDate
                      comments {
                        totalCount
                      }
                      deployments {
                        totalCount
                      }
                      status {
                        state
                      }
                      committedDate
                      authoredByCommitter
                      authoredDate
                      changedFiles
                      additions
                      deletions
                      message
                      messageBody
                      author {
                        user {
                          login
                        }
                      }
                      committer {
                        user {
                          login
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
        return query.replace('userName', userName).replace('NumberPull', numberPull).replace('commitInfo', commitInfo).replace('stateQueryCommit', state)

    @staticmethod
    def getOrganizationremnant():
        query = """
            query userInfo($nameUser: String!, $after:String!) {
                rateLimit {
                    cost
                    remaining
                    resetAt
                    }
                    user(login: $nameUser) {
                        organizations(first: 100, after:$after) {
                        pageInfo {
                            endCursor
                            hasNextPage
                        }
                        nodes {
                        name
                        }
                    }
                }
            }
        """
        return query

    @staticmethod
    def userPerfilInfo():
        query = """ 
              query userInfo($nameUser:String!){
                  rateLimit {
                        cost
                        remaining
                        resetAt
                  }
                  user(login:$nameUser) {
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
                            totalCount
                            pageInfo {
                                endCursor
                                hasNextPage
                            }
                            nodes {
                                name
                            }
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

        return query

    @staticmethod
    def userInfoContributionsCollection():
        query = """ 
            query userContByYear($nameUser:String!, $fromDate:DateTime!, $toDate:DateTime!){ 
                rateLimit{
                    cost
                    remaining
                    resetAt
                }
                user(login:$nameUser){
                    contributionsCollection (from: $fromDate, to:$toDate){
                        totalRepositoryContributions,
                        totalPullRequestContributions,
                        totalCommitContributions,
                        totalIssueContributions,
                        totalPullRequestReviewContributions
                    }
                }
            }
        """
        return query

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
                pushedAt
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

    @staticmethod
    def repIssues():
        query = """
            query repInfo($numPageIssues: Int!,$owner:String!, $name:String!) {
                rateLimit {
                    cost
                    remaining
                    resetAt
                }
                repository(owner: $owner, name: $name) {
                    issues(orderBy: {field: CREATED_AT, direction: ASC}, first: $numPageIssues) {
                        totalCount
                        pageInfo {
                            endCursor
                            hasNextPage
                        }
                        nodes {
                            author {
                                login
                            }
                            authorAssociation
                            editor {
                                login
                            }
                            lastEditedAt
                            closed
                            locked
                            publishedAt
                            createdAt
                            closedAt
                            number
                            url
                            title
                            bodyText
                        }
                    }
                }
            }
        """
        return query