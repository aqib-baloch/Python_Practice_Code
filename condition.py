# is_hot= False
# is_cold= False

# if is_hot:
#     print("Weather is hot Drink enough water")

# elif is_cold:
#     print("weather is cold wear warm clothes")
# else:
#     print("enjoy the weather ")


# Name = input("Enter your name ;")
# a=10
# b=5
# if a > b: print("a is greater than b")

# a = 2
# b = 330
# print("A") if a > b else print("B")

# a = 200
# b = 33
# c = 500
# if a > b or a > c:
#   print("At least one of the conditions is True")

# x = int(input("enter a number; "))

# if x > 10 and x<20:
#     print("between ten and twenty")
# elif x > 20 and x<50:
#     print(" between 20 and 50!")
# else:
#     print("number is greater than 50")

# temp = float(input("enter a temprature in celcius: "))

# if temp>30:
#     print("its very hot today")
# elif temp<10:
#     print("its cold today")
# else:
#     print("its neither hot nor cold")

# name = input("enetr your name please: ")

# if len(name)< 3:
#     print("please enter name having more than 3 characters, Thanks!")

# elif len(name)>50:
#     print("Please enter a name having less than 50 characters, Thanks!")

# else:
#     print("its pretty good name! "+ name)

weight = float(input("enter your weight: "))
unit = input("(L)bs or (k)gs: ")

if unit.upper()=="L":
    in_kilos = weight*0.454;
    print(f"your weight is {in_kilos} in kilos.")
else:
    in_pounds = weight/0.454;
    print(f"your weight is {in_pounds} in pounds")

