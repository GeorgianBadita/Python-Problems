from domain.entities import Person
from domain.validators import ValidatorException


class PersonService:

    def __init__(self, rep, val):
        '''
        Initializse service
        :param rep: repository - object to store people
        :param val: validator - object to validate people
        '''
        self.__rep = rep
        self.__val = val

    def createPerson(self, idPers, name, addr):
        '''
        store a person
        :param idPers: string
        :param name: string
        :param addr: string
        :return: the person
        :post: student added to the repository
        :raise: RepositoryException - if person already exists
        :raise: ValidationException - if person fields are invalid
        '''
        #create a person object
        person = Person(idPers, name, addr)
        #validate person using validator object
        self.__val.validate(person)
        #store person into using repository
        self.__rep.store(person)
        return person

    def getAllPeople(self):
        '''

        :return: list of all people in the sysyem
        '''
        return self.__rep.getAll()


    def searchPerson(self, idPerson):
        '''
        Searches person after id
        :param idPerson:
        :return: the person
        '''
        allPeople = self.getAllPeople()
        for person in allPeople:
            if idPerson == person.getId():
                return person
        return None

    def deletePerson(self, idPerson):
        '''
        Delete a person after id if it exists
        :param idPerson:
        :return: returns the person to be deleted
        '''
        allPeople = self.getAllPeople()
        for person in allPeople:
            if idPerson == person.getId():
                personToReturn = person
                self.__rep.deleteElem(person)
                return personToReturn
        return None

    def modifyPerson(self, idPers, name, address):
        '''
        Modifies a person if it exists
        :param idPers:
        :return: returns the new Person
        '''
        try:
            newPerson = Person(idPers, name, address)
            self.__val.validate(newPerson)
            self.__rep.updateElem(newPerson)
            return newPerson
        except ValidatorException as ex:
            print(ex.args)
