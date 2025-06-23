import numpy as np 
#Joining or Concatenating NumPy Arrays

#1. Combining existing arrays Horizontally or Vertically using hstack() and vstack()
"""The syntax of using these functions is :
    numpy.hstack(<tuple containing names of 1D arrays to be stacked>)
    numpy.vstack(<tuple containing names of 1D arrays to be stacked>)
For hstack() to work, the arrays being joined must match in their vertical size and for vstack() to work, the arrays being joined must match in their horizontal size. Now look at the lists on the left. As per above rule, Ist1, Ist2, Ist3 match horizontal sizes and hence can be joined using vstack(). List Ist3 and Ist4 match in vertical sizes and hence can be joine using hstack().
"""
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst3 = [ [9, 8, 7], [6, 5, 4] ]
lst4 = [ [4], [5] ]

arr4 = np.vstack((lst1, lst2))
print(arr4)

arr5 = np.hstack((lst3, lst4))
print(arr5)

#2D Arrays
Arr1 = np.array([[0,1,2], [3,4, 5], [6,7,8]])
Arr2 = np.array([[10,11, 12], [13, 14, 15], [16,17, 18]])
Arr3 = np.vstack((Arr1, Arr2))
print(Arr3)
Arr4 = np.hstack((Arr1, Arr2))
print(Arr4)

#2. Combining existing arrays using concatenate()
"""The syntax for using concatenate() is :
    numpy.concatenate((<tuple of arrays to be joined>), [axis =< n>])
    
The axis argument specifies the axis along which arrays are to be joined. If skipped, axis is assumed as 0 (i.e., along the rows). If you specify axis = 1, then arrays are joined on axis 1 i.e., along the columns.
The arrays being joined must have the same shape except in the dimension corresponding to argument axis. That is, if axis is 0, then the shape of the arrays being joined must match on column dimension if axis is 1, then the shape of the arrays being joined must match on rows dimension.
"""
ar1 = np.array([[3,4,1],[6,8,5],[2,1,3]])
ar2 = np.array([[2,4,2],[1,9,1]])
ar3 = np.array([[6,1],[2,1],[8,5]])
jar1 = np.concatenate((ar1, ar2), axis = 0)
jar2 = np.concatenate((ar1, ar3), axis = 1)
print(jar1)
print(jar2)

#Transpose of Array
"""Syntax:
    <array>.T
"""
jar3 = np.concatenate((ar1, ar2.T), axis = 1)
print(jar3)
#If axis = None, the array get flattened
jar4 = np.concatenate((ar1, ar2), axis = None)
print(jar4)
