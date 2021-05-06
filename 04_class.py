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
        if key == 'birthday':
            return self.birthday
        elif key == 'age':
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


p = Employee('An', 'Ng')
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


# call by reference

class A:

    def __init__(self, a):
        self.a = a


a = [1, 2, 3]
a_obj = A(a)
a_obj.a[2] = 10
print(a)


# multiple inheritance

## 1. first override second
class A:
    def print_me(self):
        print("A")


class B:
    def print_me(self):
        print("B")


class C(A, B):

    def __init__(self):
        super().__init__()


c = C()
c.print_me()  # A


## even like this
class A:
    n_num = 0

    def __init__(self, n):
        self.n = n


class B:
    def __init__(self, n):
        self.n = n

    @property
    def n_num(self):
        return self.n


class C(A, B):

    def __init__(self, n):
        super().__init__(n)


c = C(10)
print(c.n_num)


## 2. super() means the first
class A:
    name = "a"

    def __init__(self, x):
        self.x = x

    @classmethod
    def from_x(cls, x=10):
        return cls(x)

    def show(self):
        print("show a")


class C:
    name = "c"

    def __init__(self, x):
        self.x = x

    @classmethod
    def from_x(cls, x=10):
        return cls(x * 100)

    def show(self):
        print("c is also mother")


class B(A, C):
    name = "b"

    @classmethod
    def from_x(cls, x=10, y=20):
        b = super().from_x(x)
        b.y = y
        return b

    def show(self):
        super().show()
        print("show b")


a = A.from_x(10)
print(a.name)
print(a.x)

b = B.from_x(15, 25)
print(b.name)  # b
print(b.x)  # 10
b.show()  # show a \n show b


## 3. the way to seperate
class Student:

    def __init__(self, student_id):
        self.student_id = student_id


class Dancer:

    def __init__(self, style):
        self.style = style


class DanceStudent(Student, Dancer):

    def __init__(self, student_id, style):
        Student.__init__(self, student_id)
        Dancer.__init__(self, style)
