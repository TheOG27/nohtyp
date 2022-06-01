#only for factorial
import math
 
def factorial(n):
    return(math.factorial(n))
n = 5
print("Factorial of", n, "is",factorial(n))


#fact end
#print even num betw 1 to 100
for num1 in range(2,100):
    if num1%2==0:
        print(num1)
        

#code ends

#palidrome or not
n1=int(input("Enter number"))
temp=n
rev=0
while (n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
if (temp==rev):
    print("Number is palindrome")
else:
    print("Number is Not Palidrome")

#sum of digit
n=int(input("Enter number"))
total=0
while(n>0):
    dig=n%10
    total=total+dig
    n=n//10
print("The sum of digit",total)
