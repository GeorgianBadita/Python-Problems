from utils.helper import createNewList, readInt, readStr, clearScreen, printCostLargerThanSum, printCostTypeFromAll, \
    convertFromEnToRo, convertFromRoToEng, printCommands

'''
The apartments List will be defined as a bi-dimensional list with n rows and 6 columns
Every column from an 'apartment' which is a list of numbers will have the following meaning:
COLUMN 1: WATER COSTS
COLUMN 2: GAS COSTS
COLUMN 3: HEATING COSTS
COLUMN 4: SEWERAGE COSTS
COLUMN 5: OTHERS
COLUMN 6: THE DATE IN WHICH THE COST WAS ADDED/DELETED/MODIFIED
'''

typeOfCosts = {
    "water" : 0,
    "gas" : 1,
    "heating" : 2,
    "sewerage" : 3,
    "others" : 4
}

date = {
    "day" : 5
}

def printCost(listOfApartments, index):
    '''
    Function that prints the cost from an apartment
    '''
    print("Apartamentul ", index + 1)
    for key in typeOfCosts:
        print(convertFromEnToRo(key), " ", listOfApartments[index][typeOfCosts[key]])
    print("zi ", listOfApartments[index][date['day']])
    print("\n"*3)

def getNumOfApartments(listOfApartments):
    '''
    Function to calculate the number of apartments
    Takes one argument, the listOfApartments
    Returns the number of apartments
    '''
    return len(listOfApartments)


def testGetNumOfApartments():
    '''
    Function to thest the getNumOfApartments function
    Takes no parameters
    Doesn't return anything
    '''
    testList = createNewList(21)
    assert getNumOfApartments(testList) == 21
    testList = createNewList(0)
    assert getNumOfApartments(testList) == 0
    testList = createNewList(125)
    assert getNumOfApartments(testList) == 125

#CREATING AND ADDING COSTS PART

def addToCost(listOfApartments, index, sum, type, day):
    '''
    Function to add a new cost to an existing one
    Takes 4 arguments: the list of apartments, the index of the apartment, the sum of the cost and it's type
    Doesn't return anything
    '''
    listOfApartments[index][typeOfCosts[type]] += sum
    listOfApartments[index ][date['day']] = day


def testAddtoCost():
    '''
    Function to test the addToCost function
    Takes no arguments
    Doesen't return anything
    '''
    testList = createNewList(1)
    addToCost(testList, 0, 124, 'water', 24)
    assert testList == [[124, 0, 0, 0, 0, 24]]
    addToCost(testList, 0, 120, 'water', 1)
    assert testList == [[244, 0, 0, 0, 0, 1]]
    addToCost(testList, 0, 90, 'heating', 19)
    assert testList == [[244, 0, 90, 0, 0, 19]]


def modifyApartmentCost(listOfApartments, index, sum, type, day):
    '''
    Function to modify an apartment cost from the list
    Takes 4 arguments: the list of apartments, the index of apartment, the sum and its cost
    Doesn't return anything
    '''
    listOfApartments[index][typeOfCosts[type]] = sum
    listOfApartments[index][date['day']] = day


def testModifyApartmentCost():
    '''
    Function to test the modifyApartmentCost function
    Takes no argument
    Doesn't return anything
    '''
    emptyList = [0, 0, 0, 0, 0, 0]
    testList = createNewList(2)
    testList.append([0, 0, 125, 0, 0, 0])
    testList.append([0, 0, 0, 0, 0, 0])
    modifyApartmentCost(testList, 3, 20, 'water', 13)
    assert testList == [emptyList, emptyList, [0, 0, 125, 0, 0, 0], [20, 0, 0, 0, 0, 13]]
    modifyApartmentCost(testList, 2, 42, 'heating', 15)
    assert testList == [emptyList, emptyList, [0, 0, 42, 0, 0, 15], [20, 0, 0, 0, 0, 13]]


#DELETE PART

def deleteApartmentCost(listOfApartments, index, day):
    '''
    Function to delete all the costs of an apartment
    Takes two arguments the list of apartments and the index
    Doesn't return anything
    '''
    emptyList = [0, 0, 0, 0, 0, day]
    listOfApartments[index] = emptyList


