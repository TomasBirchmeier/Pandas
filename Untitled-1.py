print("hola mundo")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import os

os.remove('.git/index.lock')
from matplotlib import rcParams
rcParams['font.family'] = 'Arial Unicode MS'
data_filename = 'C:\\Users\\birch\\Downloads\\Advertising.csv'
df = pd.read_csv(data_filename)
print(df.head())
df_7 = df.head(7)
print(df_7)
##Preparar regresion##
X = df['TV'].values
y = df['Sales'].values
A = np.vstack([X, np.ones(len(X))]).T
m, c = np.linalg.lstsq(A, y, rcond=None)[0]
x1 = np.linspace(0, 300, 500)  # Rango para la predicción
y_pred = m * x1 + c  
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', label='Datos reales')
plt.plot(x1, y_pred, color='red', label='Línea de regresión')
plt.xlabel('Gasto en TV')
plt.ylabel('Ventas')
plt.title('Regresión Lineal: Gasto en TV vs Ventas')
plt.legend()
plt.grid(True)
plt.show()

###Grafico de dispersion##
plt.scatter(df['TV'], df['Sales'], color='blue', marker='o', s=10)
plt.title('Regresion TV vs Sales')
plt.xlabel('Inversion en TV')
plt.ylabel('Ventas')
plt.show()
