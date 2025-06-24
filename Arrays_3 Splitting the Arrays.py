#Splitting the Arrays (Obtaining the Contiguous Subsets of Arrays)

#1. Using hsplit() and vsplit() functions:
"""
    hsplit(): extract the subsets of an array after splitting it horizontally (along x-axis)
        np.hsplit(<array>, <n>)
        
    vsplit(): extract the subsets of an array after splitting it vertically (along y-axis)
        np.vsplit(<array>, <n>)
"""
import numpy as np 
ary = np.arange(24).reshape(4, 6)
print(ary)

ary1 = np.hsplit(ary, 2)
ary2 = np.vsplit(ary, 2)
print(ary1)
print(ary2)

#2. Using split() function:
"""
The split( ) function is a general function using which you can split a NumPy array both horizontally and vertically by providing axis argument (axis = 0 for horizontal axis based division, axis = 1 for vertical axis based division). Also, the split() allows you to divide array into equal as well as non-equal subarrays.
The syntax for using split():
    numpy.split(<array>, <n>|<1D array>, [axis= 0])
"""
#1D Array
ar1d = np.array([10,11,12,13,14,15,16,17,18,19])
print(np.split(ar1d, [2, 6])) #[0:2] [2:6] [6:]

#2D Array
print(np.split(ary, [1, 4])) #axis = 0
print(np.split(ary, [2, 5], axis = 1)) #axis = 1