class Animal:
    def __init__(self, name, makanan, hidup, berkembang_biak):
        self.name = name
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak

    def info_animal(self):
        print("Nama Hewan\t\t\t:", self.name,
              "\nMakanan\t\t\t\t:", self.makanan,
              "\nHidup\t\t\t\t:", self.hidup,
              "\nBerkembang Biak\t\t\t:", self.berkembang_biak)


#hewan = Animal('Buaya', 'Kebab', 'Rawa Buntu', 'Beranak Pinak')
#hewan.info_animal()