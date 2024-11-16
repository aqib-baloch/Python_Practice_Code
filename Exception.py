"""In this we wil learn how to handle the exception,
let's see!
"""

# Age = int(input("enetr your age: "))

# print(f"your age is {Age}");

# but if user will enter the age in words, then it will generate errror(Exception), 
#  to handle it we use exception handling, in which try catch(except) block are used

try:
    Age = int(input("enetr your age: "));
    Income = 1000;
    Insurence = Income / Age;
    print(f"your age is {Age}");
    print(f"Your Insurence amount is {Insurence} ")
except ValueError:
    print("You entered invalid argument!");
except ZeroDivisionError:
    print("Age cannot be zero")
    