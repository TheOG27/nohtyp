list1=[10,20,30,40,50,60]
#accessing list element
print(list1[3])
#updating list element
list1[0]=70
print(list1)
#append can add element at last
list1.append(70)
print(list1)
#extend can add multiple element
list1.extend([80,90])
print(list1)
#insert method
list1.insert(2,22)
print(list1)
list1.remove(70)
print(list1)
del list1[2]
print(list1)
print("Maximum value of element ",max(list1))
print("Minimum value of element ",min(list1))
total= sum(list1)
print("sum of all element in given list",total)
