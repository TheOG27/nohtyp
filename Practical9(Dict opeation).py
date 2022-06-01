dict1 ={1:"one",2:"two",3:"three",4:"four"}
print(type(dict1))
print(dict1[3])
dict1[5]="five"
print(d1)
del dict1[5]
print(dict1)

for key, value in dict1.items():
    print(key,"-",value)

del dict1
print(dict1)

#dictionaries concatenation
def union(d1,d2,d3):
    ans=dict()
    for ele in d1.items():
        ans.update({ele[0]:ele[1]})
    for ele in d2.items():
        ans.update({ele[0]:ele[1]})
    for ele in d3.items():
        ans.update({ele[0]:ele[1]})
    return ans

dict1={1:10,2:20}
dict2={3:30,4:40}
dict3={5:50,6:60}
concated = union(dict1,dict2,dict3)
print(concated)
#combine two dict  with comman value

d4={'a':300,'b':200,'c':300}
d5={'a':100,'b':200,'c':400}
d3={}
for i, j in d4.items():
    for x, y in d5.items():
        if i==x:
            d3[i]=(j+y)
print("adding values to common key",d3)



