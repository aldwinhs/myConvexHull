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

input = int(input("Pilihan: "))
while (not(input == 1 or input == 2 or input == 3)):
    print("Masukan salah")
    input = int(input("Pilihan: "))

if(input==1):
    data = datasets.load_iris() 
elif(input==2):
    data = datasets.load_wine()
elif(input==3):
    data = datasets.load_breast_cancer

#create a DataFrame 
df = pd.DataFrame(data.data, columns=data.feature_names) 
df['Target'] = pd.DataFrame(data.target) 

print("Atributes:")
for i in range(len(data.feature_names)):
    print(i+1, data.feature_names[i])

inputx = int(input("X: "))
inputy = int(input("Y: "))

plt.figure(figsize = (10, 6))
colors = ['b','r','g']
plt.title(data.feature_names[inputx-1]+" vs "+data.feature_names[inputy-1])
plt.xlabel(data.feature_names[inputx-1])
plt.ylabel(data.feature_names[inputy-1])
for i in range(len(data.target_names)):
    bucket = df[df['Target'] == i]
    bucket = bucket.iloc[:,[inputx-1,inputy-1]].values
    bucket = bucket.tolist() #membuat numpy array menjadi list
    hull = myConvexHull.myConvexHull(bucket) 
    hull = np.asarray(hull) #membuat list menjadi numpy array
    bucket = np.asarray(bucket)
    plt.scatter(bucket[:, 0], bucket[:, 1], label=data.target_names[i])
    for simplex in hull:
        plt.plot(bucket[simplex, 0], bucket[simplex, 1], colors[i])
plt.legend()
plt.show()