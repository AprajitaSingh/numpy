#program to move axes of an array to new positions
import numpy as np
x=np.zeros((2,3,4))
print(np.moveaxis(x,0,-1))
