import os

path = "c:/tmp"
name = "file.txt"

class Setting:

    def __init__(self):
        self.fullpath = os.path.join(path, name)  # С помощью модуля os, соеденяем путь
        print(self.fullpath)
        #if not os.path.exists(self.fullpath):
            #open(self.fullpath, "w").close()

s = Setting()