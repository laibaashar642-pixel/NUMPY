
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
print(ones_array
      )
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
#Agr hamay ones aur zeros kai ilawa values fillup krni hai tu so numpy provides a full shape value function
filled_array=np.full((2,2),7)
print(filled_array)
#Creating sequence of numbers in numpy arange() function used like a range function used in python language The difference is it returns numpy array we have to pass three things(start,stop,step)
arr=np.arange(1,12,3)
print(arr)
#How can we create identity matrixes it is a square matrix with ones of diagonal and squares of the ones both ends here
identity_matrix=np.eye(3)
print(identity_matrix)
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

#Array Join means putting contents of two or more arrays in a single array.In SQL we joined tables by a key whereas in numpy we join array by axes We pass a sequence of arrays that we want to join to the concatenate() function, along with the axis. If axis is not explicitly passed, it is taken as 0.
arr1=np.array([12,34,56])
arr2=np.array([12,34,56])
arr=np.concatenate((arr1,arr2))
print(arr)
#join 2d arrays along rows axis=1
arr1=np.array([[1,2,3],[3,4,5]])
arr2=np.array([[45,67,90],[9,2,1]])
arr=np.concatenate((arr1,arr2),axis=1)
print(arr)
#Joining arrays as by using stack functionStacking is same as concatenation, the only difference is that stacking is done along a new axis.

""" We can concatenate two 1-D arrays along the second axis which would result in putting them one over the other, ie. stacking.

We pass a sequence of arrays that we want to join to the stack() method along with the axis. If axis is not explicitly passed it is taken as 0. """
arr1=np.array([12,56,90])
arr2=np.array([1,57,80])
arr=np.stack((arr1,arr2),axis=1)
print(arr)
#Numpy also provides a function hstack to make stacking along the rows
arr=np.hstack((arr1,arr2))
print(arr)
#Stacking along the columns numpy provides us the vstack function
arr=np.vstack((arr1,arr2))
print(arr)
#Numpy provides a function to stack along the height which is same as depth
arr=np.dstack((arr1,arr2))
print(arr)
#Splitting is a reverse operation of array joining.Joing merge multiple arrays into single one whereas splitting breaks the single array into multiple arrays.Numpy provides a split function to split the array
arr=np.array([12,34,56,67])
newarr=np.array_split(arr,3)
print(newarr)
print(newarr[0])
print(newarr[1])
print(newarr[2])
#For splitting 2d arrays
arr=np.array([[1,2],[3,4],[9,0],[10,12],[89,67]])
newarr=np.array_split(arr,3)
# Use the hsplit() method to split the 2-D array into three 2-D arrays along columns.
newarr=np.hsplit(arr,2)
print(newarr)
#Similar alternates to vstack() and dstack() are available as vsplit() and dsplit().
#Searching Arrays You can search an array for a certain value, and return the indexes that get a match.To search an array, use the where() method.
arr=np.array([[12,34,56],[90,89,56]])
newarr=np.where(arr==34)
print(newarr)
#Find indexes where the values are odd
x = np.where(arr%2 == 1)

print(x)
""" There is a method called searchsorted() which performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order. 
serach sorted array 1d pr kaam krta hai 2d pr nai """
arr2=([23,78,90,87,56,43])
x=np.searchsorted(arr2,7,side='right')
""" Search From the Right Side
By default the left most index is returned, but we can give side='right' to return the right most index instead. """

x = np.searchsorted(arr2, 7, side='right')

print(x)
""" Multiple Values
To search for more than one value, use an array with the specified values. """
x=np.searchsorted(arr2,[2,4,6])
print(x)
#Sorting means putting elements in an ordered sequence.Ordered sequence is any sequence that has an order corresponding to elements, like numeric or alphabetical, ascending or descending.The NumPy ndarray object has a function called sort(), that will sort a specified array.

arr=np.array([2,3,1])
print(np.sort(arr))
#  This method returns a copy of the array, leaving the original array unchanged.You can also sort array of things and any other datatype
arr=np.array(['banana','apple','lemon'])
print(np.sort(arr))
#if you use sort method on 2d array then both arrays will be sorted
arr = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr))
#Filtering Method Getting some elements out of an exsisting array and creating a new arrayy out of them is called filtering.In numpy you filter an array by usig boolean index listIf the value at an index is True that element is contained in the filtered array, if the value at that index is False that element is excluded from the filtered array.
arr = np.array([41, 42, 43, 44])

x = [True, False, True, False]

newarr = arr[x]

print(newarr)
