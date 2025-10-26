import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math as math
from scipy.stats import gaussian_kde

#SESUAIKAN DENGAN FILE PATHNYA (DOWNLOAD DULU CSV NYA)
file_path = "C:\\Users\\<?>\\Downloads\\Produksi Buah–Buahan dan Sayuran Tahunan Menurut Jenis Tanaman di Provinsi DKI Jakarta (kuintal), 2017.csv"

data = pd.read_csv(file_path, skiprows=3)
data.columns = ['Tanaman', 'Produksi']
data['Produksi'] = pd.to_numeric(data['Produksi'], errors='coerce')
data = data.dropna(subset=['Produksi'])

values = data['Produksi'].to_numpy()

bins = np.arange(0, 70000, 1000)

mean_produksi = data['Produksi'].mean()
median_produksi = data['Produksi'].median()
modus_produksi = data['Produksi'].mode()[0]
variance_produksi = data['Produksi'].var()
stddeviasi_produksi = math.sqrt(variance_produksi)

print(f"Mean   : {mean_produksi:.2f}")
print(f"Median : {median_produksi:.2f}")
print(f"Modus  : {modus_produksi}")
print(f"Variance : {variance_produksi:.2f}")
print(f"Standar Deviasi : {stddeviasi_produksi:.2f}")

plt.hist(values, bins=bins, color='skyblue', edgecolor='black')

plt.axvline(mean_produksi, color='red', linestyle='--', label=f'Mean')
plt.axvline(median_produksi, color='green', linestyle='--', label=f'Median')
plt.axvline(modus_produksi, color='orange', linestyle='--', label=f'Mode')

plt.title("Distribusi Produksi Buah & Sayuran DKI Jakarta (2017)")
plt.xlabel("Produksi (kuintal)")
plt.ylabel("Frekuensi")

plt.xticks(np.arange(0, 70001, 10000)) 
plt.tick_params(axis='x', rotation=45)

plt.legend()
plt.show()


