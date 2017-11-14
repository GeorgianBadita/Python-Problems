from domain.entities import Event
from domain.validators import ValidatorException


class EventService:
    def __init__(self, repo):
        '''
        Initialise service
        :param repo: -repository - object to store events
        :param val: - validator - object to validate events
        '''
        self.__rep = repo

    def createEvent(self, idEvent, date, time, descr):
        '''
        store an event
        :param idEvent: string
        :param date: string
        :param time: string
        :param descr: string
        :return: the event
        :post: the event added to the repository
        :raise: RepositoryException - if event already exists
        :raise: ValidationException - if event fields are invalid
        '''
        #create event object
        event = Event(idEvent, date, time, descr)
        #store event into using repository
        self.__rep.store(event)
        return event

    def getAllEvents(self):
        '''

        :return: list of all events in the system
        '''
        return self.__rep.getAll()

    def searchEvent(self, idEvent):
        return self.__rep.findElem(idEvent)

    def deleteEvent(self, idevent):
        allEvents = self.getAllEvents()
        for event in allEvents:
            if idevent == event.getId():
                eventToReturn = event
                self.__rep.deleteElem(event)
                return eventToReturn
        return None

    def modifyEvent(self, idEvent, date, time, descr):
        '''
        Modifies an event if it exists
        :param idPers:
        :return: returns the new Event
        '''
        try:
            newEvent = Event(idEvent, date, time, descr)
            self.__rep.updateElem(newEvent)
            return newEvent
        except ValidatorException as ex:
            print(ex.args)

    #TODO move all to repo
    def enrollPersToEvent(self, person, event):
        '''
        Function that enrolls person to event
        :param idPers:
        :param idEvent:
        :return:
        '''
        event.setPersEnrolled(person)
        self.__rep.enroll(event)

    def retEventAtDate(self, date):
        '''
        gives the events in a date
        :param date:
        :return: the events at a date
        '''
        allEvents = self.getAllEvents()
        eventsInDate = []
        for event in allEvents:
            if event.getDate() == date:
                eventsInDate.append(event)
        if not len(eventsInDate):
            return None
        return eventsInDate