import math

# Deklarasi Fungsi
def l_persegi(sisi):
    hitung = sisi * sisi
    print(f'luas persegi adalah {hitung}')
    
def l_persegi_panjang(p, l):
    hitung = p * l
    print(f'luas persegi panjang adalah {hitung}')
    
def l_segitiga(alas, tinggi):
    hitung = 1/2 * alas * tinggi
    print(f'luas segitiga adalah {hitung}')
    
def l_lingkaran(pi,r):
    hitung = pi * r * r
    print(f'luas lingkaran adalah {hitung}')

def l_jajargenjang(alas,tinggi):
    hitung = alas * tinggi
    print(f'luas jajar genjang adalah {hitung}')