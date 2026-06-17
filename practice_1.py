"""Create a NumPy array containing:

[10, 20, 30, 40, 50] """
import numpy as np
arr=np.array([10,20,30,40,50])
print(arr)
""" Create a 2D array:
[[1, 2, 3],
 [4, 5, 6]] """
arr1=np.array([[1,2,3],[4,5,6]])
print(arr1)
# Create an array of zeros with 5 elements.
arr2=np.zeros(5)
print(arr2)
# Create an array of ones with shape (3,4).
arr3=np.ones((3,4))
print(arr3.shape)
# Create an array containing numbers from 1 to 20.
arr4=([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
arr4=np.arange(1,21)
print(arr4)
#Find the dimension (ndim) of:
a = np.array(42)
print(a.ndim)
# Find the dimension of:
b = np.array([1,2,3,4])
print(b.ndim)
# Find the dimension of:

c = np.array([[1,2],[3,4]])
print(c.ndim)
# Create a 3D array and print its dimensions.
arr5=([[1,2,3],[8,9,10]],[[12,13,15],[23,43,55]])
print(arr5)
# Find the shape of:

d = np.array([[1,2,3],[4,5,6]])
print(d.shape)
e = np.array([10,20,30,40,50])
# Print the first element.
print(e[0])
#Print the last element.
print(e[4])
#Print the third element.
print(e[2])
f = np.array([[10,20,30],[40,50,60]])
#Print 20.
print(f[0][1])
#Print 60.
#print(f[[1,2]])
#Slicing
g = np.array([1,2,3,4,5,6,7,8,9])
#Print elements from index 2 to 5.
print(g[1:6])
#Print first 4 elements.
print(g[:4])
#Print last 3 elements.
print(g[-3:])
#Print every second element.
print(g[::2])
#Check datatype of:

h = np.array([1,2,3])
print(h.dtype)
#Create array with datatype float.
i = np.array([1,2,3],dtype='S')
i = np.array([1,2,3],dtype=float)
print(i)
#Print datatype of:
j = np.array(['apple','banana'])
print(j.dtype)
#Copy 
k = np.array([1,2,3,4,5])
l=k.copy()
print(l)
#Change first element of original array to 100.
k[0]=100
print(l)
#Create a view of array.
print(l.view)