from domain.apartment import testGetNumOfApartments, testAddtoCost, testModifyApartmentCost, testDeleteApartmentCost, \
    testDeleteFromAtoB, \
    testDeleteCostFromAll, testGetTotalCost, testCostsLargerThanSum, \
    testCostTypeFromAll, addCostControl, deleteCostControl, searchingCostControl, testTotalSumForCost, \
    testSortAfterType, \
    viewCostControl, testAddCommandController, testModifyCommandController, readCommand, \
    testParseCommand, commandController, testDeleteCommandController
from utils.helper import readInt, testConvertToLower, testConvertFromRoToEn, createNewList, \
    testCreateNewList, printMenu, printAddSubmenu, printDeleteSubmenu, printSearchSubmenu, printViewSubmenu

testCreateNewList()
testGetNumOfApartments()
testConvertFromRoToEn()
testConvertToLower()
testAddtoCost()
testModifyApartmentCost()
testDeleteApartmentCost()
testDeleteFromAtoB()
testDeleteCostFromAll()
testGetTotalCost()
testCostsLargerThanSum()
testCostTypeFromAll()
testTotalSumForCost()
testSortAfterType()
testAddCommandController()
testModifyCommandController()
testParseCommand()
testDeleteCommandController()



# USER INTERFACE PART


def startUI():
    '''
    Function that starts the user interface menu
    Takes no argument
    Doesn't return anything
    '''
    while True:
        try:
            specfiyMenu = readInt("Apasati 1 pentru Menu Based UI sau 2 pentru Command Based UI: ")
            if specfiyMenu == 1:
                menuBasedUI()
            elif specfiyMenu == 2:
                commandBasedUI()
            else:
                raise TypeError("NUMARUL INTRODUS POATE FI DOAR 1 SAU 2")
        except TypeError as msg:
            print(msg)




def menuBasedUI():
    '''
    control the menuBased UI
    :return:
    '''
    listOfApartments = initApartments()
    while True:
        printMenu()
        command = readInt("Selectati comanda dorita: ")
        if command == 1:
            printAddSubmenu()
            addCostControl(listOfApartments)
        elif command == 2:
            printDeleteSubmenu()
            deleteCostControl(listOfApartments)
        elif command == 3:
            printSearchSubmenu()
            searchingCostControl(listOfApartments)
        elif command == 4:
            printViewSubmenu()
            viewCostControl(listOfApartments)
        elif command == 5:
            exit()


def initApartments():
    numofApartments = readInt("Dati numarul de apartamente: ")
    listOfApartments = createNewList(numofApartments)
    return listOfApartments






#COMMAND LINE BASED MENU


def commandBasedUI():
    '''
    Controls the commandBased menu
    :return:
    '''
    listOfApartments = initApartments()
    while True:
        cmd = readCommand()
        try:
            commandController(listOfApartments, cmd)
        except ValueError as msg:
            print(msg)



startUI()

