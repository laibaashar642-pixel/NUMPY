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
newarr_2d=np.insert(arr_2d,1,[5,6],axis=0)
print(newarr_2d)