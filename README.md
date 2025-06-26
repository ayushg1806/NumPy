
# NumPy Notes

NumPy (Numerical Python) is a powerful library for numerical computing in Python. It offers efficient array operations, broadcasting, and a wide range of mathematical functions.

---

## 1. Creating and Inspecting Arrays

### Array Creation
- `np.array([1, 2, 3])`: Creates a 1D array.
- `np.zeros((2, 3))`: 2x3 array of zeros.
- `np.ones((3, 2))`: 3x2 array of ones.
- `np.arange(0, 10, 2)`: Array from 0 to 8 with step 2.
- `np.linspace(0, 1, 5)`: 5 values evenly spaced from 0 to 1.

### Array Attributes
- `.shape`: Dimensions of the array.
- `.dtype`: Data type of array elements.
- `.ndim`: Number of dimensions.
- `.size`: Total number of elements.

---

## 2. Accessing & Modifying Elements

### Indexing and Slicing
- 1D: `arr[2]`
- 2D: `arr[1, 2]` or `arr[1][2]`
- Slicing: `arr[start:stop:step]`
- Multidimensional slicing: `arr[0:2, 1:3]`

### Modification
- Direct assignment: `arr[0] = 99`
- Modify slices: `arr[1:3] = [10, 20]`

---

## 3. Joining Arrays

### Concatenation
- `np.concatenate([a, b])`: Joins arrays along an axis.
- `np.vstack([a, b])`: Stack vertically (row-wise).
- `np.hstack([a, b])`: Stack horizontally (column-wise).
- `np.stack([a, b])`: Adds a new dimension.

---

## 4. Splitting Arrays

- `np.split(arr, 3)`: Split into 3 equal parts.
- `np.array_split(arr, 3)`: Split into 3 parts, even if not equal.
- `np.vsplit(arr, 2)`: Vertical split.
- `np.hsplit(arr, 2)`: Horizontal split.

---

## 5. Extracting Subsets
You can extract non-contiguous subsets of a NumPy array by applying condition on the NumPy array. The specified condition will be applied to each element of the array and the elements meeting the criteria will be part of the subset array returned. This is done with the help of extrat() as per following syntax:

`numpy.extract(<condition>, <array>)`

- `condition` is a condition applied on an ndarray.
- `array` is the ndarray on which the `condition` is applied.

The extract() always returns the elements of given ndarray that fulfill the criteria of `condition` in 1D ndarray form.

---

## 6. Arithmetic & Mathematical Operations

### Element-wise Operations
- `+`, `-`, `*`, `/` work element-wise.

### Broadcasting
Allows operations on arrays of different shapes:
```python
a = np.array([1, 2, 3])
b = 2
a + b  # [3, 4, 5]
```

### Common Functions
- `np.sum(arr)`, `np.mean(arr)`, `np.std(arr)`
- `np.min(arr)`, `np.max(arr)`
- `np.sqrt(arr)`, `np.exp(arr)`, `np.log(arr)`

---

## 7. Matrix Operations

### Dot Product
- `np.dot(a, b)` or `a @ b`

### Transpose
- `arr.T`

### Identity & Inverse
- `np.eye(3)`: 3x3 Identity matrix
- `np.linalg.inv(arr)`: Inverse of a matrix

---

## 8. Random Number Generation

- `np.random.rand(2, 3)`: Uniform random numbers in [0, 1)
- `np.random.randn(3, 3)`: Standard normal distribution
- `np.random.randint(0, 10, size=(2, 2))`: Random integers

---

## 9. Reshaping & Manipulation

- `arr.reshape((2, 3))`: Change shape
- `arr.flatten()`: Flatten to 1D
- `arr.ravel()`: Flatten view (memory efficient)
- `arr.T`: Transpose

---

## 10. Performance Tips

- Use NumPy's **vectorized operations** instead of loops for better performance.
- Avoid Python lists when working with large numerical data.
- Use `.copy()` when needed to avoid modifying the original array unintentionally.

---
