# print("Sum of the Number\n")
# Str = "1234"
# Sum = int(Str[0]) + int(Str[1]) + int(Str[2]) + int(Str[3])

# print(f"Sum of the Str is {Sum}" )


# Str = input("enter the number")
# Sum = 0;
# i=0
# while i < len(Str):
#     Sum = (Sum + int(Str[i]))
#     i+=1
# print(f"Sum of the Str is {Sum}" )

# Count the character occurence in String

# String= input("Enter the String: ");
# resultant_Ans = "";
# i= 0;
# while i < len(String):
#     if String[i] not in resultant_Ans:
#         resultant_Ans+=String[i]
#         print(f"{String[i]} :  {String.count(String[i])}")
#     i+=1;

    
String= input("Enter the String: ");
resultant_Ans = "";
i= 0;
while i < len(String):
    # if String[i] not in resultant_Ans:
    resultant_Ans+=String[i]
    print(f"{String[i]} :  {String.count(String[i])}")
    i+=1;

