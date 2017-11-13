from domain.validators import PersonValidator, EventValidator
from repository.memoryRepo import MemoryRepository
from services.eventService import EventService
from services.personService import PersonService
from ui.consoleUI import Console
from utils.tests import testCreateEventSrv, testCreatePersonSrv,\
    testStoreEvents, testStorePeople, testEventValidator, testPersonValidator, testCreatePerson, testCreateEvent



valPers = PersonValidator()
valEvent = EventValidator()

repPers = MemoryRepository(valPers)
repEvent = MemoryRepository(valEvent)

ctrPers = PersonService(repPers)
ctrEvent = EventService(repEvent)
ui = Console(ctrPers, ctrEvent)

ui.showUI()
