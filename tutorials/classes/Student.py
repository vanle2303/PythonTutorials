from tutorials.classes.Person import Person


class Student(Person):
    """
    A subclass Student extends superclass Person
    This class also introduces the way to declare private variable
        1. strongly private:    __var-name
        2. weakly private:      _var-name
    """
    student_count = 0   # class var

    def __init__(self, name, age, school, gpa=0, ssn=None):
        Person.__init__(self, name, age)    # To call the constructor of the superclass, use the superclass name

        # Or we can use `super` like Java to call superclass fields"
        # Since super() in Python already returns an object, we don't need to pass "self" to it like the above
        # But if we have multiple parens, we need to use class-name and call the constructor explicitly
        # bc now using super() is so ambiguous
        super().__init__(name, age)

        self.school = school    # subclass instance var
        self._gpa = gpa         # weakly private
        self.__ssn = ssn        # strongly private

        Student.student_count += 1

    def get_school(self):
        return self.school

    def get_info(self): # override superclass method
        print("Name:", self.name, " Age:", self.age, " School:", self.school,
              " Total students:", Student.student_count)

    def __get_ssn(self):    # strongly private function
        return self.__ssn

    def _get_gpa(self):     # weakly private function
        return self._gpa


