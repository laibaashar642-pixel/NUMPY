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
