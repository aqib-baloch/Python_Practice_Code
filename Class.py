# Python Classes/Objects
# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.
# Create a Class
# To create a class, use the keyword class:
# Example
# Create a class named MyClass, with a property named x:

# class MyClass:
#   x = 5
# # Create an object named p1, and print the value of x:
# p1 = MyClass();
# print(p1.x);

"""The self parameter is a reference to the current instance of the class, 
and is used to access variables that belongs to the class.

It does not have to be named self , 
you can call it whatever you like, 
but it has to be the first parameter of any function in the class:"""

class Name:
    def __init__(self, name , contact_no):
        self.name= name;
        self.contact_no= contact_no;
    def info(self):
        print(f"your name is {self.name} ");
        print(f"your contact no is {self.contact_no}")
    
    
person_detail = Name("Aqib Hussain", "03370683966");

# You can modify properties on objects like this:
person_detail.name= "Saqib"
person_detail.info();
# Delete the age property from the p1 object:

# del person_detail.name
# print(person_detail.name)



