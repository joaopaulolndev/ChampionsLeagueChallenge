
import os.path

class AbstractModel:

    def __init__(self, season):
        if not os.path.isdir("data/" + season):
            raise Exception('Season not found')


    def verifiedFolderSeason(self, season):
        if not os.path.isdir("data/" + season):
            raise Exception('Season not found')
