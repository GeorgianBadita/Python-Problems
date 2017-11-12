from domain.entities import Person, Event
from utils.helper import dateValidation, hourValidation


class ValidatorException(Exception):

    def __init__(self, exceptions):
        self.errors = exceptions

    def getErrors(self):
        return self.errors

class PersonValidator:
    '''
    Class to validate person data
    '''

    def validate(self, person):
        '''
        Throws ValidatorException if fields are empty
        :param person:
        :return:
        '''
        exceptions = []
        if(person.getId() == ""):
            exceptions.append("Id can't be empty!")
        if(person.getName() == ""):
            exceptions.append("Name can't be empty")
        if(person.getAddress() == ""):
            exceptions.append("Address can't be empty")
        if len(exceptions) > 0:
            raise ValidatorException(exceptions)

class EventValidator:
    '''
    Class to validate event data
    '''


    def validate(self, event):
        '''
        Throws ValidationException if fields are invalid
        :param event:
        :return:
        '''
        #exceptions = []
        exceptions = dateValidation(event.getDate()) + hourValidation(event.getTime())
        if event.getId() == "":
            exceptions.append("Id can't be empty")
        if event.getDescr() == "":
            exceptions.append("Description can't be empty")
        if event.getDate() == "":
            exceptions.append("Date can't be empty")
        if event.getTime() == "":
            exceptions.append("Time can't be empty")
        if len(exceptions) > 0:
            raise ValidatorException(exceptions)

