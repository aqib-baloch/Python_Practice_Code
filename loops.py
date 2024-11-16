# Shape = int(input("enter a digit; "))
# i=1;
# while i<=Shape:
#     print('*' * i)
#     i=i+1
# print("this is your desire rectanglar shape")


# Game guess a number
print("play a mind game and guess a one number.\n")

print("Guess the number between 0 and 10\n")

secret_number = 10;
guess_count = 0;
guess_limit = 3;

while guess_count < guess_limit:
    guess = int(input("Guess the number: "))
    guess_count = guess_count+1;
    if guess == secret_number:
        print("congrats, you win!")
        break;
    elif guess_count>1 and guess_count<3:
        print("That is your last chance, guess carefully.")

else:
    print("Sorry you are failed, Try Again!")



# count=0
# while count<=3:
#     name =input("enter your name ").upper()
#     print(name)
#     count+=1;

# numbers = [1,1,1,1,5];
# for x_count in numbers:
#     print('x' * x_count);

# # x = int(input("enter the number; "))
# # count=0
# # while count<=x:
# #     print('*' * count);
# #     count+=1;

# i = 1
# while i < 6:
#     print(i)
#     if i == 3:
#       break
#     i += 1
   

# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)

# i = 1
# while i < 6:
#   print(i)
#   i += 1
# else:
#   print("i is no longer less than 6")

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
# # In this continue statement, 
# # condition will check and 
# # if the banana found 
# # then it will not print the banana 
# # but print the nxt items
#   if x == "banana":
#     continue
#   print(x) 


# for x in range(2, 30,5):
#   print(x)

# for x in range(6):
#     print(x)
# else:
#   print("Finally finished!")

# for x in range(6):
#   if x == 3: break
#   print(x)
# else:
#   print("Finally finished!")

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]
# for x in adj:
#   for y in fruits:
#     print(x, y)

# Program to check if a number is prime or not

# num = 29
# To take input from the user
# num = int(input("Enter a number: "))
# # define a flag variable
# flag = False
# # prime numbers are greater than 1
# if num > 1:
#     # check for factors
#     for i in range(2, num):
#         if (num % i) == 0:
#             # if factor is found, set flag to True
#             flag = True
#             # break out of loop
#             break
# # check if flag is True
# if flag:
#     print(num, "is not a prime number")
# else:
#     print(num, "is a prime number")


# Python program to display all the prime numbers within an interval

# lower = int(input("enter lower number: "))
# upper = int(input("enter upper number:  "))

# print("Prime numbers between", lower, "and", upper, "are:")

# for num in range(lower, upper+1):
#    # all prime numbers are greater than 1
#    if num > 1:
#        for i in range(2, num):
#            if (num % i) == 0:
#                break
#        else:
#            print(num)
    


# X = int(input("enter the number and get all the sum of number which are included in this: "))
# Sum=0;
# for i in range(X+1):
#     Sum= Sum+i;
# print(Sum)
 
# Code with python:


# num = int(input("enter a number tp get summ of all number in it:  "))

# sum = 0;
# i = 1;
# while i<=num:
#     # if num%i!= 0:
#     sum= sum+i;
#     i+=1;
# print(sum);
