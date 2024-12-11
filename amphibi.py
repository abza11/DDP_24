from animal import Animal 

class Amphibi(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jenis_air, bernafas):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis_air = jenis_air
        self.bernafas = bernafas
        
    def info_amphibi(self):
        super().info_animal(),
        print ("jenis air \t\t\t:",self.jenis_air,
               "\nbernapas \t\t\t:",self.bernafas)
        
katak= Amphibi ("katak","serangga","dua alam","bertelur","tawar","kulit dan paru-paru")
katak.info_amphibi()

print ("==================================================================================")
salamander = Amphibi("salamander","cacing","dua alam","bertelur","tawar","kulit,ingsang dan paru-paru")
salamander.info_amphibi()

print ("==================================================================================")
caecallian_cacing = Amphibi("caecallian_cacing","serangga","dua alam","bertelur","tawar","ingsang,paru-paru dan kulit")
caecallian_cacing.info_amphibi()
        