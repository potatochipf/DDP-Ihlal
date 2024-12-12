from Animal import Animal

class Mamalia(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jenis_susu, cara_berkembang_biak):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis_susu = jenis_susu
        self.cara_berkembang_biak = cara_berkembang_biak

    def display_mamalia_info(self):
        self.display_info()
        print(f"Jenis Susu: {self.jenis_susu}")
        print(f"Cara Berkembang Biak: {self.cara_berkembang_biak}")
print("=================================")
kucing = Mamalia("Kucing", "Daging", "Daratan", "Berkembang Biak", "Susu Kucing", "Melahirkan")
kucing.display_mamalia_info()
print("=================================")
anjing = Mamalia("Anjing", "Daging", "Daratan", "Berkembang Biak", "Susu Anjing", "Melahirkan")
anjing.display_mamalia_info()
print("=================================")
gajah = Mamalia("Gajah", "Tumbuhan", "Daratan", "Berkembang Biak", "Susu Gajah", "Melahirkan")
gajah.display_mamalia_info()
print("=================================")