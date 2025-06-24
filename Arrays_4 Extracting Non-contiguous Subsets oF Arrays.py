#Extracting Non-contiguous Subsets of Arrays
"""You can extract non-contiguous subsets of a NumPy array by applying condition on the NumPy array. The specified condition will be applied to each element of the array and the elements meeting the criteria will be part of the subset array returned. This is done with the help of extrat() as per following syntax:

    numpy.extract(<condition>, <array>)

    <condition> is a condition applied on an ndarray.
    <array> is the ndarray on which the <condition> is applied.
The extract() always returns the elements of given ndarray that fulfill the criteria of <condition> in 1D ndarray form.
"""
import numpy as np 
ary = np.arange(24.0).reshape(4, 6)
condition = np.mod(ary, 2) == 0
print(condition)

print(np.extract(condition, ary))


