class Person:
    # This is a superclass
    # person_count is a class variable, which is like a static var in Java
    person_count = 0

    # This is a class constructor. In Python, there is only one constructor defined in each class
    def __init__(self, name, age):
        self.name = name    # This is how we declare instance variable in Python
        self.age = age      # instance var
        Person.person_count += 1    # class var

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_info(self):
        print("Name:", self.name, " Age:", self.age, " Total number of people:", Person.person_count)






