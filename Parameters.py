# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.
# The terms parameter and argument can be used for the same thing: information that are passed into a function.
# From a function's perspective:
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.

"""Functions define for doing something specific,
it is define by using keyword def, it has certain line of codes of doung a task
"""
# first_digit = int(input("enter a first number: "))
# second_digit = int(input("enter a second number: "))

# def print_sum( first_digit ,  second_digit = 4):
#     print(first_digit  + second_digit);

# print_sum(first_digit,second_digit);


# If the number of arguments is unknown, add a * before the parameter name:

# def my_function(*kids):
#   print("The youngest child is " + kids[0])

# my_function("Emil", "Tobias", "Linus")

# If the number of keyword arguments is unknown, add a double ** before the parameter name:

# def my_function(**kid):
#   print("His last name is " + kid["lname"])

# my_function(fname = "Tobias", lname = "Refsnes")

"""You can send any data types of argument 
to a function (string, number, list, dictionary etc.),
and it will be treated as the same data type inside the function."""

"""E.g. if you send a List as an argument, 
it will still be a List when it reaches the function:"""

def my_function(food):
  for x in food:
    print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)