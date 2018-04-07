#program to shuffle numbers between 0 and 10 
import numpy as np
x=np.arange(10)
np.random.shuffle(x)
print(x)
print(np.random.permutaion(10))