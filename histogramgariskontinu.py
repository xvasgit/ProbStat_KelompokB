import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

#SESUAIKAN DENGAN FILE PATHNYA (DOWNLOAD DULU CSV NYA)
file_path = "C:\\Users\\<?>\\Downloads\\Produksi Buah–Buahan dan Sayuran Tahunan Menurut Jenis Tanaman di Provinsi DKI Jakarta (kuintal), 2017.csv"


data = pd.read_csv(file_path, header=None, names=["Tanaman", "Produksi"], skip_blank_lines=True, skiprows=3)
data = data[~data["Tanaman"].str.contains("Buah|Sayuran|Jenis", na=False)]
data = data[~data["Produksi"].isin(["-", "–", None, np.nan])]
data["Produksi"] = pd.to_numeric(data["Produksi"], errors="coerce")
data = data.dropna(subset=["Produksi"])

values = data["Produksi"].to_numpy()

bins = np.arange(0, 70001, 10000)
freq, bin_edges = np.histogram(values, bins=bins)


mean_produksi = data['Produksi'].mean()
median_produksi = data['Produksi'].median()
modus_produksi = data['Produksi'].mode()[0]

bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

x_smooth = np.linspace(bin_centers.min(), bin_centers.max(), 500)
spline = make_interp_spline(bin_centers, freq, k=3)
y_smooth = spline(x_smooth)

plt.figure(figsize=(8, 5))
plt.plot(x_smooth, y_smooth, color="blue", linewidth=2.5, label="Kurva Spline Frekuensi")
plt.scatter(bin_centers, freq, color="red", zorder=5, label="Titik Frekuensi Asli")

plt.axvline(mean_produksi, color='red', linestyle='--', label=f'Mean')
plt.axvline(median_produksi, color='green', linestyle='--', label=f'Median')
plt.axvline(modus_produksi, color='orange', linestyle='--', label=f'Mode')

plt.title("Kurva Spline Distribusi Produksi Buah & Sayuran DKI Jakarta (2017)")
plt.xlabel("Produksi (kuintal)")
plt.ylabel("Frekuensi")

plt.xticks(np.arange(0, 70001, 10000))
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()
