#program to find common values between two arrays
import numpy as np
x=np.array([1,2,56,78,90,77,89])
y=np.array([56,78,90])
print(np.intersect1d(x,y))