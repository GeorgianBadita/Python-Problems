from itertools import product

def createList():
    '''
    Creates a list of numbers from 1 ... n
    :return: the number of elements and the list of numbers
    '''
    n = int(input("Give the number of elements in set: "))
    list = []
    for i in range(n):
        list.append(i)
    return [n, list]


def isAsociative(operation):
    '''
    Returns True if the operation is associative, False otherwise
    :param operation:
    :return:
    '''
    for i in range(len(operation)):
        for j in range(len(operation)):
            for z in range(len(operation)):
                if operation[operation[i][j]][z] != operation[i][operation[j][z]]:
                    return False
    return True


def printTables(operations):
    ''''
    Function that prints the table
    '''
    for key, value in operations.items():
       print(key + 1, file = open("output.txt", "a"))
       for i in range(len(value)):
           print(value[i], file = open("output.txt", "a"))
       print("\n", file = open("output.txt", "a"))


def convert(operation):
    '''
    Converts the operation table from int to char
    :param operation:
    :return:
    '''
    for i in range(len(operation)):
        for j in range(len(operation)):
            operation[i][j] = chr(ord('a') + operation[i][j])
    return operation


def genOperations(n, list):
    '''
    Generates every possible operation
    :param n:
    :param list:
    :return:
    '''
    numOfAsociative = 0
    associativeDictionary = {}
    for matrix in product(list, repeat = len(list)**2):
       operation = []
       cnt = 0
       for i in range(len(list)):
           secondOperation = []
           for j in range(len(list)):
               secondOperation.append(matrix[cnt])
               cnt += 1
           operation.append(secondOperation)
       if isAsociative(operation) == True:
            associativeDictionary[numOfAsociative] = convert(operation)
            numOfAsociative += 1
    print("There are " + str(n**(n*n)) + " operations, but only " + str(numOfAsociative) + " are associative", file = open("output.txt", "a"))
    printTables(associativeDictionary)





#START PROGRAM FUCNTIONS
open("output.txt", "w").close()
params = createList()
genOperations(params[0], params[1])
