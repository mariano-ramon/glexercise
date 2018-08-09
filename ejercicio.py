class Person():

    instances = 0 

    def __init__(self, name, last_name, age):
        self.__name = name
        self.__last_name = last_name
        self.age = age
        self.__class__.instances += 1

    def __str__(self):
        return ("{} {}".format(self.__name, self.__last_name))


    @classmethod
    def omit_age(cls, name, last_name, *args):

        if cls != Person:
            raise Exception("You can only use this method when creating persons")

        person = cls.__new__(cls)
        person.__name = name
        person.__last_name = last_name
        Person.instances += 1

        return person


class Employee(Person):

    instances = 0 
    def __init__(self, name, last_name, age, salary):
        #parameters for super can be ommited in python3
        super(Employee, self).__init__(name, last_name, age)
        self.salary = salary


a = Person("Mariano", "Ramon", "36")
b = Person.omit_age("Manuel", "Rodriguez")
c = Employee("Juan", "Perez", "18", "15000")
d = Employee("Pedro", "Ramirez", "21", "30000")
e = Employee("Sofia", "Fernandez", "29", "30000")

#This throws an exception
#f = Employee.omit_age("Juana", "Molina", "30000")


print(a)
print(b)
print(c)
print(d.salary)
print(e)

print("Person instances: {}".format(Person.instances))
print("Employee instances: {}".format(Employee.instances))
