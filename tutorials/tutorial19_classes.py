"""
Classes in Python are pretty much the same as in Java
To define a class:
    class class_name (superclasses):      ->> This is how to extend superclasses. In Python, a subclass can extend
                                              multiple superclasses
There are 2 types of variables in Python:
    1. class variable: defined within the class scope, not inside constructor. This is the same as static variable in Java
    2. instance variable: defined inside constructor
"""


class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):    # This is a Python constructor
        self.name = name                # This is how we declare instance vars
        self.salary = salary            # "self" is the same as "this" in Java
        Employee.empCount += 1          # How to access

    def display_count(self):
        print("The total employees %d" % Employee.empCount)

    def display_employee(self):
        print("Name:", self.name, " Salary:", self.salary)


class Point:
    'This class demos how to destroy an object with destructor __del__'
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__    # __name__ is to get class namw
        print(class_name, "destroyed")


class Vector:
    'This class demos how to overload operators'
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return "Vector (%d, %d)" % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


class Counter:
    'This class demos how to hide data by using the sign __ before the data filed when declaring it'
    __secrete_count = 0

    def count(self):
        self.__secrete_count += 1
        print(self.__secrete_count)


if __name__ == '__main__':
    # Demos class Employee
    emp1 = Employee("Van", 100)  # This is how we create an instance obj
    emp2 = Employee("Long", 200)
    # Accessing attributes
    emp1.display_employee()
    emp2.display_employee()
    emp2.display_count()

    # Demos class Point
    pt1 = Point()
    pt2 = pt1
    pt3 = pt1
    print(id(pt1), id(pt2), id(pt3))    # 4456240704 4456240704 4456240704
    del pt1                             # Point destroyed
    del pt2
    del pt3

    # Demos class Vector
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    print(v1+v2)    # Vector (4, 6)

    # Demos class Counter
    counter = Counter()
    counter.count()
    counter.count()
    # print(counter.__secrete_count)    ->> AttributeError: 'Counter' object has no attribute '__secrete_count'








