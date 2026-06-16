import numpy as np
arr=np.array([1,2,3,4])
print(arr)
print(type(arr))

print(np.__version__)
""" NumPy is used to work with arrays. The array object in NumPy is called ndarray.
We can create a NumPy ndarray object by using the array() function. 
To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, and it will be converted into an ndarray"""
arr1=np.array((23,45,67,89))
print(arr1)
""" Dimensions in Arrays
A dimension in arrays is one level of array depth (nested arrays).

nested array: are arrays that have arrays as their elements. 
0-D Arrays
0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.
Creation of 0d array"""
arr3=np.array(43)
print(arr3)
#1d array An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.

arr4=np.array([23,45,78,90])
print(arr4)
""" 2-D Arrays
An array that has 1-D arrays as its elements is called a 2-D array.

These are often used to represent matrix or 2nd order tensors.

NumPy has a whole sub module dedicated towards matrix operations called numpy.mat """
arr5=np.array([[1,2,3],[4,5,6]])
print(arr5)
""" 3-D arrays
An array that has 2-D arrays (matrices) as its elements is called 3-D array.

These are often used to represent a 3rd order tensor. """
arr6=([[[1,2,3],[4,5,6]],[[9,10,12],[10,12,13]]])
print(arr6)
#NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have
print(arr.ndim)
print(arr1.ndim)
print(arr3.ndim)
print(arr4.ndim)
print(arr5.ndim)
#Accessing Elements by using its index
print(arr1[0])
#Access 2d array
print(arr5[0,1])
#Access 3d array
#print(arr6[0, 1, 2]) Not Working
#Negative Accessing
print(arr5[0,-1])
#Slicing Index in Numpy
#When you have to print from the start Slicing topic revise agian triple way 1d,2d,3d
arr7=np.array([12,67,89,90])
print(arr7[0:5])
print(arr7[3:])
print(arr7[-3:-1])
print(arr7[:3])
print(arr7[:3])
print(arr[1:5:2])
print(arr7[::2])
#Slicing in 2d arrays
print(arr5[1,1:4])
#You can also check datatypes of the arrays
print(arr.dtype)
print(arr7.dtype)
print(arr5.dtype)
#You can use any type of datatypes like int,float,char,boolean etc
arr8=np.array(['cherry','banana','apple','orange','lemon'])
print(arr8.dtype)
""" Creating Arrays With a Defined Data Type
We use the array() function to create arrays, this function can take an optional argument: dtype that allows us to define the expected data type of the array elements: """

arr9=np.array([12,89,78.8,90],dtype='S')
print(arr9.dtype)
print(arr9)
""" Converting Data Type on Existing Arrays
The best way to change the data type of an existing array, is to make a copy of the array with the astype() method.

The astype() function creates a copy of the array, and allows you to specify the data type as a parameter.

The data type can be specified using a string, like 'f' for float, 'i' for integer etc. or you can use the data type directly like float for float and int for integer. """
#Conversion from float to integer
arr10=np.array([1.,2.3,4.5,8.9])
newarr=arr.astype('i')
print(newarr)
print(newarr.dtype)
newarr=arr.astype(int)
print(newarr)
#Conversion Integer to Boolean
newarr=arr.astype(bool)
print(newarr)
newarr=arr.astype(float)
print(newarr)
""" Difference Between Copy and View
The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.

The copy owns the data and any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.

The view does not own the data and any changes made to the view will affect the original array, and any changes made to the original array will affect the view. Make a copy, change the original array, and display both arrays:"""
x=arr10.copy()
arr10[0]=42
print(arr10)
print(x)
