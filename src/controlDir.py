import os


class ControlDir:
    def __init__(self, nameUser):
        directory = '.\data'
        self.newDirectory(directory)
        userDir = directory + '\\' + nameUser
        self.__userDirectory = userDir
        self.newDirectory(userDir)

    def validNameDirectory(self, pwd):
        pwd = pwd.split('\\')
        name = pwd.pop(-1)
        return name not in os.listdir('\\'.join(pwd))

    def newDirectory(self, pwd):
        if self.validNameDirectory(pwd):
            os.makedirs(pwd)

    @property
    def userDirectory(self):
        return self.__userDirectory
    #
    # @nameUser.setter
    # def nameUser(self, nameUser):
    #     self.__nameUser = nameUser
