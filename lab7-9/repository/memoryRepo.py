from domain.entities import *

class RepositoryException(Exception):
    pass

class MemoryRepository:
    '''
    Class for the memory repository
    '''

    def __init__(self):
        self.__list = {}

    def store(self, elem):
        '''
        Store __list
        elem is the element of a class
        raise RepositoryException if we have an element with the same ID in list
        :param elem:
        :return:
        '''
        if elem.getId() in self.__list:
            raise RepositoryException()
        self.__list[elem.getId()] = elem

    def deleteElem(self, elem):
        '''
        Delete the element elem
        :param elem:
        :return:
        '''
        del self.__list[elem.getId()]

    def size(self):
        '''
        The number of element in the repository list
        :return: an integer number
        '''
        return len(self.__list)

    def getAll(self):
        '''
        return a list, list of all elements of __list
        :return:
        '''
        return  list(self.__list.values())

    def updateElem(self, newElem):
        '''
        modify an element if it exists
        :return:
        '''
        self.__list[newElem.getId()] = newElem