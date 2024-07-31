print("hola mundo")
import pandas as pd
import matplotlib.pyplot as plt
import os
from matplotlib import rcParams
rcParams['font.family'] = 'Arial Unicode MS'
data_filename = 'C:\\Users\\birch\\Downloads\\Advertising.csv'
df = pd.read_csv(data_filename)
print(df.head())
df_7 = df.head(7)
print(df_7)
plt.scatter(df_7['TV'], df_7['Sales'], color='blue', marker='o', s=100)
plt.title('Regresion TV vs Sales')
plt.xlabel('Inversion en TV')
plt.ylabel('Ventas')
plt.show()