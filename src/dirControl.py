import os

class DirControl:
    def __index__(self, nameUser):
        userDir = '.\data\\' + nameUser
        self.newDir('.\data')
        self.__userDir = (userDir)
        self.newDir(self.userDir)

    def newDir(self, pwd):
        try:
            os.makedirs(pwd)
        except EOFError:
            print(EOFError.args)

    # @property
    # def nameUser(self):
    #     return self.__nameUser
    #
    # @nameUser.setter
    # def nameUser(self, nameUser):
    #     self.__nameUser = nameUser