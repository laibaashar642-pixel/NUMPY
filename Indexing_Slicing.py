#Indexing and Slicing ki help sai kisi bhi specific position pr hum access kr skty hai Indexing mai hum aik element ko access krty hai (jahan pr apko aik element access krna hai wahan pr ) whereas slicng helps us to access multiple elements at a time and the other thing is fancy indexing multiple elements ko aik baar select krna using a list of indixes. And the other thing is Boolean Masking means hum aik certain condition dain gai aur us hisab sai filtering kry gai.Numpy always uses indexing start from zero index when we want to access the element.+ve indexing from left to right whereas -Ve indexing from right to left -ve indexing means kai i want to access the last element jb apko 1d array kai sth kaam krna hai tu indexing array[index] kry gai whereas lekin jb ap multidimensional kai sth kaam kry gai tu tb hum slicing use kry gai array[row,column]
import numpy as np
arr2=np.array([12,45,90,32,89])
print(arr2[0])
print(arr2[1])
print(arr2[4])

#Slicing array[start:stop:step] array[start:end],start to end -1,negative step,-1 reverse
arr=np.array([23,78,90,12])
print(arr[1:5])
print(arr[:4]) #it starts from this index 0 sai chaly gah aur 3 tk jye gha
print(arr[::2])#it gives every second element
print(arr[::-1])#it reverse the array
#Fancy Indexing is used when selecting elements at once jb bhi fancy indexing krni hai tu as a list pass krni hai
arr3=np.array([90,89,23,12])
print(arr3[[0,2,3]])
#Boolean Masking means filtering the data based on conditions generate only two things whether it is true or false.We can also use for loop to filtering but boolean masking is a best idea
print(arr3[arr3>34])
#Reshaping And Mainpulating Reshaping means array kai shape yani kai usky dimensions ko change krna without modifying the data like 1d sai 2d sai 3d reshape(rows,columns) specify new shape and it only dones when dimension matches
arr=np.array([1,2,3,4,5,6])
reshape_Arr=arr.reshape(2,3)#2rows chaye aur 3 columns
print(reshape_Arr)
#Reshape kbhi bhi copy nai krta bulkay it returns view(yani kai jo hamara original array aya hai aur uska new shape aya hai ussy farak pry gha)
#Flateening array one is ravel it returns the views jo original array hogha  usmy modification hogi flatter returns the copy array aur is sy original array pr effect nai hogha and the other is flatter it is used when we want to convert the multidimensional array into single  1d array
arr_2d=np.array([[1,2,3],[4,5,6]])
print(arr_2d.ravel())
print(arr_2d.flatten())
#Interview most imp question is what's the difference between ravel and flattten
