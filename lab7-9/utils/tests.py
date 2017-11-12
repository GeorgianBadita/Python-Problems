from domain.entities import *
from domain.validators import *
from repository.memoryRepo import *
from services.eventService import EventService
from services.personService import PersonService
from utils.helper import dateValidation, hourValidation


def testCreatePerson():
    person = Person("1", "Geo", "Olanu")
    assert person.getName() == "Geo"
    assert person.getId() == "1"
    assert person.getAddress() == "Olanu"


def testCreateEvent():
    event = Event("2", "20/7/2012", "12:30", "Wedding")
    assert event.getId() == "2"
    assert event.getDate() == "20/7/2012"
    assert event.getTime() == "12:30"
    assert event.getDescr() == "Wedding"

def testPersonValidator():
    validator = PersonValidator()

    person = Person("", "", "")

    try:
        validator.validate(person)
        assert False
    except ValidatorException as ex:
        assert len(ex.getErrors()) == 3

    person = Person("1", "", "")
    try:
        validator.validate(person)
        assert False
    except ValidatorException as ex:
        assert len(ex.getErrors()) == 2

    person = Person("1", "Geo", "Olanu")
    try:
        validator.validate(person)
        assert True
    except ValidatorException as ex:
        assert False

def testEventValidator():

    validator = EventValidator()
    event = Event("", "", "", "")

    try:
        validator.validate(event)
        assert False
    except ValidatorException as ex:
        assert len(ex.getErrors()) == 6

    event = Event("IdEv", "", "", "")

    try:
        validator.validate(event)
        assert False
    except ValidatorException as ex:
        assert len(ex.getErrors()) == 5

    event = Event("1", "20/07/2016", "12:30", "Wedding")

    try:
        validator.validate(event)
        assert True
    except ValidatorException as ex:
        assert False


def testStorePeople():
    person = Person("1", "Ion", "Arad")
    rep = MemoryRepository()
    assert rep.size() == 0
    rep.store(person)
    assert rep.size() == 1
    person2 = Person("2", "Andrei", "Constanta")
    rep.store(person2)
    assert rep.size() == 2
    person3 = Person("2", "Andrada", "Ramnicu Valcea")
    try:
        rep.store(person3)
        assert False
    except RepositoryException:
        pass


def testStoreEvents():
    event = Event("1", "20/07/2015", "12:30", "Wedding")
    rep = MemoryRepository()
    rep.store(event)
    assert rep.size() == 1
    event1 = Event("2", "15/06/2018", "08:30", "Funeral")
    rep.store(event1)
    assert rep.size() == 2
    event2 = Event("2", "20/09/2020", "17:55", "Birthday Party")
    try:
        rep.store(event2)
        assert False
    except RepositoryException:
        pass

def testCreatePersonSrv():
    rep = MemoryRepository()
    val = PersonValidator()
    perSrv = PersonService(rep, val)
    person = perSrv.createPerson("1", "Adi", "Calimanesti")
    assert person.getId() == "1"
    assert person.getName() == "Adi"
    allPeople = perSrv.getAllPeople()
    assert len(allPeople) == 1
    assert allPeople[0] == person

    try:
        person = perSrv.createPerson("1", "Anghel", "Baia-Mare")
        assert False
    except RepositoryException:
        assert True

def testCreateEventSrv():
    rep = MemoryRepository()
    val = EventValidator()
    eventSrv = EventService(rep, val)
    event = eventSrv.createEvent("1", "20/07/2012", "13:20", "Wedding")
    assert event.getId() == "1"
    assert event.getDate() == "20/07/2012"
    assert event.getTime() == "13:20"
    allEvnts = eventSrv.getAllEvents()
    assert len(allEvnts) == 1
    assert allEvnts[0] == event

    try:
        event = eventSrv.createEvent("1", "12/06/2018", "19:00", "Funeral")
        assert False
    except RepositoryException:
        assert True

def testDateValidator():
    errors = dateValidation("10/02/2017")
    #print(errors)
    assert len(errors) == 0
    errors = dateValidation("20/7/2012")
    assert len(errors) == 1
    errors = dateValidation("1s/05/2017")
    assert len(errors) == 1


def testHourValidator():
    errors = hourValidation("10:50")
    assert len(errors) == 0
    errors = hourValidation("25:61")
    assert len(errors) == 2
    errors = hourValidation("25:01")
    assert len(errors) == 1
    errors = hourValidation("14:55")
    assert len(errors) == 0

testHourValidator()
testDateValidator()
testCreateEventSrv()
testCreatePersonSrv()
testStoreEvents()
testStorePeople()
testEventValidator()
testPersonValidator()
testCreatePerson()
testCreateEvent()