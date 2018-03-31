#program to test whether each element of a 1-D array is also present in a second array.
import numpy as np
x=np.array([1,2,56,78,90,77,89])
y=np.array([56,78,90])
print(np.in1d(x,y))