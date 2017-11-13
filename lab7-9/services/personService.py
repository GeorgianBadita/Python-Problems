from domain.entities import Person
from domain.validators import ValidatorException


class PersonService:

    def __init__(self, rep):
        '''
        Initializse service
        :param rep: repository - object to store people
        :param val: validator - object to validate people
        '''
        self.__rep = rep

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
        return self.__rep.findElem(idPerson)

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
            self.__rep.updateElem(newPerson)
            return newPerson
        except ValidatorException as ex:
            print(ex.args)

    def printEnrolled(self, person, serviceEvents):
        '''
        Prints the events of a person
        :param person:
        :param serviceEvents:
        :return:
        '''
        enrolledIn = []
        events = serviceEvents.getAllEvents()
        for event in events:
            if person in event.getPersEnrolled():
               enrolledIn.append(event)
        if not len(enrolledIn):
            return None
        return enrolledIn


