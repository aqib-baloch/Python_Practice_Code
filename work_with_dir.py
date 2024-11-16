from pathlib import Path
# To check the existence of file, firslt create the object of class and then
# by using . operator with object, pass the respective keyword


# path = Path("Ecommerce")

# print(path.exists())

# to create folder
# path = Path("Emails")
# print(path.mkdir())

# to remove folder
# path = Path("Emails")
# print(path.rmdir())

path = Path();
for i in path.glob('*'):
    print(i) 

