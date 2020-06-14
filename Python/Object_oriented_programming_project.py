from abc import ABC, abstractmethod
# multi-level inheritance: Manager(Employee) and Employee(Person)
class Person():
    def __init__(self, name, age):
        # the attributes
        self._name = name
        self._age = age

    # redefine str(obj); it's called when we use print(obj)
    def __str__(self):
        return self._name + ' ' + str(self._age)

# abstract class
class Employee(Person, ABC):
    def __init__(self, name, age, salary):
        # define the attributes of the mother class
        super().__init__(name, age)
        # add the new attribute
        self._salary = salary

    @abstractmethod
    def show_salary(self):
        pass


class Manager(Employee):
    # Redefining the abstract method
    def show_salary(self):
        print("Salary from Manager is = ", self._salary)

# Here you can test any example you want !
p = Person("younes", 20)
print(p)
