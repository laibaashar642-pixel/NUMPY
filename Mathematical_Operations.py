#We can perform easily fast operations on arrays +,-*,/
import numpy as np
arr=np.array([32,89,90,12])
print(arr+5)
print(arr*4)
print(arr**4)
print(arr/4)
#Aggregation function means summarizing the actual data
print(np.sum(arr))
print(np.average(arr))
print(np.mean(arr))
print(np.min(arr))
print(np.max(arr))
print(np.std(arr))
print(np.var(arr))