#Check the number is prime or not
i = int(input("Enter number"))
fact =1
def myfunc(fact,i):
    while(i>0):
        fact=fact*i
        i-=1
    print("factorial=",fact)
myfunc(fact,i)

#factorial 
n=int(input("Enter number"))
def me(n):
    if n>1:
        for i in range (2,n):
            if(n%2==0):
                print(n,"is not prime")
            else:
                print(n,"is prime")
                break
        else:
            print("Please enter value greater than 1")
me(n)

#count the lowercase and uppercase letter 
str1="Kumud Kundan Patil"
count1=0
count2=0
def func1(str1,count1,count2):
    for i in str1:
        if(i.isupper()):
            count1+=1
        elif(i.islower()):
            count2+=1
    print("Uppercase letter count",count1)
    print("Lowercase letter count",count2)
func1(str1,count1,count2)

