
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import os
import glob

path = os.getcwd()
files=sorted(glob.glob(path+"\*.csv"), key=os.path.getmtime)

amplitudes=np.zeros(25)
frequencias=np.arange(1,26)
contador=0

for file in files:
    teste=pd.read_csv(file, header=None) 
    R=teste.loc[:,1]
    Xl=teste.loc[:,2]
    max_R=max(R)
    min_R=min(R)
    max_Xl=max(Xl)
    min_Xl=min(Xl)
    ampl_R=max_R-min_R;#Amplitude
    ampl_Xl=max_Xl-min_Xl;#Amplitude Xl
    Z=(ampl_R**2+ampl_Xl**2)**0.5;#|Z|
    amplitudes[contador]=Z
    contador+=1

#Plotagem das amplitudes maximas em funcao das frequencias

plt.plot(frequencias,amplitudes);
plt.title ('freq. vs |Z|')
plt.xlabel ('Frequência (Hz)')
plt.ylabel ('Amplitude |Z|')
plt.show()


data_frequencia_10 = pd.read_csv('var_peq_10.csv',header=None);#Importa os dados da frequencia mais indicada para inspecao

t=data_frequencia_10.iloc[:,0]
R=data_frequencia_10.iloc[:,1]
Xl=data_frequencia_10.iloc[:,2]

# Plotagem R vs XL


plt.plot(R,Xl);
plt.title ('Plano de impedância')
plt.xlabel ('Restistência (R)')
plt.ylabel ('Reatância indutiva (Xl)')
plt.show()
# Plotagem R vs t

plt.plot(t,R);
plt.title ('Gráfico R versus Tempo')
plt.xlabel ('Tempo')
plt.ylabel ('Resistência (R)')
plt.show()

# Plotagem XL vs t. 

plt.plot(t,Xl);
plt.title ('Gráfico Xl versus Tempo')
plt.xlabel ('Tempo')
plt.ylabel ('Reatância indutiva (Xl)')
plt.show()    



