import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math as math
from scipy.stats import gaussian_kde

file_path = "C:\\Users\\argaf\\Downloads\\Produksi Buah–Buahan dan Sayuran Tahunan Menurut Jenis Tanaman di Provinsi DKI Jakarta (kuintal), 2017.csv"

data = pd.read_csv(file_path, skiprows=3)

# 2️⃣ Ganti nama kolom agar mudah digunakan
data.columns = ['Tanaman', 'Produksi']

# 3️⃣ Pastikan kolom produksi berupa angka
data['Produksi'] = pd.to_numeric(data['Produksi'], errors='coerce')

# 4️⃣ Hapus nilai kosong (NaN)
data = data.dropna(subset=['Produksi'])

#Hanya kurang dari 10000
# data = data[(data['Produksi'] <= 10000) & (data['Produksi'] != 0)]

# 5️⃣ Ambil nilai produksi
values = data['Produksi'].to_numpy()

# 6️⃣ Tentukan batas interval bins sesuai sketsa (0-350.000 dengan interval 50.000)
bins = np.arange(0, 70000, 1000)

# Hitung MEAN,MEDIAN,MODUS
mean_produksi = data['Produksi'].mean()
median_produksi = data['Produksi'].median()
#Modus nya masih PR (dapet 2017)
modus_produksi = data['Produksi'].mode()[0]  # ambil nilai pertama jika ada lebih dari satu modus
variance_produksi = data['Produksi'].var(ddof=1)
stddeviasi_produksi = math.sqrt(variance_produksi)


# Cetak hasil MEAN,MEDIAN,MODUS
print(f"Mean   : {mean_produksi:.2f}")
print(f"Median : {median_produksi:.2f}")
print(f"Modus  : {modus_produksi}")
print(f"Variance : {variance_produksi:.2f}")
print(f"Standar Deviasi : {stddeviasi_produksi:.2f}")

# 7️⃣ Buat histogram
plt.hist(values, bins=bins, color='skyblue', edgecolor='black')

plt.axvline(mean_produksi, color='red', linestyle='--', label=f'Mean')
plt.axvline(median_produksi, color='green', linestyle='--', label=f'Median')
plt.axvline(modus_produksi, color='orange', linestyle='--', label=f'Mode')
# garis kontinu
# plt.plot(x_grid, kde_values, color="blue", linewidth=2, label="Kurva Kontinu")


# 8️⃣ Tambahkan judul dan label sumbu
plt.title("Distribusi Produksi Buah & Sayuran DKI Jakarta (2017)")
plt.xlabel("Produksi (kuintal)")
plt.ylabel("Frekuensi")

# 9️⃣ Atur tampilan sumbu X sesuai interval
plt.xticks(np.arange(0, 70001, 10000))  # label setiap 10.000
plt.tick_params(axis='x', rotation=45)

plt.legend()
# 10️⃣ Tampilkan grid

# 11️⃣ Tampilkan hasil
plt.show()

#ada outliers (data terisolasi)
#unimodal di awal
#skewer positively
