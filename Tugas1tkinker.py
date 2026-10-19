import tkinter as tk

# Membuat jendela
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("400x500")

# Judul aplikasi
judul = tk.Label(
    root,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Arial", 14)
)
judul.pack(pady=10)

# Daftar mata pelajaran
mapel = [
    "Matematika",
    "Bahasa Indonesia",
    "Bahasa Inggris",
    "Fisika",
    "Kimia",
    "Biologi",
    "Ekonomi",
    "Geografi",
    "Sejarah",
    "Informatika"
]

# Membuat input nilai
input_nilai = []

for nama in mapel:
    frame = tk.Frame(root)
    frame.pack(pady=3)

    label = tk.Label(frame, text=nama, width=20, anchor="w")
    label.pack(side="left")

    entry = tk.Entry(frame, width=10)
    entry.pack(side="left")

    input_nilai.append(entry)

# Fungsi tombol prediksi
def hasil_prediksi():
    hasil.config(text="Prodi Pilihan: Teknologi Informasi")

# Tombol prediksi
tombol = tk.Button(
    root,
    text="Hasil Prediksi",
    command=hasil_prediksi
)
tombol.pack(pady=10)

# Menampilkan hasil
hasil = tk.Label(root, text="Hasil Prediksi: -")
hasil.pack()

# Menjalankan aplikasi
root.mainloop()