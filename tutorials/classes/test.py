from tutorials.classes.Person import Person
from tutorials.classes.Student import Student


if __name__ == '__main__':
    p = Person("Van", 19)
    print(p.name, p.age)    # Van 19
    p.get_info()    # Name: Van  Age: 19  Total number of people: 1

    s = Student("Long", 12, "Thai Binh")
    s.get_info()    # Name: Long  Age: 12  School: Thai Binh  Total students: 1
    p.get_info()    # Name: Van  Age: 19  Total number of people: 3

    # print(s.__ssn) ->> CANNOT access instance var __ssn since it is a strongly private var

    print(isinstance(s, Student))   # True
    print(isinstance(s, Person))    # True ->> since Student is the subclass of Person
    print(isinstance(p, Student))   # False
    print(issubclass(Student, Person))  # True
    print(issubclass(Person, Student))  # False
