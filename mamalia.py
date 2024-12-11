from animal import Animal

class Mamalia(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jenis_darah, jenis_kulit):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis_darah = jenis_darah
        self.jenis_kulit = jenis_kulit
        
        
    def info_mamalia(self):
        super().info_animal()
        print("Jenis Darah \t\t\t:" , self.jenis_darah,
              "\nJenis Kulit \t\t\t:" , self.jenis_kulit)
        
singa = Mamalia ("singa", "Daging", "Darat","melahirkan", "darah panas","berbulu")
singa.info_mamalia()

print("========================================================================")

kucing = Mamalia("kucing", "daging", 'darat', 'melahirkan', 'darah panas', 'berbulu')
kucing.info_mamalia()
        
print("========================================================================")
monyet = Mamalia("monyet", "daging", 'udara', 'melahirkan', 'darah panas', 'berbulu')
monyet.info_mamalia()