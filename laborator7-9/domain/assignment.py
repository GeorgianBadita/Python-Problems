'''
Created on Nov 20, 2017

@author: Geo
'''
class Assignment:
    '''
    Class which controls the enrollment functionality of the application 
    '''
    def __init__(self, pers, event):
        self.__id_ass = None
        self.__pers = pers
        self.__event = event
        
    def get_person(self):
        '''
        Function that gets the person from the assignment
        '''
        return self.__pers
    
    def get_event(self):
        '''
        Function that gets the event from the assignment
        '''
        return self.__event
    
    def get_id_ass(self):
        '''
        Function that gets the assignment id
        '''
        return self.__id_ass
    
    def set_id_ass(self, id_ass):
        '''
        Function that sets the id of the assignment
        '''
        self.__id_ass = id_ass
        
    def __eq__(self, ot):
        '''
        Function which defines when 2 assignments are equal
        '''
        if self.__pers == ot.__pers and self.__event == ot.__event:
            return True
        return False 
        
    
    