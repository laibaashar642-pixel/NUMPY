#firstly, it is how can we check the shape,size,type of an array,whether we have to know the no of dimensions
#shape We can easily check the shape of an array it works only when you have to use the multidimensional array
import numpy as np
twod_array=np.array([[1.6,2,3],[45,9,89]])
print(twod_array.shape)
#2shows that rows are 2 and 3 shows the column
#Size returns the total no of elements
print(twod_array.size)
#Third is ndim which helps to check our no of dimension use tb krna hai jb hum 2d ,3d ya multidimensional array kai sth deal kr rhy hu
print(twod_array.ndim)
arr=np.array([[1,2,3],[4,5,6],[9,10,11]])
print(arr.ndim)
third_arr=np.array([[[1,2.9],[4,5.3]],[[7.3,8],[9,12.5]]])
print(third_arr.ndim)
zerod_array=np.array(23)
print(zerod_array.ndim)
oned_array=np.array([1,2,3,4])
print(oned_array.ndim)
#dtype means checking the dtype of the elements dtype (datatype of the elements)
print(twod_array.dtype)
#These topics all about checking
#And if i wanted to change the datatype of any value then we used astype It is used when we want to make any conversion
print(third_arr.astype('S'))
#type conversion ki trah hi hai bs array ko convert krna hota hai
arr1=np.array([12,23,56],[90,89,78])
