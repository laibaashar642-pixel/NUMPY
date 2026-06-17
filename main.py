
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

""" Creation of arrays from python list so numpy had given us an array function which is called ndarray 
Creation of arrays with default values numpy provides a built in function which is called zeroes function jis sai hamara khali array fillup ho jye gha means zero zero hojye gha"""
zeros_array=np.zeros(3)
print(zeros_array)
#Aur agr muje zeros ki jga one fillup krna ho
ones_array=np.array([1,2,3])
print(ones_array)
"""Dimensions in Arrays
A dimension in arrays is one level of array depth (nested arrays).Creation of arrays from python list 


nested array: are arrays that have arrays as their elements. 
0-D Arrays
0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.
Creation of 0d array"""
arr3=np.array(43)
print(arr3)
#1d array An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.
arr4=np.array([23,45,78,90])
print(arr4)
#matrix menas jo 2d array hi hoty bs unka aik fancy name hai
matrix=np.array([[2,4,6],
             [6,7,8]])
print(matrix)
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
#making a view changing the orginal array both view and copy did this
x=arr10.view()
print(x)
x[0]=31
x[1]=23
x[2]=89
print(x)
print(x)
print(x)
""" Check if Array Owns its Data
As mentioned above, copies owns the data, and views does not own the data, but how can we check this?

Every NumPy array has the attribute base that returns None if the array owns the data.

Otherwise, the base  attribute refers to the original object. """
#Shape of an array is the number of elementsnin each dimension
#NumPy arrays have an attribute called shape that returns a tuple with each index having the number of corresponding elements.
a=np.array([[12,34,56],[19,89,45]])
print(a.shape)
b=np.array([23,89,45],ndmin=5)
print(b.shape)
#Reshaping Array means changing the shape of an array.The shape of an array means the no of elements in each dimension whether the reshaping means changing the,add or remove dimensions or change the number of elements in each dimension
#Convert the 1 d array into 2d array
""" c=np.array([12,78,45,90,34])
newarr = c.reshape(4, 3)

print(newarr)
 """
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(4, 3)

print(newarr)
#Reshaping from 1d to 3d
newarr=arr.reshape(2,3,2)
print(newarr)
#Flatenning the array means converting the multidimensional array into oned array
i=np.array([[12,34,56],[90,45,67]])
h=i.reshape(-1)
print(h)
""" Iterating means going through elements one by one.

As we deal with multi-dimensional arrays in numpy, we can do this using basic for loop of python.

If we iterate on a 1-D array it will go through each element one by one. """
j=np.array([1,2,3])
for x in j:
    print(j)

# In a 2-D array it will go through all the rows.
k=np.array([[2,3,4],[5,6,7]])
for x in k:
    print(x)
# In a 3-D array it will go through all the 2-D arrays.
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
    print(x)
    for y in x:
        for z in y:
            print(z)