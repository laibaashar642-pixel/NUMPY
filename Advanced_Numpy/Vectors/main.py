#Vectors number ki ek list hai jo kisi bhi cheez ko represent krta hai real life mai agr sochain tu ali pasand krta hai cricket ,football,hockey ko pasand nai krty then yee hamaray pass vector bn gya[1,1,0]
#How can we create vectors in numpy
import numpy as np
#ye ak user ka interest vector hai
ali=np.array([1,1,0,0])
ahmad=np.array([1,1,1,0])
sana=np.array([0,1,0,1])
print(ali)
print(sana)
print(ahmad)
#Vector Operations
#Addition dono  users kai interests ko combine krna
combined=ali+sana
print(combined)
#Scaling (double importance)
print(ali * 2)
#Dot Product(kitny interests match krty hai)
similarity=np.dot(ali,sana)
print(similarity)
#Cosine Similarity It tells how many vectors are similar
def cosine_similarity(a,b):
    dot_product=np.dot(a,b)
    magnitude_a=np.linalg.norm(a)
    magnitude_b=np.linalg.norm(b)
    return dot_product/(magnitude_a*magnitude_b)
print(cosine_similarity(ali,sana))#Boht Similar
print(cosine_similarity(ali,ahmad))#Bilkul Different

#Pandas with vector
import pandas as pd
#Real-World Product Rating as vectors
data={
    'user':['sara','ahmed','ali','zara'],
    'laptop':[5,4,3,2],
    'phone':[8,9,4,3],
    'tablet':[12,34,56,78],

}
df=pd.DataFrame(data)
print(df)
#hr user aik vector hai
ali_vector=df.loc["Ali"].values
sana_vector=df.loc["Sana"].values
ahmad_vector=df.loc["Ahmad"].values
#Ali aur sara ki similar values
sim=cosine_similarity(ali_vector,sana_vector)
print(f"Ali & Sara similarity:{sim:.2f}")
#real Use Ai 