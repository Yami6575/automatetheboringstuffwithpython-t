import re
data=input("enter password") 
def passworddetector(data):
    length=re.compile(r'.{8,}')
    lowercase=re.compile(r'[a-z]+')
    uppercase=re.compile(r'[A-Z]+')
    number=re.compile(r'[0-9]+')
    if length.search(data)==None:
        print("add more characters")
        return False
    elif lowercase.search(data)==None:
        print("add lower case characters")
        return False
    elif uppercase.search(data)==None:
        print("add upper casee characters")
        return False
    elif number.search(data)==None:
        print("add numbers")
        return False
    else :
        print("your password is perfect")
passworddetector(data)
