class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if 0 <= age <= 120:
            self.__age = age


person = Person("Alice", 30)
print(person.get_name())
person.set_age(15)
print(person.get_age())
