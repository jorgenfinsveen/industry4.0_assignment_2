
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

new_column_names = ['Roughness', 'Sensor_1', 'Sensor_2', 'Sensor_3', 'Sensor_4', 'Sensor_5']

df = pd.read_csv('Bok2.csv', header=None, names=new_column_names, sep=';')
print(df)

X = df['Roughness'].values.astype(int)
S1 = df['Sensor_1'].values.astype(float)
S2 = df['Sensor_2'].values.astype(float)
S3 = df['Sensor_3'].values.astype(float)
S4 = df['Sensor_4'].values.astype(float)
S5 = df['Sensor_5'].values.astype(float)

plt.figure(figsize=(20, 6))
plt.plot(X, S1, label='Sensor 1', linestyle='--', marker='o', color='blue')
plt.plot(X, S2, label='Sensor 2', linestyle='--', marker='o', color='red')
plt.plot(X, S3, label='Sensor 3', linestyle='--', marker='o', color='green')
plt.plot(X, S4, label='Sensor 4', linestyle='--', marker='o', color='orange')
plt.plot(X, S5, label='Sensor 5', linestyle='--', marker='o', color='purple')

plt.xlabel('Roughness [µm]')
plt.ylabel('Temperature [K]')
plt.title('Impact of roughness on the steady state temperatures')
plt.ylim(500, 600)
plt.xlim(20, 160)

plt.legend(['Sensor 1', 'Sensor 2', 'Sensor 3', 'Sensor 4', 'Sensor 5'])
plt.grid()
plt.show()