#program to create a random 10x4 array and extract the first five rows of the array and store them into a variable
import numpy as np
x=np.random.random((10,4))
print(x)
y=x[:5,:]
print(y)