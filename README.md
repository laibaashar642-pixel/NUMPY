NumPy
1. What is NumPy?
NumPy (Numerical Python) is a foundational open-source library for scientific computing in Python. It provides fast, memory-efficient multi-dimensional arrays and a huge collection of mathematical functions to operate on them. Nearly every data science, machine learning, and scientific Python library — pandas, scikit-learn, TensorFlow, SciPy — is built on top of NumPy internally.Numpy is 52 times faster than actual python list,uses less memory and easy use maths operation.
Nd arrays jo python ki list ki trah hi hoty hai but many times faster hoty hai
Quick import convention: import numpy as np  (always use this alias — every tutorial and codebase uses it)

2. How NumPy Was Discovered — The History
The problem: Python lists are slow for math
In the early 2000s, scientists and engineers were using Python because of its clean syntax, but they struggled with one major issue: Python lists are general-purpose and store references to objects, making numerical computation painfully slow compared to languages like C, C++, or Fortran.
The early solution: Numeric and Numarray
In 1995, Jim Hugunin created a library called Numeric for Python, which introduced array objects with efficient memory storage. Around 2001, a competing library called Numarray emerged with more features. However, the community was now split between two incompatible libraries — a major problem.
The birth of NumPy (2005)
Travis Oliphant, a graduate student at Mayo Clinic at the time, took the challenge of unifying both libraries. In 2005, he created NumPy by combining the best parts of Numeric and Numarray into a single, consistent library. He released it as open-source and it quickly became the community standard.
Why it worked so well
•	NumPy arrays store data in contiguous blocks of memory — just like C arrays — making them extremely fast.
•	It allowed Python to call C and Fortran code under the hood, getting near-native performance.
•	The API was clean, consistent, and well-documented.
•	It became the base layer that pandas, SciPy, Matplotlib, and later TensorFlow all depended on.
Today: NumPy is maintained by the NumFOCUS foundation and has millions of users worldwide. Version 2.0 was released in 2024.

3. Important Terms & Concepts
These are the core vocabulary of NumPy. You will encounter them constantly:

Term	Explanation
ndarray	The core object in NumPy — an N-dimensional array. Short for 'N-Dimensional Array'. Everything in NumPy is built around this.
dtype	Data type of array elements (int32, float64, bool, etc.). All elements in one ndarray share the same dtype — unlike Python lists.
shape	A tuple describing the size of each dimension. (3, 4) means 3 rows and 4 columns. (5,) means a 1D array with 5 elements.
ndim	Number of dimensions (axes) in the array. 1D = vector, 2D = matrix, 3D = tensor/cube.
size	Total number of elements in the array. Equals the product of all values in shape.
axis	A specific dimension. axis=0 goes DOWN rows, axis=1 goes ACROSS columns. Critical for sum, mean, etc.
broadcasting	NumPy's rules for doing math between arrays of different shapes by automatically 'stretching' the smaller array.
Multidimensional means ore than 2d arrays whether it is 3d,4d,5d........
Matrix is a fancy name for 2d array
vectorization	Applying an operation to an entire array at once, without writing a for-loop. The key to NumPy's speed.
indexing	Accessing specific elements using square brackets: a[0], a[1:4], a[row, col].
boolean mask	An array of True/False values used to filter elements: a[a > 5] returns only elements greater than 5.
view	A reshaped or sliced array that shares the same memory as the original. Changing one changes the other.
copy	An independent array with its own memory. Use a.copy() to make one explicitly.
reshape	Changing the shape of an array without changing its data. Total elements must remain the same.
flatten / ravel	Converting any array back to 1D. flatten() always returns a copy; ravel() returns a view when possible.
dot product	Matrix multiplication. Use A @ B or np.dot(A, B). Different from element-wise * multiplication.
broadcasting rule	Shapes are compatible from the RIGHT. Dimensions must either match or one of them must be 1.
universal function (ufunc)	Functions like np.sqrt, np.abs, np.exp that apply element-wise to every element in an array.
argmax / argmin	Return the INDEX (position) of the maximum or minimum value, not the value itself.
np.where	An element-wise if-else. np.where(condition, value_if_true, value_if_false).
np.arange	Like Python's range() but returns an ndarray. np.arange(start, stop, step).
np.linspace	Creates N evenly spaced numbers between start and stop (inclusive). Great for plotting.

