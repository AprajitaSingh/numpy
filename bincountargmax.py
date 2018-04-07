#program to find the most frequent value in an array
import numpy as np
x=np.random.randint(1,10,40)
print(np.bincount(x).argmax())