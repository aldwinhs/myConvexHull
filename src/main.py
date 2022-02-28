
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
import myConvexHull
from sklearn import datasets 


# MAIN
print(
    """
    Visualizer myConvexHull
    Datasets:
    1. iris
    2. wine
    3. breast cancer
    """
)

opsi = int(input("Pilihan: "))
while (not(opsi == 1 or opsi == 2 or opsi == 3)):
    print("Masukan salah")
    opsi = int(input("Pilihan: "))

if(opsi==1):
    data = datasets.load_iris() 
elif(opsi==2):
    data = datasets.load_wine()
elif(opsi==3):
    data = datasets.load_breast_cancer()

#create a DataFrame 
df = pd.DataFrame(data.data, columns=data.feature_names) 
df['Target'] = pd.DataFrame(data.target) 

print("Atributes:")
for i in range(len(data.feature_names)):
    print(i+1, data.feature_names[i])

print()

inputAbsis = int(input("Pilihan X: "))
inputOrdinat = int(input("Pilihan Y: "))

plt.figure(figsize = (10, 6))
colors = ['b','r','g']
plt.title(data.feature_names[inputAbsis-1]+" vs "+data.feature_names[inputOrdinat-1])
plt.xlabel(data.feature_names[inputAbsis-1])
plt.ylabel(data.feature_names[inputOrdinat-1])
for i in range(len(data.target_names)):
    bucket = df[df['Target'] == i]
    bucket = bucket.iloc[:,[inputAbsis-1,inputOrdinat-1]].values
    bucket = bucket.tolist() #membuat numpy array menjadi list
    hull = myConvexHull.myConvexHull(bucket) 
    hull = np.asarray(hull) #membuat list menjadi numpy array
    bucket = np.asarray(bucket)
    plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
    for simplex in hull:
        plt.plot(bucket[simplex, 0], bucket[simplex, 1], colors[i])
plt.legend()
plt.show()