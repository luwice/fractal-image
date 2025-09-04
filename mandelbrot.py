import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk menghitung nilai mandelbrot untuk setiap titik
def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

# Mengatur ukuran gambar dan batas bidang kompleks
width, height = 800, 800
re_min, re_max = -2.0, 1.0
im_min, im_max = -1.5, 1.5

# Membuat grid kompleks
real = np.linspace(re_min, re_max, width)
imag = np.linspace(im_min, im_max, height)
X, Y = np.meshgrid(real, imag)
C = X + 1j * Y

# Iterasi untuk setiap titik pada grid
max_iter = 1000
mandelbrot_set = np.zeros(C.shape, dtype=int)

for i in range(width):
    for j in range(height):
        mandelbrot_set[j, i] = mandelbrot(C[j, i], max_iter)

# Plot gambar fractal
plt.figure(figsize=(10, 10))
plt.imshow(mandelbrot_set, extent=[re_min, re_max, im_min, im_max], cmap='twilight_shifted')
plt.colorbar()
plt.title('Mandelbrot Set')
plt.show()
