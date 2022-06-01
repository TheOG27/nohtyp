#matrix opeation fist code
import numpy as np
M1= np.array([[1,2,3],[4,5,6],[7,8,9]])
M2= np.array([[9,8,7],[6,5,4],[3,2,1]])
print("Matrix Addtion\n",np.add(M1,M2))
print("Matrix Subtraction\n",np.subtract(M1,M2))
print("Matrix Multiplication\n",np.multiply(M1,M2))
print("Matrix division\n",np.divide(M1,M2))


#concate to string second code
import numpy as np
print("concate Two strings")
first=np.array(["Kumud"],dtype=np.str)
second=np.array(["Patil"],dtype=np.str)
full=np.char.add(first,second)
print(full)



# generate six random intrger

mport numpy as np
x =np.random.randint(10,30,6)
print(x)
