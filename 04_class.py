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

hasattr(People, '__del__')
callable(People.__del__)



# -----------------------------------------------
# inhert
class Superman(People):
    def __init__(self, birthday, superpower):
        super().__init__(birthday)
        print('ha, superman for {}'.format(superpower))

superman = Superman('2019-2-10', 'speed')

print(isinstance(superman, Superman))
print(isinstance(superman, People))
print(issubclass(Superman, People))


# -----------------------------------------------
# property(getter), setter, deleter
class Employee():
    
    def __init__(self, firstname, lastname):
        self.fname = firstname
        self.lname = lastname
    
    @property
    def fullname(self):
        print("calculating fullname")
        return ' '.join([self.fname, self.lname])
        
    @fullname.setter
    def fullname(self, fullname):
        self.fname, self.lname = fullname.split()
    
    @fullname.deleter
    def fullname(self):
        self.fname = None
        self.lname = None
        print('Persons name missed')

p = Employee('An','Ng')
print(p.fullname)
print(p.fullname)
p.fullname = 'Andrew Ng'
print(p.fullname)

print(p.fname)
del p.fullname
print(p.lname)



# -----------------------------------------
# class's connection with outside (better do not use this tech)
class InClass():
    stone = 10
    
    def __init__(self, stone):
        self.stone = stone
    
    def show_stone(self):
        stone = 5  # the stone outside will not be changed. use global variable to realise it.
        print('show it: ', stone)
        return self.stone
    
    def show_stone2(self):
        print('show it: ', stone)
        return self.stone
        
stone = InClass(10)
print(stone)
print(stone.stone)
print(stone.show_stone())
print(stone.show_stone2())



  