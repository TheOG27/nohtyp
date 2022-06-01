tup1 =(12,23,45,67,24,97)
#tup type
print(type(tup1))
#tup accessing element
print(tup1[2])
list1=list(tup1)
print(type(tup1))
#updating tuplr
list1[2]=29
list1[5]=20
print(list1)
tup2 = tuple(list1)
print(tup2)
#deleting tuple element
del tup1
print(tup1)
#max and min value in tuple
tup3=(10,20,30,40,50)
print("Maximum value in tuple",max(tup3))
print("Minimum value in tuple",min(tup3))
#repeated items in tuple
tup4=(1,2,3,4,5,6,7,7,5)
l=[]
for e in tup4:
    if(tup4.count(e)>1):
        l.append(e)
for e in l:
    print(e)
print("Above are repeated item ")
