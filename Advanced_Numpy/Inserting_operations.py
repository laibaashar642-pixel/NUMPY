#First one is inserting np.insert(array,index,value,asix=None) array
# -original array , index-,value-,axis- If i am working with 2d array then axis is 0 and i wanted to insert the data row-wise but if the axis is 1 then axis is 1 and insert the data column-wise
import numpy as np
arr=np.array([23,45,67,90])
print(arr)
newarr=np.insert(arr,2,100)

print(newarr)#Means kai muje 2 kai index mai abhi 67 hai uski jagah muje 100 chaye
#how can we insert in 2d array
arr_2d=([[1,2],[3,4]])
print(arr_2d)
newarr_2d=np.insert(arr_2d,1,[5,6],axis=1)#For column version 
newarr_2d=np.insert(arr_2d,1,[5,6],axis=0)#For row version
newarr_2d=np.insert(arr_2d,1,[5,6],axis=None)#For flatten(single line)
print(newarr_2d)
#next Operation is appending when i have to add the element in array but at the end
newarr=([1,23,45,67])
arr=np.append(newarr,[40,50,60])
print(arr)
#Concatenation If i wanted to join the two arrays then we used concatenation
arr1=np.array([23,89,90])
arr2=np.array([20,69,9])
newarr=np.concatenate((arr1,arr2))
print(newarr) #concatenate function hamaray pass elemnets kai end pr add kry gha jb kai jo hamary pass insert function hai wo specific point pr element add kry gah
#Deleting Commmand np.delete(array,index,axis=None)Flattern Array It is a method of deleting oned array
arr=np.array([34,57,90,12])
print(arr)
newarr=np.delete(arr,0)
print(newarr)
#It is a method of deleting 2d array
arr_2d=np.array([[1,2,3],[4,5,6]])
newarr_2d=np.delete(arr_2d,0,axis=0)
print(newarr_2d)
#Stacking means from top to bottom vertically horizontally vstack() rowwise  hstack() columnwise
arr1=np.array([89,67,34,12])
arr2=np.array([23,90,12,34])
print(np.vstack((arr1,arr2)))#Vertically Stack
print(np.hstack((arr1,arr2)))#Horizontally Stack
#Splitting np.split() equal np.hsplit(),np.vsplit()
arr=np.array([12,34,56,78])
print(np.split(arr,2))
# Broadcasting ka matlab hai different sizes ke arrays par arithmetic operations perform karna bina manually loops likhe.Vectorization ka matlab hai operations ko poore array par ek saath perform karna instead of using loops.
prices = [100,200,400]
discount =  10 #10%discount
final_prices = []
for price in prices:
    discounted_price=price-(price*discount/100)
    final_prices.append(discounted_price)
print(final_prices)
#Done this with the help of vectorization
prices = np.array([100,200,300,700])
discount=10 #This is scalar value(means single value)
final_prices = prices - (prices * discount/100)
print(final_prices)
#how numpy handles  different different shapes of the array
#mainly Broadcasting has three most imp rules first is matching dimension second is expanding second elements like this [1,2,3] + 10 so it will be [11,12,13] and the third command is  incomapatible shapes kai agr shapes match nai ho rhy tu wo expand nai kry gha like this [1,2,3]+[1,2] so their shapes not matching and it thorws the error
#Broadcasting with single array
arr=np.array([23,56,90,72])
result=arr*2
print(result)
#Broadcasting with 1d array and 2d array
matrix=np.array([[1,2,3],[4,5,6]])# 2*3  matrix
vector=np.array([10,20,30])#1d array
result=matrix+vector
print(result)
#Eg 3 of when error throws
""" arr1=np.array([[1,2,3],[4,5,6]])
ar2=np.array([1,2])#only 2 elements reamining
result=arr1+arr2
print(result) """
#Vectorization means aik entire array pr aik hi baar mai operations perform krna bina loops ko use kiye but ye list method python mai bht slow hai
#this is slow method approach
list1=[1,2,3]
list2=[4,5,6]
result=[x+y for x,y in zip(list1,list2)]
print(result)
#then we did fast method approach
arr1=np.array([23,45,90])
arr2=np.array([20,4,89])
print(arr1+arr2)
#Same method for vector multiplication

arr1=np.array([23,45,90])
arr2=np.array([20,4,89])
print(arr1+arr2 * 3)
#The summary is broadcasting means expanding the smaller values into longer values faster than loops it used to expand the 1d into 2d  vectorization means kai entire array pr hi aik baar operations perform kr dena 100 times faster than loop it used on matrixes