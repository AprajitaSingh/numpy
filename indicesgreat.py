#program to get the values and indices of the elements that are bigger than 10 in a given array
import numpy as np
x=np.array([[0,10,20],[20,30,40]])
print(np.nonzero(x>10))
