import matplotlib.pyplot as plt
import numpy as np

# Proyek: Membuat dua kurva sederhana untuk perbandingan

# 1. Menyiapkan data
# Membuat 1000 titik data dari -10 sampai 10 untuk sumbu X
x = np.linspace(-10, 10, 1000)

# Kurva 1: Garis lurus (linear) y = 2x + 1
y1 = 2 * x + 1

# Kurva 2: Kurva kuadratik (parabola) y = x^2 - 5
y2 = x**2 - 5

# 2. Membuat plot
# Plot kurva pertama (garis lurus) dengan garis solid dan label
plt.plot(x, y1, label='y = 2x + 1')

# Plot kurva kedua (parabola) dengan garis putus-putus dan label
plt.plot(x, y2, linestyle='--', label='y = x^2 - 5')

# 3. Menambahkan elemen tambahan pada plot
# Memberi judul pada plot
plt.title("Perbandingan Kurva Linear dan Kuadratik")

# Memberi label pada sumbu X
plt.xlabel("Sumbu X")

# Memberi label pada sumbu Y
plt.ylabel("Sumbu Y")

# Menampilkan legenda agar setiap kurva mudah dikenali
plt.legend()

# Menambahkan grid (kotak-kotak) di latar belakang plot
plt.grid(True)

# 4. Menampilkan plot
plt.show()

# PETUNJUK SINTAKS
# --------------------
# - import matplotlib.pyplot as plt: Mengimpor library untuk plotting.
# - import numpy as np: Mengimpor library untuk operasi matematika dan array.
# - np.linspace(start, stop, num): Membuat array dengan 'num' titik yang berjarak sama antara 'start' dan 'stop'.
# - plt.plot(x, y, ...): Fungsi utama untuk menggambar kurva.
# - label='...': Memberi nama pada kurva yang akan muncul di legenda.
# - linestyle='--': Mengubah gaya garis menjadi putus-putus. Gunakan '-' untuk solid, ':' untuk titik, dan '-.' untuk kombinasi.
# - plt.title('...'): Mengatur judul plot.
# - plt.xlabel('...'): Mengatur label sumbu X.
# - plt.ylabel('...'): Mengatur label sumbu Y.
# - plt.legend(): Menampilkan legenda.
# - plt.grid(True): Menampilkan grid.
# - plt.show(): Menampilkan semua plot yang sudah dibuat.