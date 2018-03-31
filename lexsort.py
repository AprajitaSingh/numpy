#Program to sort two arrays , sorting by first and then second
import numpy as np
a = [1,5,1,4,3,4,4]
b = [9,4,0,4,0,2,1]
ind=np.lexsort((b,a))
print(ind)