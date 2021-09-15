"""
Created on Wed Sep 15 12:31:02 2021

@author: AlejRam
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

events = pd.read_csv("C:/Users/1087066173/.spyder-py3/eventos_pxpypzE.csv")
events.head()

datos = np.genfromtxt("C:/Users/1087066173/.spyder-py3/eventos_pxpypzE.csv", delimiter=",",
                      names=["px", "py", "pz", "E"])

a = len(events)
b=int((a+1)/2)
print(len(datos))
H=[]
j=[]
for i in range(b):
    j=(i,datos[i*2][0],datos[i*2][1],datos[i*2][2],datos[i*2][3],
        datos[i*2+1][0],datos[i*2+1][1],datos[i*2+1][2],datos[i*2+1][3])
    H.append(j)

# for i in range(5):
#     j=(i,datos[i*2][0],datos[i*2+1][0])
print(len(H))
print(H[500][2])

np.savetxt("Hcito.txt", H, 
            fmt=["%.0f","%.5f","%.5f","%.5f","%.5f","%.5f","%.5f","%.5f","%.5f"],
            header="event  px1  py1  pz1  E1  px2 py2  pz2  E2")


#plt.plot(datos["px"])
