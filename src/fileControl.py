import json


class FileControl:

    @staticmethod
    def saveJson(data, dir, nameFile, typeOpen='w', encodingFile='UTF-8'):

        dirFull = dir + '\\' + nameFile
        file = open(dirFull, typeOpen, encoding=encodingFile)
        json.dump(data, file, indent=4)
        file.close()

