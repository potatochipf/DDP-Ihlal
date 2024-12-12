from Animal import Animal

class Amphibi(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, habitat, cara_berkembang_biak):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.habitat = habitat
        self.cara_berkembang_biak = cara_berkembang_biak

    def display_amphibi_info(self):
        self.display_info()
        print(f"Habitat: {self.habitat}")
        print(f"Cara Berkembang Biak: {self.cara_berkembang_biak}")

print("=============OBJECT 1====================")
kodok = Amphibi("Kodok", "Serangga", "Air dan Darat", "Berkembang Biak", "Hutan Hujan", "Bertelur")
kodok.display_amphibi_info()
print("==============OBJECT 2===================")
katak = Amphibi("Katak", "Serangga", "Air dan Darat", "Berkembang Biak", "Hutan Hujan", "Bertelur")
katak.display_amphibi_info()
print("==============OBJECT 3==================")
bufo = Amphibi("Bufo", "Serangga", "Air dan Darat", "Berkembang Biak", "Hutan Hujan", "Bertelur")
bufo.display_amphibi_info()
print("=================================")