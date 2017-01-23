
from locatie import locatie

class tranzit():

    # constructor
    def __init__(self):
        # locInput represent the list of input locations
        self.__locInput = []
        # fluxInput represent the flux value for each input location
        self.__fluxInput = []
        # locOutput represent the list of output locations
        self.__locOutput = []
        # fluxOutput represent the flux value for each output location
        self.__fluxOutput = []

    # method for adding a location input for this transition
    def addIn(self, loc, flux):
        self.__locInput.append(loc)
        self.__fluxInput.append(flux)

    # method for adding a location output for this transition
    def addOut(self, loc, flux):
        self.__locOutput.append(loc)
        self.__fluxOutput.append(flux)

    # this method checks if the transition is active
    def isActive(self):
        it = 0
        for loc in self.__locInput:
            var = int(self.__fluxInput[it])
            # se verifica daca numarul jetoanelor din locatie este mai decat fluxul pe acel arc
            if not loc.isGood(var): # isGood(var) method member in locatie.py
                return False  # if one location isn't good the transition isn't acitve
            it += 1
        return True

    # run this transit
    def runTransit(self):
        it = 0
        # for output location the flux is added
        for loc in self.__locOutput:
            loc.addJetoane(self.__fluxOutput[it])
            it += 1

        it = 0
        # for input location the flux is substracted
        for loc in self.__locInput:
            loc.removeJetoane(self.__fluxInput[it])
            it += 1
