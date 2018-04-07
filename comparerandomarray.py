#program to check two random arrays are equal or not
import numpy as np
x=np.random.randint(0,2,6)
y=np.random.randint(0,2,6)
equal=np.allclose(x,y)
print(equal)