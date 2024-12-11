from animal import Animal 

class Carnivora(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, habitat, sistem_pencernaan):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.habitat = habitat
        self.sistem_pencernaan= sistem_pencernaan
        
    def info_carnivora(self):
        super().info_animal(),
        print ("habitat \t\t\t:",self.habitat,
               "\nsistem percernaan\t\t:",self.sistem_pencernaan)
        
jaguar= Carnivora ("jaguar","daging(hasil dari buruannya seperti kudanil,rusa dll)","Darat","melahirkan","hutan tropis,savana,sungai dan perairan","Sederhana dan efisien untuk memproses daging")
jaguar.info_carnivora()

print ("==================================================================================")
serigala= Carnivora ("serigala","daging(hewan buruan seperti rusa dll)","darat dan berkelompok","melahirkan",'hutan,padang rumput,dan daerah dingin',"sistem pencernaan dengan usus pendek sehingga memudahkan untuk mencerna daging")
serigala.info_carnivora()

print ("==================================================================================")
anjing_laut= Carnivora ("anjing_laut","daging(seperti udang,ikan,cumi-cumi dll)","air laut",'melahirkan','perairan laut dan tempat favoritnya seperti pantai berbatu,es terapung,dan pulau kecil','usus yang pendek memudahkan untuk mencerna daging')
anjing_laut.info_carnivora()
        