#Agr hum nay missing values ko handle krna na seekha tu hamay machine learning mai models ko train krny mai mushkil hoey ghi tu numpy iskay liye hamay builtin functions provide krta hai np.insan(detact missing values) np.nan_to_num() jo nan sai values mili hai usko replace krna chaty ho kisi number sai tu then we use and the third is np.isinf() to detect infinity values 
#First is nan(not a number) ye tb use hogha jb apky cell mai data missing hongha aur value nai hoghi 0/0 krna hogha and it always return boolean value true or false
import numpy as np
arr=np.array([23,np.nan,78,56,np.nan])
print(np.isnan(arr))#Interview ka imp sawal kai kia ap np.nan ki values ko apas mai compare kr skty hokay nai so nai krskty
print(np.nan==np.nan)#We can't compare it directly
#Agr apky dataset mai apko milgyi blank value tu usko replace kesy kry gai aur in nan values ko replace kun krna hai kunnkay baaz operations jb hum perform krty hai tu nan ki values ki wja sai operations complete or shi perform nai hosky gai aur jo machine learning kai models hoty hai wo in nan ki values ko process nai kr skty
#np.nan_to_num()(array,nan=value)default value hoti hai hamesha 0
arr=np.array([23,np.nan,78,56,np.nan])
cleaned_arr=np.nan_to_num(arr)
print(cleaned_arr)
cleaned_arr=np.nan_to_num(arr,nan=100)#If you don't want default value
print(cleaned_arr)
#And the next is for infinite values np.isinf() aesa no jo python ki no limit ko exceed krti hai hum usko infinity karrar de dety hai

arr=np.array([23,np.nan,78,56,np.inf,78,90,-np.inf])
print(np.isinf(arr))
#Aur agr is infinite no ko replace krna hai finite no sai how can we do this
arr=np.array([23,np.inf,78,56,-np.inf,45])
print(np.isinf(arr))
cleaned_arr=np.nan_to_num(arr,posinf=1000,neginf=1000)
print(cleaned_arr)