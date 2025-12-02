import tkinter as tk
from tkinter import ttk, messagebox

class Kontak:
    def __init__(self, nama, nomor, kategori):
        self.nama = nama
        self.nomor = nomor
        self.kategori = kategori

    # Method untuk format tampilan teks di layar
    def info_lengkap(self):
        return f"[{self.kategori}] {self.nama} - {self.nomor}"

# --- Class Utama Aplikasi ---
class AplikasiKontak:
    def __init__(self, root):
        self.root = root
        self.root.title("Buku Telepon Digital")
        self.root.geometry("450x500")

        self.database_kontak = [] # List penyimpanan data

        # === BAGIAN INPUT DATA BARU ===
        frame_input = tk.LabelFrame(root, text="Tambah Kontak Baru", padx=10, pady=10)
        frame_input.pack(fill="x", padx=10, pady=5)

        tk.Label(frame_input, text="Nama:").grid(row=0, column=0, sticky="w")
        self.entry_nama = tk.Entry(frame_input, width=30)
        self.entry_nama.grid(row=0, column=1, padx=5, pady=2)

        tk.Label(frame_input, text="Nomor HP:").grid(row=1, column=0, sticky="w")
        self.entry_nomor = tk.Entry(frame_input, width=30)
        self.entry_nomor.grid(row=1, column=1, padx=5, pady=2)

        tk.Label(frame_input, text="Kategori:").grid(row=2, column=0, sticky="w")
        self.combo_kategori = ttk.Combobox(frame_input, values=["Keluarga", "Teman", "Kantor", "Darurat"])
        self.combo_kategori.current(1)
        self.combo_kategori.grid(row=2, column=1, padx=5, pady=2)

        btn_simpan = tk.Button(frame_input, text="Simpan Kontak", command=self.simpan_kontak, bg="#4CAF50", fg="white")
        btn_simpan.grid(row=3, column=1, sticky="e", pady=10)

        # === BAGIAN PENCARIAN & DAFTAR ===
        frame_list = tk.LabelFrame(root, text="Daftar Kontak", padx=10, pady=10)
        frame_list.pack(fill="both", expand=True, padx=10, pady=5)

        # Baris Pencarian
        tk.Label(frame_list, text="Cari Nama:").pack(anchor="w")
        self.entry_cari = tk.Entry(frame_list)
        self.entry_cari.pack(fill="x", pady=2)
        
        # Tombol Cari memicu fungsi update_listbox
        btn_cari = tk.Button(frame_list, text="Filter / Cari", command=self.update_listbox)
        btn_cari.pack(anchor="e", pady=2)

        # Listbox Output
        self.listbox = tk.Listbox(frame_list)
        self.listbox.pack(fill="both", expand=True, pady=5)

    def simpan_kontak(self):
        nama = self.entry_nama.get()
        nomor = self.entry_nomor.get()
        kategori = self.combo_kategori.get()

        if nama == "" or nomor == "":
            messagebox.showwarning("Oops", "Nama dan Nomor tidak boleh kosong!")
            return

        # Buat Objek Baru (OOP)
        kontak_baru = Kontak(nama, nomor, kategori)
        self.database_kontak.append(kontak_baru)

        messagebox.showinfo("Sukses", f"Kontak {nama} berhasil disimpan.")
        
        self.entry_nama.delete(0, tk.END)
        self.entry_nomor.delete(0, tk.END)
        
        self.update_listbox()

    # (LOGIKA PENCARIAN) ---
    def update_listbox(self):
        kata_kunci = self.entry_cari.get().lower()

        self.listbox.delete(0, tk.END)
        for kontak in self.database_kontak:
            
            if kata_kunci in kontak.nama.lower():
                self.listbox.insert(tk.END, kontak.info_lengkap())

if __name__ == "__main__":
    root = tk.Tk()
    app = AplikasiKontak(root)
    root.mainloop()