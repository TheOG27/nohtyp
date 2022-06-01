a={1,2,3,4,5,6,7}
b={7,8,9,10}
print("a=",a)
print("b=",b)
print("\nunion = ",a.union(b))
print("\nintersectoin =",a.intersection(b))
print("\ndifference =",a.difference(b))
print("\nsymmetric_difference =", a.symmetric_difference(b))
#length of set
print("Length of set ", (len(a)))
#max and min value
print("Maximum value ", max(a))
print("Minimum value ", min(a))
#add and remove element
a.add(8)
print(a)
a.discard(8)
print(a)
