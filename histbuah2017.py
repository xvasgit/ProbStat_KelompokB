import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import gaussian_kde

#SESUAIKAN DENGAN FILE PATHNYA (DOWNLOAD DULU CSV NYA)
file_path = "C:\\Users\\<?>\\Downloads\\Produksi Buah–Buahan dan Sayuran Tahunan Menurut Jenis Tanaman di Provinsi DKI Jakarta (kuintal), 2017.csv"

data = pd.read_csv(file_path, header=None, names=["Tanaman", "Produksi"], skip_blank_lines=True,skiprows=3)
data = data[~data["Tanaman"].str.contains("Buah|Sayuran|Jenis", na=False)]
data = data[~data["Produksi"].isin(["-", "–", None, np.nan])]

data['Produksi'] = pd.to_numeric(data['Produksi'], errors='coerce')
data = data.dropna(subset=['Produksi'])
values = data['Produksi'].to_numpy()

bins = np.arange(0, 70001, 10000)

mean_produksi = data['Produksi'].mean()
median_produksi = data['Produksi'].median()
modus_produksi = data['Produksi'].mode()[0]

print(f"Mean   : {mean_produksi:.2f}")
print(f"Median : {median_produksi:.2f}")
print(f"Modus  : {modus_produksi}")

counts, bin_edges = np.histogram(values, bins=bins)
plt.hist(values, bins=bins, color='skyblue', edgecolor='black', alpha=0.7, label="Histogram")

kde = gaussian_kde(values)
bin_width = bins[1] - bins[0]
x_grid = np.linspace(min(values), max(values), 1000)
kde_density = kde(x_grid)

kde_frequency = kde_density * len(values) * bin_width

max_hist_height = np.max(counts)

max_kde_height = np.max(kde_frequency)

if max_kde_height > 0:
    scale_factor = max_hist_height / max_kde_height
    kde_frequency_scaled = kde_frequency * scale_factor
else:
    kde_frequency_scaled = kde_frequency

plt.plot(x_grid, kde_frequency_scaled, color="blue", linewidth=2, label="Kurva Kontinu (KDE)")


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