def testDeleteApartmentCost():
    '''
    Function to test the deleteApartment function
    Takes no arguments
    Doesn't return anything
    '''
    emptyList = [0, 0, 0, 0, 0, 0]
    testList = [emptyList, emptyList, [0, 0, 125, 0, 0, 0], [20, 0, 0, 0, 0, 0]]
    deleteApartmentCost(testList, 2, 5)
    assert testList == [emptyList, emptyList, [0, 0, 0, 0, 0, 5], [20, 0, 0, 0, 0, 0]]
    deleteApartmentCost(testList, 3, 6)
    assert testList == [emptyList, emptyList,  [0, 0, 0, 0, 0, 5], [0, 0, 0, 0, 0, 6]]


def deleteFromAtoB(listOfApartments, A, B):
    '''
    Function to delete apartments costs between index A and index B
    Takes 3 parameters, the list of apartments, the starting index and the ending index
    Doesn't return anything
    '''

    emptyList = [0, 0, 0, 0, 0, 0]
    for i in range(A, B):
        listOfApartments[i] = emptyList


def testDeleteFromAtoB():
    '''
    Function to test the function deleteFromAtoB
    Takes no arguments
    Doesn't return anyhting
    '''
    emptyList = [0, 0, 0, 0, 0, 0]
    testList = createNewList(4)
    deleteFromAtoB(testList, 2, 4)
    assert testList == [emptyList]*4
    modifyApartmentCost(testList, 2, 123, 'water', 1)
    modifyApartmentCost(testList, 3, 123, 'gas', 2)
    modifyApartmentCost(testList, 0, 123, 'heating', 3)
    deleteFromAtoB(testList, 2, 3)
    assert testList == [[0, 0, 123, 0, 0, 3], emptyList, emptyList, [123, 123, 0, 0, 0, 2]]


def deleteCostFromAll(listofApartments, type, day):
    '''
    Delet the cost of some type from all apartments
    Takse the list of apartments and a type of cost as arguemts
    Doesen't return anything
    '''
    for i in range(0, len(listofApartments)):
        listofApartments[i][typeOfCosts[type]] = 0
        listofApartments[i][date['day']] = day


def testDeleteCostFromAll():
    '''
    Function to test the function deleteCostFromAll
    Takes no arguments
    Doesen't return anything
    '''
    tmpList = [0, 0, 0, 0, 0, 5]
    testList = createNewList(4)
    deleteCostFromAll(testList, 'gas', 5)
    assert testList == [tmpList] * 4
    modifyApartmentCost(testList, 2, 123, 'water', 1)
    modifyApartmentCost(testList, 3, 123, 'gas', 2)
    modifyApartmentCost(testList, 0, 123, 'water', 3)
    deleteCostFromAll(testList, 'water', 7)
    tmpList[5] = 7
    assert testList == [tmpList, tmpList, tmpList, [0, 123, 0, 0, 0, 7]]


#SEARCHING PART

def getTotalCost(listofApartments, index):
    '''
    Function that calculates the total cost of an apartment
    Takes the list of apartments and the the index of the apartment as input
    Return the total cost of an apartment
    '''
    totalCost = 0
    for i in typeOfCosts:
        totalCost += listofApartments[index][typeOfCosts[i]]
    return  totalCost


def testGetTotalCost():
    '''
    Function that test the function getTotalCost
    Takes no arguments
    Doesn't return anything
    '''
    testList = createNewList(4)
    assert getTotalCost(testList, 2) == 0
    modifyApartmentCost(testList, 2, 123, 'water', 1)
    modifyApartmentCost(testList, 3, 123, 'gas', 2)
    modifyApartmentCost(testList, 2, 120, 'others', 3)
    modifyApartmentCost(testList, 0, 123, 'heating', 4)
    assert getTotalCost(testList, 2) == 243


def costsLargerThanSum(listOfApartments, sum):
    '''
    Function that returns all apartments with totalCost > sum
    Takes 2 arguments the list of apartments and the sum
    Returns a list of apartments with totalCost > sum
    '''
    newApartments = []
    for i in range(len(listOfApartments)):
        if getTotalCost(listOfApartments, i) > sum:
            newApartments.append(i)
    return newApartments


def testCostsLargerThanSum():
    '''
    Function to test the function costsLargerThanSum
    Takes no arguments
    Doesn't return anything
    '''
    testList = createNewList(4)
    assert costsLargerThanSum(testList, 0) == []
    modifyApartmentCost(testList, 2, 123, 'water', 1)
    modifyApartmentCost(testList, 3, 123, 'gas', 2)
    modifyApartmentCost(testList, 2, 120, 'others', 3)
    modifyApartmentCost(testList, 0, 123, 'heating', 4)
    assert costsLargerThanSum(testList, 119) == [0, 2, 3]


