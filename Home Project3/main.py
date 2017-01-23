
from petri import sysPetri

# System declaration
System = sysPetri()

print(" First add locations and tranzistors then the system can be runned")

# adding locations
option = 1
while option > 0:
    option = int(input(" If you want to add a location press 1 else 0: "))
    if option == 1:
        System.addLoc()

# adding transitions
option = 1
while option > 0:
    option = int(input(" If you want to add a transition press 1 else 0: "))
    if option == 1:
        System.addTrans()

# sistem print
System.printStateSys()

# sistem run
option = 1
while option > 0:
    option = int(input(" If you want to run the system press 1 else 0: "))
    if option == 1:
        if System.runSystem() == False:
            break
