from domain.validators import PersonValidator, EventValidator
from repository.memoryRepo import MemoryRepository
from services.eventService import EventService
from services.personService import PersonService
from ui.consoleUI import Console
from utils.tests import testCreateEventSrv, testCreatePersonSrv,\
    testStoreEvents, testStorePeople, testEventValidator, testPersonValidator, testCreatePerson, testCreateEvent

repPers = MemoryRepository()
repEvent = MemoryRepository()

valPers = PersonValidator()
valEvent = EventValidator()
ctrPers = PersonService(repPers, valPers)
ctrEvent = EventService(repEvent, valEvent)
ui = Console(ctrPers, ctrEvent)

ui.showUI()
'''
Questions about repository and CONSOLE UI
'''