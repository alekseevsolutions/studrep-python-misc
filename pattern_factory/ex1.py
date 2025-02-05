from abc import ABC, abstractmethod


class Person(ABC):

    @abstractmethod
    def person_method(self):
        pass


class Student(Person):

    def __init__(self):
        self.name = "Basic Student Name"

    def person_method(self):
        print("I am a student")


class Teacher(Person):

    def __init__(self):
        self.name = "Basic Teacher Name"

    def person_method(self):
        print("I am a teacher")


s1 = Student()
s1.person_method()

t1 = Teacher()
t1.person_method()


class PersonFactory:

    @staticmethod
    def build_person(person_type):
        if person_type == "Student":
            return Student()
        if person_type == "Teacher":
            return Teacher()
        print("Invalid Type")
        return -1


if __name__ == "__main__":
    choice = input("What type of person you want to create?\n")
    person = PersonFactory.build_person(choice)
    person.person_method()