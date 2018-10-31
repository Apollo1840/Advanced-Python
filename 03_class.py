# -*- coding: utf-8 -*-

# special function
# this example is funny, I know
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
    
    def __add__(self, other):
        return People(self.birthday + other.birthday)
    
    def __getitem__(self, key):
        if key=='birthday':
            return self.birthday
        elif key=='age':
            return 'noknown'
        else:
            return None
