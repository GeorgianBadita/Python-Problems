'''
Created on Nov 20, 2017

@author: Geo
'''
from utils.tests import test_create_event_service, test_create_person_service, test_event_repo, test_person_repo, test_event_validator, test_person_validator, test_date_validation, test_hour_validation, test_event_entity, test_person_entity
from domain.validator import PersonValidator, EventValidator
from repository.event_repository import EventRepository
from repository.person_repository import PersonRepository
from services.person_service import PersonService
from services.event_service import EventService
from ui.console_ui import ConsoleUI
from repository.assignment_repository import AssignRepository
from services.assignment_service import AssignmentService

person_val = PersonValidator()
event_val = EventValidator()
person_rep = PersonRepository(person_val)
event_rep = EventRepository(event_val)
assig_rep = AssignRepository()

ctr_person = PersonService(person_rep)
ctr_event = EventService(event_rep)
ctr_assign = AssignmentService(assig_rep)

user_interface = ConsoleUI(ctr_event, ctr_person, ctr_assign)
user_interface.show_ui()

