#Arithmetic Opeations on Arrays
"""1. Using Operators:
    <ndarray1>+<n>|<ndarray2>
    <ndarray1> - <n> |<ndarray2>
    <ndarray1> * <n> |<ndarray2>
    <ndarray1> / <n> |<ndarray2>
    <ndarray1> % <n>|<ndarray2>
    
    2. Using NumPy Functions:
    Numpy.add(<ndrray1>, <n>|<ndarray2>)
    Numpy.subtract(<ndrray1>, <n>|<ndarray2>)
    Numpy.multiply(<ndrray1>, <n>|<ndarray2>)
    Numpy.divide(<ndrray1>, <n>|<ndarray2>)
    Numpy.mod(<ndrray1>, <n>|<ndarray2>)
    Numpy.remainder(<ndrray1>, <n>|<ndarray2>)
"""
import numpy as np
ary = np.arange(24.0).reshape(4, 6)
new = ary + 2.1
twos = np.full((4, 6), 2)

#Addition
print(ary + 0.3) #OR print(np.add(ary, 0.3))
print(np.add(ary, new))

#Subtraction
print(ary - 6) #OR print(np.subtract(ary, 6))

#Multiplication
print(np.multiply(ary, twos))