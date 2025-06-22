import numpy as np 
nar1 = np.array([2, 5.2, 10])
print(nar1)

#Using list
list1 = [1, 2, 3, 4, 5]
ar1 = np.array(list1)
print(ar1)

#Using tuple
tup1 = (1, 2, 3, 4, 5)
ar2 = np.array(tup1)
print(ar2)

#Type, dtype and size of array
print(type(ar1))
print(ar1.dtype)
print(ar1.itemsize)

#Access array's elements
print(ar1[1])
print(ar1[2])

"""Creating ndarrays using fromiter()
To create ndarrays from sequences of all types (numeric sequence, or string sequence or dictionaries etc.), you can use fromiter( ) function The fromiter( ) function is useful, when you want to create an ndarray from a non-numeric sequence. However, fromiter( ) supports all types of sequences-numeric or non-numeric.

The syntax to use fromiter() function is

    numpy.fromiter(<iterable sequence name>, <target data type>, [<count>])
"""
adic = {1:"A", 2:"B", 3:"C", 4:"D"}
ar3 = np.fromiter(adic, dtype = np.int32)
print(ar3)

astr = "Hello Brother, I'm Ayush!"
ar4 = np.fromiter(astr, dtype = "U2")
print(ar4)
"""fromiter() is creating an ndarray from a string with datatype U2 i.e., each element of ndarray can have length of 2 Unicode characters."""

#Count argument of fromiter()
ar5 = np.fromiter(astr, dtype = "U2", count = 10)
print(ar5)


#Using arange()
ar6 = np.arange(1, 10, 2, dtype = np.float32)
print(ar6)


#using linespace()
"""To generate evenly spaced elements between two given limits, NumPy provides linspace() function to which you provide, the start value, the end value and number of elements to be generated for the ndarray.
The syntax for using linspace() function is :
    <arrayname> = numpy. linspace(<start>, <stop>, <number of values to be generated>) """
ar7 = np.linspace(2.5, 8, 6)
print(ar7)


#Creating 2D Array using array()
list2 = [[1, 3, 5], [2, 4, 6]]
nd2 = np.array(list2)
print(nd2)
print(nd2.shape)

t1 = ((2, 4), (3, 5), (6, 4), (5, 6))
nd3 = np.array(t1)
print(nd3)
print(nd3.shape)

#Creating 2D Array using arange()
ar = np.arange(10)
ar8 = ar.reshape(5, 2)
ar9 = ar.reshape(2, 5)
print(ar8)
print(ar9)

"""In other words, the number of elements in the originally created ndarray must be the same as that of new 2D array being created through reshape().
You can also combine arrange() and reshape() in single statement."""
ary=np.arange(8.0).reshape(2, 4)
print(ary)


#Create an empty array
"""It is important to note the empty() does not mean that the array will have all zeros. With empty(), Python often creates an array with uninitialized garbage values."""
ar10 = np.empty([3, 2])
print(ar10)


#Creating arrays filled with zeros using zeros()
ar11 = np.zeros([2, 3], dtype = np.int64, order = 'C')
print(ar11)


#Creating arrays filled with ones using ones()
ar12 = np.ones([2, 3], dtype = np.float32)
print(ar12)

np.eye(5)
"""Create a 5 x 5 array with values O at non-diagonal positions and with 1 on diagonal (Identity matrix)"""

np.full((2,3), 6) #Create a 2x3 array with all values as 6

np.random.rand(3, 4) #Create a 3x4 array of random floats in the range 0 - 1

np.random.rand(4, 5) * 100 #Create a 4x5 array of random floats in the range 0- 100

np.random.randint(5,size=(2,3)) #Create a 2x3 array with random ints in the range 0-4