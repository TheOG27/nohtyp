#math built-in function
from math import *

x = int(input("enter value :"))
y = int(input("enter value :"))
print("ceil() function :",ceil(x))
print("pow() function :",pow(x,y))
print("sqrt() function :",sqrt(x))
print("sin() function :",sin(x))
print("cos() function :",cos(x))
print("tan() function :",tan(x))
print("factorial() function :",factorial(x))
print("gcd() function :",gcd(x,y))

#random module
import random
num=range(5,50)
choose=random.choice(num)
print(choose)

#STRING BUILt in function
from string import *
s ="hello everyone"
print("find() function :",s.find("r"))
print("count() function :",s.count("e"))
print("endswith() function :",s.endswith("o"))
print("index() function :",s.index("l"))
print("isupper() function :",s.isupper())
print("lower() function :",s.lower())
print("capitalize() function :",s.capitalize())

#string count uppercase and lowercase letter
str1 ="Kumud Kundan Patil"
count1=0
count1=0
for i in str1:
    if(i.isupper()):
        count1+=1
    elif(i.islower()):
        count2+=1
print("Uppercase letter=",count1)
print("lowercase letters=",count2)



