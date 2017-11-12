from domain.validators import ValidatorException
from repository.memoryRepo import RepositoryException



class Console:
    '''
    Class for the console program
    '''
    def __init__(self, servicePeople, serviceEvents):
        self.__servicePeople = servicePeople
        self.__serviceEvents = serviceEvents

    def __showAllPerople(self):
        '''
        View (print) all people from the catalog
        :return:
        '''
        people = self.__servicePeople.getAllPeople()
        if len(people) == 0:
            print("No people in the list")
        else:
            print("Id   Name      Address")
        for person in people:
            print(person.getId(), person.getName(), person.getAddress())

    def __addPerson(self):
        '''
        Add person read from console
        :return:
        '''
        idPers = input("Give person ID: ")
        name = input("Give person name: ")
        addr = input("Give person address: ")
        try:
            person = self.__servicePeople.createPerson(idPers, name, addr)
            print("Person " + person.getName() + " saved...")
        except RepositoryException:
            print("Duplicated person ID")
        except ValidatorException as ex:
            print(ex.getErrors())


    def __searchPerson(self):
        '''
        Search for a person after its id
        :return:
        '''
        try:
            idPers = input("Give the person ID: ")
            person = self.__servicePeople.searchPerson(idPers)
            self.printPerson(idPers, person)
        except TypeError as ex:
            print(ex)


    def __deletePerson(self):
        '''
        Delete a person if it exists
        :return:
        '''
        idPers = input("Give person ID: ")
        person = self.__servicePeople.deletePerson(idPers)
        if person == None:
            print("There are no people with the ID ", idPers)
        else:
           print(person.getName(), " was deleted")


    def __modifyPerson(self):
        '''
        Modify a person if it exists
        :return:
        '''
        try:
            idPers = input("Give person ID: ")
            person = self.__servicePeople.searchPerson(idPers)
            self.printPerson(idPers, person)
            name = input("Give the new name of the person: ")
            address = input("Give the new address of the person: ")
            person = self.__servicePeople.modifyPerson(idPers, name, address)
            self.printPerson(idPers, person)
        except TypeError as ex:
            print(ex)

    def printPerson(self, idPers, person):

        if person == None: raise TypeError("The persin with ID "+ idPers + ' does not exist')
        else:
            print("Id   Name      Address")
            print(person.getId(), person.getName(), person.getAddress())


    def __showAllEvents(self):
        '''
        View (print) all events from the list
        :return:
        '''
        events = self.__serviceEvents.getAllEvents()
        if len(events) == 0:
            print("No events in the list")
        else:
            print("Id   Date    Time    Description")
        for event in events:
            print(event.getId(), event.getDate(), event.getTime(), event.getDescr())

    def __addEvent(self):
        '''
        Add event read from console
        :return:
        '''
        idEvent = input("Give event ID: ")
        date = input("Give event date in format (dd/mm/yyyy): ")
        time = input("Give event time in format (hh:mm): ")
        descr = input("Give description to the event: ")
        try:
            event = self.__serviceEvents.createEvent(idEvent, date, time, descr)
            print("Event " + event.getId() + " saved...")
        except RepositoryException:
            print("Duplicated event ID")
        except ValidatorException as ex:
            print(ex.getErrors())


    def __searchEvent(self):
        '''
        Searches for an event after its id
        :return:
        '''
        try:
            idEvent = input("Give the event ID: ")
            event = self.__serviceEvents.searchEvent(idEvent)
            self.printEvent(idEvent, event)
        except TypeError as ex:
            print(ex)

    def printEvent(self, idEvent, event):

        if event == None: raise TypeError("There is np such event with ID " + idEvent)
        else:
            print("Id   Name    Date    Time    Description")
            print(event.getId(), event.getDate(), event.getTime(), event.getDescr())


    def __deleteEvent(self):
        '''
        Delete an if it exists
        :return:
        '''
        idEvent = input("Give event ID: ")
        event = self.__serviceEvents.deleteEvent(idEvent)
        if event == None:
            print("There are no events with the ID ", idEvent)
        else:
            print("Id   Date    Time      Description")
            print(event.getId(), event.getDate(), event.getTime(), event.getDescr())
            print("Was deleted!")


    def __modifyEvent(self):
        '''
        Modify an event if it exists
        :return:
        '''
        try:
            idEvent = input("Give event ID: ")
            event = self.__serviceEvents.searchEvent(idEvent)
            self.printEvent(idEvent, event)
            date = input("Give the new date of the event: ")
            time = input("Give the new time of the event: ")
            descr = input("Give the new description of the event: ")
            person = self.__serviceEvents.modifyEvent(idEvent, date, time, descr)
            self.printEvent(idEvent, event)
        except TypeError as ex:
            print(ex)


    def showUI(self):
        self.addEvents()
        self.addPeople()
        while True:
            cmd = input("Give command (Add, View, Search, Delete, Modify): ")
            if cmd.lower() == "add":
                self.__addCmd()
            if cmd.lower() == "view":
                self.__viewCmd()
            if cmd.lower() == 'search':
                self.__searchCmd()
            if cmd.lower() == 'modify':
                self.__modifyCmd()
            if cmd.lower() == 'delete':
                self.__deleteCmd()

    def __searchCmd(self):
        newcmd = input("Give command (Person, Event): ")
        if newcmd.lower() == 'person':
            self.__searchPerson()
        if newcmd.lower() == 'event':
            self.__searchEvent()

    def __viewCmd(self):
        newcmd = input("Give command (People, Events): ")
        if newcmd.lower() == "people":
            self.__showAllPerople()
        elif newcmd.lower() == "events":
            self.__showAllEvents()

    def __addCmd(self):
        newcmd = input("Give command (Person, Event): ")
        if newcmd.lower() == "person":
            self.__addPerson()
        elif newcmd.lower() == "event":
            self.__addEvent()

    def __modifyCmd(self):
        newCmd = input("Give command (Person, Event): ")
        if newCmd.lower() == 'person':
            self.__modifyPerson()
        elif newCmd.lower() == "event":
            self.__modifyEvent()
    def __deleteCmd(self):
        newCmd = input("Give command (Person, Event): ")
        if newCmd.lower() == 'person':
            self.__deletePerson()
        elif newCmd.lower() == 'event':
            self.__deleteEvent()

    def addPeople(self):
        self.__servicePeople.createPerson('1', 'Geo', 'Olanu')
        self.__servicePeople.createPerson('2', 'Gabi', 'Baia Mare')

    def addEvents(self):
        self.__serviceEvents.createEvent('1', '20/12/2012', '15:45', 'Wedding')
        self.__serviceEvents.createEvent('2', '12/11/2019', '12:40', 'Funeral')
