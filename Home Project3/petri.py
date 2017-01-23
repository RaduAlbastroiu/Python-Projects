
from locatie import locatie
from tranzit import tranzit

class sysPetri():

    # constructor
    def __init__(self):
        # number of runs
        self.__nrOfRuns = 0
        # every location this system has
        self.__locations = []
        # every transition this system has
        self.__transits = []

    # new location
    def addLoc(self):
        nrJetoane = int(input(" Enter the number of Counters in this location: "))
        newLoc = locatie(nrJetoane)
        self.__locations.append(newLoc)

    # new transition
    def addTrans(self):
        newTransit = tranzit()
        option = 1

        while option:
            # link between transitions and locations as long the user wants to add them
            option = int(input(" To add an input location press 1, to add an output location press 2, to finish press 3: "))

            if option == 1:
                # read location and add it as input for this transition
                nrloc = int(input(" Number of location(locations start with 1): "))
                if nrloc < len(self.__locations) + 1:
                    # if location exists it is added to this transition
                    flux = int(input(" Value of the flux on this arc: "))
                    newTransit.addIn(self.__locations[nrloc-1], flux)
                else:
                    # in case the location doesn't exist
                    print(" In the system are only " + str(len(self.__locations)) + " locations")

            # adding links between locations and tranzistions but this time for output
            if option == 2:
                nrloc = int(input(" Number of location(locations start with 1): "))
                if nrloc < len(self.__locations) + 1:
                    flux = int(input(" Value of the flux on this arc: "))
                    newTransit.addOut(self.__locations[nrloc-1], flux)
                else:
                    print(" In the system are only " + str(len(self.__locations)) + " locations")

            # this transition is added in the list of transitions
            if option == 3:
                self.__transits.append(newTransit)
                break

    # print locations
    def __printState(self):
         it = 0
         for aLoc in self.__locations:
            it += 1
            print(" Location with number " + str(it) + " has " + str(aLoc.nrJetoane()) + " Counters")

    # print locations before running
    def printStateSys(self):
        print()
        print(" The state of the system is the following: ")
        self.__printState()

    # this method choses the transition that should run and prints the state of locations after run
    def runSystem(self):
        self.__nrOfRuns += 1

        # search for active transitions
        it = 0
        activeTransistors = []
        for aTransit in self.__transits:
            it += 1
            if aTransit.isActive():
                activeTransistors.append(int(it))

        # if there are not active transitions the last state of the system will be printed
        if len(activeTransistors) == 0:
            print()
            print(" There is no tranzistor active and this is the last state of this system:")
            self.__printState()
            return False
        # if there are active transitions a list of them will be printed
        else:
            print(" From the list of active tranzistors chose the one you want to Activate:")
            for it in activeTransistors:
                print(" Tranzistor " + str(it) + " is good")

            # from the list of active transitions one will be chosed
            option = 0
            while not option in activeTransistors:
                option = int(input(" Your option: "))
                if not option in activeTransistors:
                    print(" Your option is not in the list of available tranzistors")

            # run transit
            self.__transits[option-1].runTransit()

            # print system state
            print()
            print(" The state after the " + str(self.__nrOfRuns) + " run is the following:")
            self.__printState()

            return True