4. Deep Dive: The ndarray Object
The ndarray (n-dimensional array) is the heart of NumPy. Understanding it is understanding NumPy.
What makes ndarray special?
•	Homogeneous: every element has the exact same data type (dtype). This allows NumPy to store data in a flat, contiguous block of memory.
•	Fixed-size: the size of an ndarray is fixed at creation. Appending to it creates a new array.
•	Efficient: operations run in compiled C code — typically 100x faster than equivalent Python loops.
•	N-dimensional: can represent scalars (0D), vectors (1D), matrices (2D), and tensors (3D+).
Memory layout: how numpy stores data
Under the hood, a 2D array like [[1,2,3],[4,5,6]] is stored in memory as a flat sequence [1,2,3,4,5,6]. The shape and strides tell NumPy how to interpret that flat memory as a multi-dimensional structure. A 'stride' is how many bytes to jump to move one step along each dimension.
Creating ndarray objects
np.array([1, 2, 3])              # 1D from list
np.array([[1,2],[3,4]])           # 2D from nested list
np.zeros((3, 4))                 # 3x4 of zeros, dtype=float64
np.ones((2, 3), dtype=np.int32)  # 2x3 of ones, dtype=int32
np.arange(0, 20, 2)              # [0,2,4,6,8,10,12,14,16,18]
np.linspace(0, 1, 5)             # [0.0, 0.25, 0.5, 0.75, 1.0]
np.random.rand(3, 3)             # 3x3 of random floats between 0 and 1
Inspecting an ndarray
a = np.array([[1,2,3],[4,5,6]])
a.shape    # (2, 3)  — 2 rows, 3 columns
a.ndim     # 2       — it is a 2D array
a.size     # 6       — 6 total elements
a.dtype    # int64   — default integer type
a.nbytes   # 48      — total bytes in memory (6 x 8 bytes each)

5. Core Concepts to Remember
Indexing and slicing
The rule for 2D arrays is always: m[row, column]. Slicing follows Python's start:stop:step syntax where stop is NOT included.
a = np.array([10, 20, 30, 40, 50])
a[0]       # 10  (first element)
a[-1]      # 50  (last element)
a[1:4]     # [20, 30, 40]  (index 1 to 3)
a[::2]     # [10, 30, 50]  (every 2nd)
m[:, 0]    # all rows, first column
m[0, :]    # first row, all columns
Boolean filtering
One of the most powerful NumPy features. Create a mask of True/False, then use it to select elements.
scores = np.array([45, 78, 92, 55, 88, 33])
scores[scores >= 60]              # [78, 92, 88]  — passing scores
scores[(scores>50) & (scores<90)] # [78, 55, 88]  — use & not 'and'
Broadcasting
NumPy can add a scalar or a differently-shaped array to a larger one by automatically expanding (broadcasting) the smaller one. This avoids the need for for-loops.
m = np.array([[1,2,3],[4,5,6]])
m + 100          # adds 100 to every element
m * np.array([1,2,3])  # multiplies each ROW element-wise
The axis parameter
Many functions like sum(), mean(), max() accept an axis argument that changes what gets reduced.
m = np.array([[1,2,3],[4,5,6]])
np.sum(m)         # 21     — sum of everything
np.sum(m, axis=0) # [5,7,9] — sum down each column
np.sum(m, axis=1) # [6,15]  — sum across each row

6. Quick Reference Cheat Sheet

Function / Syntax	Example	Output / Effect
np.array([1,2,3])	np.array([10,20])	ndarray from list
np.zeros((r,c))	np.zeros((2,3))	All-zero array
np.ones((r,c))	np.ones((3,3))	All-ones array
np.arange(s,e,step)	np.arange(0,10,2)	[0,2,4,6,8]
np.linspace(s,e,n)	np.linspace(0,1,5)	5 evenly spaced values
np.eye(n)	np.eye(3)	3x3 identity matrix
np.random.rand(r,c)	np.random.rand(2,3)	Random floats 0–1
a.shape	a.shape	(rows, cols) tuple
a.reshape(r,c)	a.reshape(3,4)	Change shape
a.flatten()	a.flatten()	Collapse to 1D
a.T	a.T	Transpose rows/cols
a[i]	a[2]	Index element
a[s:e]	a[1:4]	Slice elements
a[a>5]	a[a>10]	Boolean filter
np.where(c,x,y)	np.where(a>5,1,0)	Element-wise if-else
np.sum(a,axis=)	np.sum(m,axis=0)	Sum along axis
np.mean/std/max/min	np.mean(a)	Statistics
np.argmax/argmin	np.argmax(a)	Index of max/min
np.sort(a)	np.sort(a)	Sorted copy
A @ B	A @ B	Matrix multiplication
np.hstack/vstack	np.vstack([a,b])	Combine arrays
np.concatenate	np.concatenate([a,b])	Join arrays

7. Study Tips for Beginners
•	Always import as: import numpy as np — this is the universal convention.
•	Practice in a Jupyter Notebook so you can see output instantly after each cell.
•	When confused about shape, print a.shape and a.ndim before doing anything else.
•	Master indexing before moving to operations — everything builds on it.
•	When you get an error about shapes, read the error carefully — NumPy tells you exactly what went wrong.
•	Use np.arange for integer sequences, np.linspace when you need exact number of points.
•	Remember: axis=0 goes DOWN (reduces rows), axis=1 goes ACROSS (reduces columns).
•	Boolean filtering is used constantly in real data work — practice it daily.
•	The difference between a view and a copy trips up even experienced users. When in doubt, use .copy().

Happy Learning! — NumPy is the foundation of all of Python's data science ecosystem.