def costTypeFromAll(listOfApartments, type):
    '''
    Function that returns a type of cost from all apartments
    Takes two arguments, the list of apartments and the type of cost
    Returns a list, representing the value of a cost from every apartment
    '''
    newApartments = []
    for i in range(len(listOfApartments)):
        newApartments.append(listOfApartments[i][typeOfCosts[type]])
    return newApartments


def testCostTypeFromAll():
    '''
    Function to test the function costTypeFromAll
    Takes no arguments
    Doesn't return anything
    '''
    testList = createNewList(4)
    assert costTypeFromAll(testList, 'water') == [0, 0, 0, 0]
    modifyApartmentCost(testList, 2, 123, 'water', 1)
    modifyApartmentCost(testList, 3, 123, 'water', 2)
    modifyApartmentCost(testList, 1, 120, 'water', 3)
    modifyApartmentCost(testList, 0, 123, 'heating', 4)
    assert costTypeFromAll(testList, 'water') == [0, 120, 123, 123]


def costBeforDay(listOfApartments, day, sum):
    '''
    Function that prints all the costs before a day and larger than a sum
    Takes the list of costs, the day and the sum as arguments
    Returns the costs made before the day and larger than sum
    '''
    for cost in range(0, len(listOfApartments)):
        if listOfApartments[cost][date['day']] and getTotalCost(listOfApartments, cost) > sum:
            printCost(listOfApartments, cost)

#VIEW PART
def totalSumForCost(listOfApartments, type):
    '''
    Function that calculates the total sum of some cost
    Takes the list of costs and the type of cost as arguments
    Returns a list with 2 elements, the sum and the type of cost
    '''
    totalCost = 0
    for cost in listOfApartments:
        totalCost += cost[typeOfCosts[type]]
    return [type, totalCost]

def testTotalSumForCost():
    testList = createNewList(4)
    assert totalSumForCost(testList, 'water') == ['water', 0]
    modifyApartmentCost(testList, 2, 123, 'water', 1)
    modifyApartmentCost(testList, 3, 123, 'gas', 2)
    modifyApartmentCost(testList, 2, 120, 'water', 3)
    modifyApartmentCost(testList, 0, 123, 'gas', 4)
    assert totalSumForCost(testList, 'water') == ['water', 120]
    assert totalSumForCost(testList, 'gas') == ['gas', 246]


def sortAfterType(listOfApartments, type):
    '''
    Function to print the list of apartments sorted after some type of cost
    :param listOfApartments: list of costs
    :param type: type of cost
    :return: listOfApartments sorted by index
    '''
    sortedList = sorted(range(len(listOfApartments)), key=lambda k : listOfApartments[k][typeOfCosts[type]])
    return sortedList

def testSortAfterType():
    testList = createNewList(4)
    #print(sortAfterType(testList, 'water'))
    assert sortAfterType(testList, 'water') == [0, 1, 2, 3]
    modifyApartmentCost(testList, 3, 119, 'water', 1)
    modifyApartmentCost(testList, 2, 156, 'water', 2)
    modifyApartmentCost(testList, 1, 120, 'water', 3)
    modifyApartmentCost(testList, 0, 200, 'water', 4)
    #print(sortAfterType(testList, 'water'))
    assert sortAfterType(testList, 'water') == [3, 1, 2, 0]

def printSortedAfterType(listOfApartments, type):
    listToPrint = sortAfterType(listOfApartments, type)
    for apartment in listToPrint:
        printCost(listOfApartments, apartment)

#COMMANDS CONTROL

