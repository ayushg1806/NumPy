import numpy as np 
#Accessing individual elements using indexing
arr = np.array([17, 23, 11, 18])
print(arr[2])
print(arr[-1])

#2D array
arr1 = np.array([[17, 23, 11, 18], [55, 33, 28, 27]])
print(arr1[1, 2])
print(arr1[1][3])
print(arr1[-1][-1])


#Modifying the values of array
arr[1] = 25
arr1[1, 3] = 67


#Array Slicing (extracting a subset of elements from an existing array and returning the result as another array)
#1D Array
arr2 = np.array([2,4,6,8,10,12,14,16])
print(arr2[3:7])
print(arr2[:-1]) #from 0 to end (-1)
print(arr2[:-2])
print(arr2[2:7:2])

#2D Array
arr3 = np.array([[2,4,6,8,10],[12,14,16,18,20],[22,24,26,28,30],[32,34,36,38,40]])
#array_name[row_slicing, column_slicing]
print(arr3[:3, 3:])
print(arr3[1::2, :3])
print(arr3[::3, ::2])
print(arr3[-3:-1, -5::2])
print(arr3[3, :]) #all columns
print(arr3[:, 4]) #all rows
print(arr3[:, :])