#calendar
import calendar
yy = int(input("Enter year"))
mm = int(input("Enter month"))
print(calendar.month(yy,mm))

#area of circle and circumference
from math import *
r = int(input("Enter radius"))
area = pi *r*r
cir=2*pi*r
print("Area of circle" ,area)
print("circumference of circle" ,cir)


#user define module
#here first code is save as mymod.py
def clg():
  str=input("Enter your clg name")
  print("your clg name is :",str)

  #here second code save as my.py
  from mymod import *
  clg()
