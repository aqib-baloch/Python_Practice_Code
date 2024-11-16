# Inheritance allows us to define a class 
# that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, 
# also called derived class.
# Example:
# class Animal:
#     def walk(self):
#         print("Walk:")

# class Dog(Animal):
#     def bark(self):
#         print("dog is barking:")

# class Cat(Animal):
#     def eat(self):
#         print("cat is eating:")

# dog1 = Dog()
# dog1.bark();

# cat1 = Cat()
# cat1.eat();

# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)

# class Student(Person):
#     def __init__(self, fname, lname):
#         super().__init__(fname, lname)

# x = Student("Mike", "Olsen")
# x.printname();


# example of adding method

class Person:
    firstname = input("Enter your first name: ")
    lastname = input("Enter your last name: ")
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student()
x.welcome();
x.printname();


        