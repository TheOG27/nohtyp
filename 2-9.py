#PRA-2 display msg on screen
'''print("Hello Everyone !!")'''

#PRA-3 Arithmetic operator, logical operator, bitwise operator
'''a = int(input("Enter the 1st number :"))
b = int(input("Enter the 2nd number :"))
print("Addition is :",a+b)
print("Subtraction is :",a-b)
print("Multipliction is :",a*b)
print("Division is :",a/b)
print("Modulus is :",a%b)
print("Floor Division is :",a//b)
print("Expoential is :",b**2)

a1=12
b1 = 56
c1= 34
print("Logical and :",(a1>b1)and (b1>c1))
print("Logical or :",(a1>b1)or (b1>c1))
print("Logical not :",not(a1>c1))

print(a&b)
print(a|b)
print(~b)
print(a^b)
print(a>>2)
print(a<<2)'''

#PRA-4 conditional statements
'''x=int(input("enter number :"))
if x%2==0:
    print(x,"is even.")

y= int(input("enter year :"))
if y%4==0:
    print(y,"is leap year.")
else:
    print(y,"is not leap year.")


if(25>100):
    if(25>15):
        print("25 is greater than 15 ")
    if(25>10):
        print("25 is grater than 10")
else:
    print("25 is small")'''


#PRA-5 loop
'''print("while loop")
counter =0
while(counter<10):
    print(counter)
    counter = counter +1

print("for loop")
sub = [1,2,3,4,5,7,6,8,9]
for i in sub:
    print(i)

print("nested loop")
a = int(input("Enter a number :"))
for i in range(0,a):
    for j in range(0,i+1):
        print("*",end="")
    print("\r")'''

#PRA-6
'''l1 =[12,23,34,45,56,67,78,89]
print(type(l1))
print(l1)
print(l1[5])
l1[5]=60
print(l1)
l1.append(43)
l1.extend([90])
l1.insert(2,22)
print(l1)
l1.remove(34)
print(l1)
del l1
print(l1)'''

#PRA-7
'''t1 =(12,23,45,67,24,97)
print(type(t1))
print(t1[2])
l1=list(t1)
print(type(l1))
l1[2]=29
l1[5]=20
print(l1)
t2 = tuple(l1)
print(t2)
del t2
print(t2)'''

#PRA-8
'''s1={12,23,34,45,56,67,78,89,90}
s2={98,87,76,65,54,43,32,21}
print(type(s1))
s1.add(30)
print(s1)
print("intersection :",s1&s2)
print("Union :",s1|s2)
print("set difference :",s1-s2)
print("symmetric difference:",s1^s2)
del s1
print(s1)'''

#PRA-9
'''d1 ={1:"one",2:"two",3:"three",4:"four"}
print(type(d1))
print(d1[3])
d1[5]="five"
print(d1)
del d1[5]
print(d1)

for key, value in d1.items():
    print(key,"-",value)

del d1
print(d1)'''




























