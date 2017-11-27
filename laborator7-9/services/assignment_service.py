'''
Created on Nov 20, 2017

@author: Geo
'''
from domain.assignment import Assignment

class AssignmentService:
    '''
    Class for assignment operations
    '''
    def __init__(self, assig_repository):
        self.__rep = assig_repository
        
    def create_assig(self, person, event):
        '''
        store an event
        :param: person - Person 
        :param: event - Event
        :post: the assignment will be added to the list
        :return: the new assignment added
        '''
        #create new_assignment
        new_assig = Assignment(person, event)
        #add the assignment into using repository
        return self.__rep.store_assig(new_assig)
        
    def get_all_assign_service(self):
        '''
        Function that gets all assignments from repository
        :return: a list with all assignments
        '''
        return self.__rep.get_all_assign()
    
    def get_pers_enrolled_serv(self, person):
        '''
        Function that gets all events in which a person is enrolled
        :return: a list of events in which the person is enrolled if 
        there are any, else returns None
        '''
        return self.__rep.get_pers_enrolled(person)
    
    def sort_pers_enrolled_serv(self, eventsList):
        '''
        Function that sorts all the events of a person by description and date
        :return: a new list representing the first list sorted
        '''
        return self.__rep.sort_pers_enrolled(eventsList)
    
    
    def search_assign_serv(self, assignment):
        '''
        Function which searches for an assignment in the list
        '''
        return self.__rep.search_assign(assignment)
    
    
    def print_most_participants(self):
        '''
        Function that prints the most participants to an event
        '''
        dict_pers = {}
        
        list_pers = self.get_all_assign_service()
        
        for assig in list_pers:
            if assig.get_person() in dict_pers:
                dict_pers[assig.get_person()] += 1
            else:
                dict_pers[assig.get_person()] = 1
            
        max_pers = 0
        
        for person in dict_pers.values():
            if person > max_pers:
                max_pers = person
                
        list_pers = []
        
        for person in dict_pers:
            if dict_pers[person] == max_pers:
                list_pers.append(person)
                
        return list_pers
    
    def first_20_percent(self):
        '''
        Function that returns a list representing the first 20% events with most participants
        '''
        list_events = self.get_all_assign_service()
        dict_events = {}   
            
        for assig in list_events:
            if assig.get_event() in dict_events:
                dict_events[assig.get_event()] += 1
            else:
                dict_events[assig.get_event()] = 1
            
        list_events = []
        
        for event in dict_events:
            list_events.append([event, str(dict_events[event])])
        
        list_events = sorted(list_events, key = lambda x: x[1], reverse = True)
        
        return list_events
            
        
            
        
        
    