def addCostControl(listOfApartments):
    '''
    Function that controls the subcommand1 (adding a new cost to an apartment)
    Takes no arguments
    Doesn't return anything
    '''
    print("\n")
    subCommand = readInt("Selectati comanda dorita: ")
    print("\n"*2)
    if subCommand == 1:
        try:
            index = readInt("Dati numarul apartamentului: ")
            sumCost = readInt("Dati suma cheltuielii: ")
            type = readStr("Specificati tipul cheltuielii: ")
            day = readInt("Dati ziua in care se adauga cheltuiala: ")
            addToCost(listOfApartments, index - 1, sumCost, type, day)
            clearScreen()
        except IndexError:
            print("\nIndexul este prea mare sau negativ !!\n")
    elif subCommand == 2:
        try:
            index = readInt("Dati numarul apartamentului ")
            sumCost = readInt("Dati suma cheltuielii: ")
            type = readStr("Specificati tipul cheltuielii: ")
            day = readInt("Dati ziua in care se modifica cheltuiala: ")
            modifyApartmentCost(listOfApartments, index - 1, sumCost, type, day)
            clearScreen()
        except IndexError:
            print("\nIndexul este prea mare sau negativ!!\n")


def deleteCostControl(listOfApartments):
    '''
    Function that controls the subcommand2 (deleting cost of an apartment)
    Takes no arguments
    Doesn't return anything
    '''
    print("\n"*2)
    subCommand = readInt("Selectati comanda dorita :")
    print("\n"*2)
    if subCommand == 1:
        try:
            index = readInt("Dati numarul apartamentului: ")
            day = readInt("Dati ziua in care se face stergerea: ")
            deleteApartmentCost(listOfApartments, index - 1, day)
            clearScreen()
        except IndexError:
            print("Indexul este prea mare sau prea mic!!")
    elif subCommand == 2:
        try:
            startIndex = readInt("Dati primul apartamentul de la care se incepe stergerea: ")
            endIndex = readInt("Dati ultimul apartament la care se face stergere")
            if startIndex > endIndex:
                startIndex,endIndex = endIndex,startIndex
            deleteFromAtoB(listOfApartments, startIndex - 1, endIndex)
            clearScreen()
        except IndexError:
            print("Indecsii sunt prea mari sau prea mici!!")
    elif subCommand == 3:
        type = readStr("Dati tipul de cheltuiala care se vrea a fi stearsa: ")
        date = readInt("Dati ziua in care se face stergerea: ")
        deleteCostFromAll(listOfApartments, type, date)
        clearScreen()


def searchingCostControl(listOfApartments):
    '''
    Function that controls the searching part of the aplication
    Takes the list of costs as parameter
    Doesn't return anything
    '''
    print("\n")
    subCommand = readInt("Selectati comanda dorita :")
    print("\n"*2)
    if subCommand == 1:
        sum = readInt("Dati suma de comparare: ")
        print("\n"*2)
        printCostLargerThanSum(costsLargerThanSum(listOfApartments, sum), sum)
        print("\n"*2)
    elif subCommand == 2:
        type = readStr("Dati tipul de cheltuiala ce se vrea afisat de la toate apartamentele: ")
        printCostTypeFromAll(costTypeFromAll(listOfApartments, type), type)
    elif subCommand == 3:
        day = readInt("Dati ziua: ")
        sum = readInt("Dati suma de comparare: ")
        costBeforDay(listOfApartments, day, sum)

def viewCostControl(listOfApartments):
    '''
    Function that controls the view part of the aplication
    :param listOfApartments:
    :return: None
    '''

    print("\n")
    subCommand = readInt("Selectati comanda dorita: ")
    print("\n" * 2)
    if subCommand == 1:
        type = readStr("Dati tipul de cheltuiala: ")
        totalSum = totalSumForCost(listOfApartments, type)
        print("Suma totala pentru ", convertFromEnToRo(totalSum[0]), " este ", totalSum[1])
        print("\n" * 2)
        print("\n" * 2)
    elif subCommand == 2:
        type = readStr("Dati tipul de cheltuiala dupa care se vrea a fi sortata lista: ")
        printSortedAfterType(listOfApartments, type)
    elif subCommand == 3:
        try:
            index = readInt("Dati numarul apartamentului pentru tiparirea costului: ")
            print("Costul total pentru apartamentul ", index,  " este ", getTotalCost(listOfApartments, index - 1))
        except IndexError:
            print("Indxul este prea mare sau prea mic!!")


#COMMAND BASED CONTROLS

