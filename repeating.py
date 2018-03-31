#Python program to construct an array by repeating
import numpy as np
x=np.array([0,10,20,40,60,80])
y=np.tile(x,2)
print(y)
y=np.tile(x,3)
print(y)