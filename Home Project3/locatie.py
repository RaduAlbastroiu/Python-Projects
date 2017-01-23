
class locatie():

    # constructor with token initializer
    def __init__(self, nrJetoane):
        self.__nrJ = nrJetoane
    
    # for a given flux value it is checked if the location is good
    def isGood(self, vFlux):
        if self.__nrJ >= vFlux:
            return True
        else:
            return False

    # add tokens to a location
    def addJetoane(self, nrJetoane):
        self.__nrJ += nrJetoane
    # substract tokens from a location
    def removeJetoane(self, nrJetoane):
        self.__nrJ -= nrJetoane
    # return number of tokens
    def nrJetoane(self):
        return self.__nrJ
