class Person:
    '''
    Create a new person within the given
    idPerson, name and address all strings
    '''
    def __init__(self, idPerson, name, address):
        self.__id = idPerson
        self.__name = name
        self.__address = address

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getAddress(self):
        return self.__address

    def setId(self, newId):
        self.__id = newId

    def setName(self, newName):
        self.__name = newName

    def setAdr(self, newAddress):
        self.__address = newAddress

class Event:
    '''
    Create a new event within the given
    idEvent, date, time amd description all strings
    '''
    def __init__(self, idEvent, date, time, descr):
        self.__id = idEvent
        self.__date = date
        self.__time = time
        self.__descr = descr
        self.__persEnrolled = []

    def getId(self):
        return self.__id

    def getDate(self):
        return self.__date

    def getTime(self):
        return self.__time

    def getPersEnrolled(self):
        return self.__persEnrolled

    def getDescr(self):
        return self.__descr

    def setPersEnrolled(self, person):
        self.__persEnrolled.append(person)

    def setId(self, newId):
        self.__id = newId

    def setDate(self, newDate):
        self.__date = newDate

    def setTime(self, newTime):
        self.__time = newTime

    def setDescription(self, newDescr):
        self.__descr = newDescr