#adauga nrApartament sumaCost tipCost ziua
def addCommandController(listOfApartments, command):
    '''
    Function that controls adding cost part
    :param listOfApartments:
    :param command:
    :return:
    '''
    try:
        if len(command) != 4: raise ValueError("Indexul trebuie sa fie un numar intreg pozitib!!!")
        #TODO add description
        index = int(command[0])
        sumCost = int(command[1])
        costType = convertFromRoToEng(command[2])
        if costType not in typeOfCosts:
            raise KeyError("Tipul costului trebuie sa fie valid!!")
        day = int(command[3])
        addToCost(listOfApartments, index - 1, sumCost, costType, day)
    except ValueError as msg:
        print(msg)
    except IndexError:
        print("Indexul trebuie sa fie un numar intreg pozitiv!!")
    except KeyError as ex:
        print(ex)


def testAddCommandController():
    emptyList = [0, 0, 0, 0, 0, 0]
    testList = createNewList(4)
    addCommandController(testList, ['3', '120', 'apa', '15'])
    assert testList == [emptyList, emptyList, [120, 0, 0, 0, 0, 15], emptyList]
    addCommandController(testList, ['2', '99', 'incalzire', '22'])
    assert testList == [emptyList, [0, 0, 99, 0, 0, 22], [120, 0, 0, 0, 0, 15], emptyList]
    addCommandController(testList, ['3', '120', 'apa', '16'])
    assert testList == [emptyList, [0, 0, 99, 0, 0, 22], [240, 0, 0, 0, 0, 16], emptyList]

def deleteCommandController(listOfApartments, command):
    '''
    Function that controls the delete part of the aplication
    :param listOfApartments:
    :param command:
    :return:
    '''
    if len(command) > 1 and command[1] == ',':
        try:
            if len(command) != 3:
                raise ValueError("Comanda trebuie sa fie valida!")
            startIndex = int(command[0])
            endIndex = int(command[2])
            if startIndex > endIndex:
                startIndex,endIndex = endIndex,startIndex
            deleteFromAtoB(listOfApartments, startIndex - 1, endIndex)
        except IndexError:
            print("startIndex si stopIndex trebuie sa fie numere intregi pozitive!!")
        except ValueError:
            print("startIndex si stopIndex trebuie sa fie numere intregi pozitive!!")

    elif len(command) > 1 and  command[0] == 'de' and command[1] == 'la':
        try:
            if len(command) != 4:
                raise ValueError("Comanda trebuie sa fie Valida!")
            index = int(command[2])
            day = int(command[3])
            deleteApartmentCost(listOfApartments, index - 1, day)
        except ValueError:
            print("Indexul trebuie sa fie un numar intreg pozitiv")
        except IndexError:
            print("Indexul este prea mare sau negativ!")
    elif len(command) != 0 and  convertFromRoToEng(command[0]) in typeOfCosts:
        try:
            if not convertFromRoToEng(command[0]) in typeOfCosts:
                raise KeyError("Tip de cost invalid")
            type = convertFromRoToEng(command[0])
            day = int(command[1])
            deleteCostFromAll(listOfApartments,type, day)
        except KeyError as msg:
            print(msg)
    else:
        print("Comanda invalida!!!")


def testDeleteCommandController():
    emptyList = [0, 0, 0, 0, 0, 0]
    testList = createNewList(4)
    addCommandController(testList, ['3', '120', 'apa', '15'])
    assert testList == [emptyList, emptyList, [120, 0, 0, 0, 0, 15], emptyList]
    deleteCommandController(testList, ['1', ',', '3'])
    assert testList == [emptyList, emptyList, emptyList, emptyList]
    addCommandController(testList, ['3', '120', 'apa', '16'])



def modifyCommandController(listOfApartments, command):
    '''
    Function that modifies costs
    :param listOfApartments:
    :param command:
    :return:
    '''
    try:
        if len(command) != 4:
            raise ValueError("Comanda gresita!!!")
        index = int(command[0])
        sumCost = int(command[1])
        costType = convertFromRoToEng(command[2])
        if not costType in typeOfCosts:
            raise KeyError("Tipul costului trebuie sa fie valid!")
        day = int(command[3])
        modifyApartmentCost(listOfApartments, index - 1, sumCost, costType, day)
    except ValueError as msg:
        print(msg)
    except IndexError:
        print("Indexul trebuie sa fie numar intreg pozitiv")
    except KeyError as ex:
        print(ex)


def testModifyCommandController():
    emptyList = [0, 0, 0, 0, 0, 0]
    testList = createNewList(4)
    modifyCommandController(testList, ['3', '120', 'apa', '15'])
    assert testList == [emptyList, emptyList, [120, 0, 0, 0, 0, 15], emptyList]
    modifyCommandController(testList, ['2', '99', 'incalzire', '22'])
    assert testList == [emptyList, [0, 0, 99, 0, 0, 22], [120, 0, 0, 0, 0, 15], emptyList]


