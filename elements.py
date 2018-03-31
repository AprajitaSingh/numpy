#Program to find the number of elements,length of one array element in bytes and total bytes consumed by the elements
import numpy as np
x=np.array([1,2,3,4,5])
print("Size of the array is:",x.size)
print("Size of each element is:", x.itemsize)
print("Total bytes consumed by the elements of the array: ",x.nbytes)
