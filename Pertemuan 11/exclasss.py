#Pendeklarasian Class

class Orang:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat
    #variabel(atribut)

    #fungsi(method)
    def ngomong(self,nama):
        print(f"Saya bernama {self.nama}")

#Pemanggilan objek
supir = Orang("Subhan",19, "Jl. Malang Nengah") #membuat objek supir
supir.nama = "Potatochipf" 
print(supir.nama)
print(supir.umur)
print(supir.alamat)
supir.ngomong()

dokter = Orang()
dokter.sertifikat = "Spesialis Dada"
print(dokter.nama)
print(dokter.sertifikat)


#mahasiswa
mahasiswa = Orang()
mahasiswa.mim = "0110124049"
mahasiswa.prodi = "Teknik Informatika"
print(mahasiswa.nama)
print(mahasiswa.mim)
print(mahasiswa.prodi)

class Mobil:
    #variabel(artibut)
    merk = "Toyota"
    bensin = "Pertalite"
    maju = "Mobil Berjalan"

    def maju(self):
       print("Mobil Berjalan")

kijang = Mobil()
kijang.maju()