def printsCommandController(listOfApartments, command):
    '''
    Function that controls the user prints
    :param listOfApartments:
    :param command:
    :return:
    '''

    if command[0] == '>':
        try:
            if len(command) != 2:
                raise ValueError("Comanda trebuie sa fie valida!")
            sum = int(command[1])
            printCostLargerThanSum(costsLargerThanSum(listOfApartments, sum), sum)
        except ValueError as msg:
            print(msg)
    elif command[0] == 'toate':
        try:
            if len(command) != 2:
                raise ValueError("Comanda trebuie sa fie valida!!")
            type = convertFromRoToEng(command[1])
            if not type in typeOfCosts:
                raise KeyError("Tipul costului trebuie sa fie valid!")
            printCostTypeFromAll(costTypeFromAll(listOfApartments, type), type)
        except KeyError as msg:
            print(msg)
        except ValueError as ex:
            print(ex)
    elif len(command) > 2 and command[0] == '<' and command[2] == '>':
        try:
            if len(command) != 4:
                raise ValueError("Comanda trebuie sa fie valida!")
            day = int(command[1])
            sum = int(command[3])
            costBeforDay(listOfApartments, day, sum)
        except ValueError as msg:
            print(msg)
    else:
        print("Comanda invalida!!!")

def listCommandController(listOfApartments, command):
    '''
    Function that prints the sorted list of apartments
    :param listOfApartments:
    :param command:
    :return:
    '''
    try:
        if len(command) != 2:
            raise IndexError("Comanda nu este valida!!")
        costType = convertFromRoToEng(command[1])
        if not costType in typeOfCosts: raise KeyError("Tipul Costului trebuie sa fie valid")
        printSortedAfterType(listOfApartments, costType)
    except KeyError as msg:
        print(msg)
    except IndexError as ex:
        print(ex)


def viewCommandController(listOfApartments, command):
    '''
    Function for views
    :param listOfApartments:
    :param command:
    :return:
    '''
    if len(command) == 1 and convertFromRoToEng(command[0]) in typeOfCosts:
        type = convertFromRoToEng(command[0])
        totalSum = totalSumForCost(listOfApartments, type)
        print("Suma totala pentru ", convertFromEnToRo(totalSum[0]), " este ", totalSum[1])
    elif len(command) == 1:
        try:
            index = int(command[0])
            printCost(listOfApartments, index - 1)
        except ValueError:
            print("Indexul trebuie sa fie un numar intreg pozitiv!!")
        except IndexError:
            print("Indexul trebuie sa fie un numar intreg pozitiv!!")

    else:
        print("Comanda invalida!!!")


def readCommand():
    '''
    Reads Command
    '''
    cmd = input("Dati comanda dorita/Scrieti help pentru comenzi: ")
    return cmd.lower()


def parseCommand(command):
    '''

    :param command:
    :return:
    '''
    command = command.lstrip(" ")
    pos = command.find(" ")

    if pos == -1:
        return command, []

    cmds = command[: pos]
    args = command[pos + 1: ].split()

    return cmds, args


def testParseCommand():
    assert parseCommand("sterge de la 1 la 10") == ('sterge', ['de', 'la', '1', 'la', '10'])
    assert parseCommand("adauga 10 100 apa 15") == ('adauga', ['10', '100', 'apa', '15'])


def commandController(listOfApartments, command):
    '''

    :param command:
    :return:
    '''

    command = parseCommand(command)
    if command[0] == 'help':
        printCommands()
    elif command[0] == 'adauga':
        addCommandController(listOfApartments, command[1])
    elif command[0] == 'sterge':
        deleteCommandController(listOfApartments, command[1])
    elif command[0] == 'modifica':
        modifyCommandController(listOfApartments, command[1])
    elif command[0] == 'afiseaza':
        printsCommandController(listOfApartments, command[1])
    elif command[0] == 'lista':
        listCommandController(listOfApartments, command[1])
    elif command[0] == 'tipareste':
        viewCommandController(listOfApartments, command[1])
    elif command[0] == 'iesire':
        exit()
    else:
        raise ValueError("Comanda introdusa gresit, tastati help pentru a vedea comenzile posibile!!!")
