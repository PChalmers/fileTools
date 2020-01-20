from os import listdir
from os import path

class directoryTools:
    def __init__(self):
        pass

    fileNames = []

    def getDirectoryContents(self, dirPath):

        onlyFiles = [f for f in listdir(dirPath) if  path.isfile(path.join(dirPath, f))]
        onlyDirs = [d for d in listdir(dirPath) if  path.isdir(path.join(dirPath, d))]

        for file in onlyFiles:
            self.fileNames.append(path.join(dirPath, file))

        for dir in onlyDirs:
            obj = directoryTools()
            obj.getDirectoryContents(path.join(dirPath, dir))

        return self.fileNames



if __name__ == '__main__':
    dt = directoryTools()
    files = dt.getDirectoryContents(r'c:\@training')

    with open('files.txt', 'w') as f:
        for file in files:
            f.write(file + '\n')



