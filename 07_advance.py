# -*- coding: utf-8 -*-


# exchage variable
def swap():
    a = 5
    b = 3
    a, b = b, a



# ----------------------------------
# location and value
a = 'hello world'
b = 'hello world'
print(a==b)
print(a is b)

# trial string will be intern, intern variable sign to same id.
a = 'hello'
b = 'hello'
print(a==b)
print(a is b)
print(id(a)==id(b))

a = 3
b = 3
print(a==b)
print(a is b)
print(id(a)==id(b))


# use is None.
class BaiBianGuai():
    def __eq__(self, other):
        return True

bbg = BaiBianGuai()
print(bbg == None)
print(bbg is None)



# ----------------------------------
# changable and unchangeble

# append is faster than += , because append is unchangable action
a = [1,2,3]
print(id(a))

a.append(4)
print(id(a))

a+=list(range(100))
print(id(a))

b=a
b[0]=10
print(a)

b=a[:]  # simplified copy
b[0]=100
print(a)




# very interesting facts:
class Group():
    def __init__(self, members=[]):
        self.members=members
    
    def add_member(self, member):
        self.members.append(member)

g1 = Group()
g1.add_member('li')
g1.add_member('wang')

g2 = Group()
g2.add_member('zhang')
g2.add_member('hu')

print(g1.members)
print(g2.members)
# they sames to share the group list
# the reason is default members, it takes cache
# solution:

class Group():
    def __init__(self, members=None):
        self.members=members
        if members is None:
            self.members = []
    
    def add_member(self, member):
        self.members.append(member)

g1 = Group()
g1.add_member('li')
g1.add_member('wang')

g2 = Group()
g2.add_member('zhang')
g2.add_member('hu')

print(g1.members)
print(g2.members)




# ----------------------------------
# new method

class Person():
    
    def __new__(cls, *args, **kwargs):
        print('in new')
        instance = object.__new__(cls, *args, **kwargs)
        return instance
    
    def __init__(self):
        print('in init')

p = Person()

# singleton
class Singleton():
    _instance=None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance
    
s1 = Singleton()
s2 = Singleton()
s1 is s2

#只要程序不结束, Singleton永远指向同一个object

# factory mode:
class Fruit():
    def __init__():
        pass

class Apple():
    def name(self):
        print('apple')

class Banana():
    def name(self):
        print('banana')
    
class FruitFactory():
    fruits = {'apple':Apple, 'banana':Banana}
    
    def __new__(cls, name):
        if name in cls.fruits.keys():
            return cls.fruits[name]()
        else:
            return Fruit()

fruit1 = FruitFactory('apple')
fruit2 = FruitFactory('banana')
fruit1.name()
fruit2.name()



# ----------------------------------
# context
# class context
class ContextManager():
    def __enter__(self):
        print('in enter')
    
    def __exit__(self, exception_type, exception_value, traceback):
        print('in exit')
        if exception_type is None:
            print('no error')
        else:
            print('except with error - {}'.format(exception_value))
            return False
    
with ContextManager():
    print('working under the context')


# function context
    
    
    
    
    
    
    
    
    
    