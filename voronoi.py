import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.cm as cm

seed = np.random.randint(0, 10_000_000)
seed = 3770726
np.random.seed(seed)


# Jumlah titik random
num_points = 50
points = np.random.rand(num_points, 2)

# Buat Voronoi diagram
vor = Voronoi(points)

# Warna gradien (cmap bisa diganti: plasma, viridis, coolwarm, magma, dll)
cmap = cm.get_cmap("turbo")  # bisa coba "viridis", "magma", "cividis"

#fig, ax = plt.subplots(figsize=(8, 8))
fig, ax = plt.subplots(figsize=(60, 60), dpi=100)  # 60 inch * 100 dpi = 6000 px

### Loop tiap region Voronoi
for region in vor.regions:
    if not region or -1 in region:
        continue
    polygon = [vor.vertices[i] for i in region]

    # Hitung centroid region
    poly_arr = np.array(polygon)
    centroid = poly_arr.mean(axis=0)

    # Warna berdasarkan posisi centroid dengan sedikit noise
    base_value = (centroid[0] + centroid[1]) / 2
    noise = np.random.uniform(-0.05, 0.05)  # bikin variasi halus
    color_value = np.clip(base_value + noise, 0, 1)

    ax.fill(*zip(*polygon), color=cmap(color_value), alpha=0.85)

# Tambahkan titik pusat
ax.plot(points[:, 0], points[:, 1], "o", color="white", markersize=4)

# Hilangkan axis biar lebih clean
ax.set_xticks([])
ax.set_yticks([])
ax.axis("off")

plt.tight_layout()
plt.savefig(f"{seed}_{num_points}_voronoi_gradient.png", dpi=100, bbox_inches="tight")

print(f"Seed yang dipakai: {seed}")
