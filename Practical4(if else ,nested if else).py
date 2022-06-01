#Evenodd
num = int(input("Enter any number"))
if num%2==0:
    print("{} is even number".format(num) )
else:
    print("{} is odd number".format(num))
#EvenOdd end

#largest about of three

n1= int(input("enter 1st number"))
n2= int(input("enter 2nd number"))
n3= int(input("enter 3rd number"))
if n1>n2 and n2>n3:
    print("{0} in greater than {1}and {2}".format(n1,n2,n3))
elif n2>n1 and n2>n3:
    print("{0} in greater than {1}and {2}".format(n2,n1,n3))
else:
    print("{0} in greater than {1}and {2}".format(n3,n1,n2))

#largest about of three code ends

# year leap or not
year = int(input("Enter year"))
if year%4==0:
    print(year, "is leap year")
else:
    print(year,"is not a year ")
#year leap or not code end
