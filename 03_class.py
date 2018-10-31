# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 22:21:21 2018

@author: zouco
"""



# --------------------------------------------------------------------------
# class
# class can take variable out of definition

# special function
class People():
    population = 0
    
    def __init__(self, birthday):
        self.birthday = birthday
        People.population += 1
    
    def __del__(self):
        People.population -= 1
    
    def __str__(self):
        return 'a human born in {}'.format(self.birthday)
    
    def __len__(self):
        return 'not konw'
    
    def __getitem__(self, key):
        if key=='birthday':
            return self.birthday
        else:
            return None
