from Animal import Animal

class Carnivora(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jenis_daging, cara_berburu):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis_daging = jenis_daging
        self.cara_berburu = cara_berburu

    def display_carnivora_info(self):
        self.display_info()
        print(f"Jenis Daging: {self.jenis_daging}")
        print(f"Cara Berburu: {self.cara_berburu}")

print("=================================")
singa = Carnivora("Singa", "Daging", "Daratan", "Berkembang Biak", "Daging Mamalia", "Berburu dengan Kelompok")
singa.display_carnivora_info()
print("=================================")
harimau = Carnivora("Harimau", "Daging", "Daratan", "Berkembang Biak", "Daging Mamalia", "Berburu Sendirian")
harimau.display_carnivora_info()
print("=================================")
anjing = Carnivora("anjing", "Daging", "Daratan", "Berkembang Biak", "Daging Mamalia", "Berburu Sendirian")
anjing.display_carnivora_info()
print("=================================")



























 

 