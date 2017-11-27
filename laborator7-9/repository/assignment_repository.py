'''
Created on Nov 20, 2017

@author: Geo
'''

class AssignRepository:
    '''
    Class to manage assignment data
    '''
    def __init__(self):
        self.__list = {}
        
    def store_assig(self, assig):
        '''
        Store __list
        assig is the element of the class Assignment
        :param: assig
        :return: nothing
        :post: assignment added to the repository
        '''
        id_assig = len(self.__list) + 1
        assig.set_id_ass(id_assig)
        if self.search_assign(assig) is None:
            self.__list[assig.get_id_ass()] = assig
            return assig
        else:
            return None
        
    def get_all_assign(self):
        '''
        Function that gets all the assignments from the list
        '''
        return list(self.__list.values())
    
    
    def get_pers_enrolled(self, person):
        '''
        Function that gets all events in which a person is enrolled
        :return: a list of events in which the person is enrolled if 
        there are any, else returns None
        '''
        list_events = []
        for assignment in self.__list.values():
            if person.get_id_pers() == assignment.get_person().get_id_pers():
                list_events.append(assignment.get_event())
        
        if len(list_events) > 0:
            return list_events
        return None
    
    def sort_pers_enrolled(self, eventsList):
        '''
        Function that sorts all the events of a person by description and date
        :return: a new list representing the first list sorted
        '''
        if eventsList is None:
            return None
        return sorted(eventsList)
        
        
    
    
    def search_assign(self, assignment):
        '''
        Function that searches for a given assignment
        '''
        for assig in self.__list.values():
            if assignment == assig:
                return assig
        
        return None
    
  
            
            