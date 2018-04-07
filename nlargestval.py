#program to get the n largest values of an array.
import numpy as np
x=np.arange(24)
np.random.shuffle(x)
n=5
print(x[np.argsort(x)[-n:]])
