import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#events = pd.read_csv("https://cernbox.cern.ch/index.php/s/5n2wG7OD7a0wYXX/download")
#events.head()

datos = np.genfromtxt("https://cernbox.cern.ch/index.php/s/5n2wG7OD7a0wYXX/download", delimiter=",",
                      names=["px","py","pz","E"])
p_t = np.sqrt((datos["px"]**2)+(datos["py"]**2))

#plt.hist(p_t)

a = len(datos)
b=int((a+1)/2)
#print(len(datos))

"""
En las siguientes lineas esta el codigo donde se crea una matriz
con los datos por evento de los momentos y la energia
su estrucutra es:
evento px_1 py_1 pz_1 E_1 px_2 py_2 pz_2 E_2
Con 1 correspondiente al muon negativo y 2 el positivo
"""
H = []
j = []
L = []
M2 = []
for i in range(b):
    j = (i,datos[i*2][0],datos[i*2][1],datos[i*2][2],datos[i*2][3],
        datos[i*2+1][0],datos[i*2+1][1],datos[i*2+1][2],datos[i*2+1][3])
    H.append(j)
    E2 = (H[i][4]+H[i][8])**2
    P2 = (H[i][1]+H[i][5])**2 + (H[i][2]+H[i][6])**2 +(H[i][3]+H[i][7])**2
    L = E2 - P2
    M2.append(L)

print(len(H))
#print(H[500][2])

# np.savetxt("Hcito.txt", H, 
#             fmt=["%.0f","%.5f","%.5f","%.5f","%.5f","%.5f","%.5f","%.5f","%.5f"],
#             header="event  px1  py1  pz1  E1  px2 py2  pz2  E2")

print(M2[0])

plt.hist(np.sqrt(M2), color=(0.4,0.9,0.4))
