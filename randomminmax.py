#program to create a 5x5 array with random values and find the minimum and maximum values
import numpy as np
x=np.random.random((5,5))
print("The minimum value is",x.min())
print("The maximum value is",x.max())
