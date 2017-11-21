'''
Created on Nov 20, 2017

@author: Geo
'''
from domain.person import Person
from domain.event import Event
from domain.validator import PersonValidator, EventValidator, ValidatorException
from repository.person_repository import PersonRepository, PersonRepositoryException
from repository.event_repository import EventRepository, EventRepositoryException
from services.person_service import PersonService
from services.event_service import EventService
from utils.helper import hour_validation, date_validation



def test_person_entity():
    '''
    Function for testing the person class
    '''
    person = Person('1', 'Geo', 'Olanu')
    assert person.get_id_pers() == '1'
    assert person.get_name() == 'Geo'
    assert person.get_adr() == 'Olanu'
    
    
def test_event_entity():
    '''
    Function for testing the event class
    '''
    event = Event('1', '20/12/2012', '10:59', 'Wedding')
    assert event.get_id_event() == '1'
    assert event.get_date() == '20/12/2012'
    assert event.get_time() == '10:59'
    assert event.get_descr() == 'Wedding'

def test_hour_validation():
    '''
    Function for testing the hour validation function
    '''
    errors = hour_validation("25:60")
    assert len(errors) == 2
    errors = hour_validation("10:61")
    assert len(errors) == 1
    errors = hour_validation("9:59")
    assert len(errors) == 1
    errors = hour_validation("09:59")
    assert len(errors) == 0
    errors = hour_validation("akfla")
    assert errors == ['The hour format is incorrect!']

def test_date_validation():
    '''
    Function for testing the date validation function
    '''
    errors = date_validation('33/15/2020')
    assert len(errors) == 2
    errors = date_validation('13/13/20100')
    assert len(errors) == 2
    errors = date_validation('12/12/2012')
    assert len(errors) == 0
    errors = date_validation('12/13/2012')
    assert len(errors) == 1

def test_person_validator():
    '''
    Function to test the person validation
    '''
    person = Person("", "", "")
    validator = PersonValidator()
    try:
        validator.validate(person)
        assert False
    except ValidatorException as ex:
        assert len(ex.get_errors()) == 3
    
    person = Person("1", "", "")
    try:
        validator.validate(person)
        assert False
    except ValidatorException as ex:
        assert len(ex.get_errors()) == 2
    
    person = Person("1", "Gabi", "")
    try:
        validator.validate(person)
        assert False
    except ValidatorException as ex:
        assert ex.get_errors() == ["The address can't be empty!"] 
    
    person = Person("1", "Gabi", "Baia-Mare")
    try:
        validator.validate(person)
        assert True
    except ValidatorException as ex:
        assert False
        
        
def test_event_validator():
    '''
    Function to test the event validation
    '''
    event = Event("", "", "", "")
    validator = EventValidator()
    try:
        validator.validate(event)
        assert False
    except ValidatorException as ex:
        assert len(ex.get_errors()) == 6
    
    event = Event("1", "", "", "")
    try:
        validator.validate(event)
        assert False
    except ValidatorException as ex:
        assert len(ex.get_errors()) == 5
    
    event = Event("1", "32/12/2051", "", "Funeral")
    try:
        validator.validate(event)
        assert False
    except ValidatorException as ex:
        assert ex.get_errors() == ['The day must be between 1 and 31', 'The year must be between 2010 and 2050', 'The hour format is incorrect!', "The time can't be empty!"]
    
    person = Event("1", "20/12/2012", "20:59", "Birthday party")
    try:
        validator.validate(person)
        assert True
    except ValidatorException as ex:
        assert False


def test_person_repo():
    '''
    Function to test the person repository store
    '''
    person = Person('1', "Ion", "Arad")
    repo = PersonRepository(PersonValidator)
    assert repo.size() == 0
    repo.store_person(person)
    assert repo.size() == 1
    person = Person('2', "Andrei", "Valcea")
    repo.store_person(person)
    assert repo.size() == 2
    repo.delete_person(person.get_id_pers())
    assert repo.size() == 1
    person = Person("1", "Alexandru", "Sibiu")
    try:
        repo.store_person(person)
        assert False
    except PersonRepositoryException:
        pass

def test_event_repo():
    '''
    Function to test the event repository store
    '''
    event = Event('1', "20/06/2010", "10:56", "Funeral")
    repo = EventRepository(EventValidator)
    assert repo.size() == 0
    repo.store_event(event)
    assert repo.size() == 1
    event = Event('2', "15/06/2011", "12:03", "Wedding")
    repo.store_event(event)
    assert repo.size() == 2
    repo.delete_event(event.get_id_event())
    assert repo.size() == 1
    event = Event("1", "12/12/2012", "11:07", "Birthday Party")
    try:
        repo.store_event(event)
        assert False
    except EventRepositoryException:
        pass



def test_create_person_service():
    '''
    Function to test the person service create method
    '''
    val = PersonValidator()
    repo = PersonRepository(val)
    person_service = PersonService(repo)
    person = person_service.create_person("1", "Badita", "Valcea")
    assert person.get_id_pers() == "1"
    assert person.get_adr() == "Valcea"
    assert person.get_name() == "Badita"
    allPeople = person_service.get_all_people_service()
    assert len(allPeople) == 1
    
    try:
        person = person_service.create_person("1", "Adi", "Baia Mare")
        assert False
    except PersonRepositoryException:
        assert True
    
    try:
        person = person_service.create_person("", "", "")
        assert False
    except ValidatorException:
        assert True

def test_create_event_service():
    '''
    Function to test the event service create method
    '''
    val = EventValidator()
    repo = EventRepository(val)
    event_service = EventService(repo)
    event = event_service.create_event("1", "20/12/2013", "10:59", "Wedding")
    assert event.get_id_event() == "1"
    assert event.get_date() == "20/12/2013"
    assert event.get_time() == "10:59"
    assert event.get_descr() == "Wedding"
    allEvents = event_service.get_all_events_service()
    assert len(allEvents) == 1
    
    try:
        event = event_service.create_event("1", "20/11/2014", "20:59", "Funeral")
        assert False
    except EventRepositoryException:
        assert True
    
    try:
        event = event_service.create_event("", "", "25:67", "")
        assert False
    except ValidatorException:
        assert True


test_create_event_service()
test_create_person_service()
test_event_repo()
test_person_repo()
test_event_validator()
test_person_validator()
test_date_validation()
test_hour_validation()
test_event_entity()
test_person_entity()


