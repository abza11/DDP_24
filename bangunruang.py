import math

def l_balok(p, l, t):
    hitung = 2 * (p * l) + (p * t) + (l * t)
    print(f'luas balok adalah {hitung} cm2')
    
def l_kubus(sisi):
    hitung = 6 * (sisi * sisi)
    print(f'luas kubus adalah {hitung} cm2')
    
def l_tabung(jari2_alas, tinggi):
    hitung_l_selimut = 2 * 3.14 * jari2_alas * tinggi
    hitung_l_kedua_alas = 2 * 3.14 * jari2_alas * jari2_alas
    hitung_l_permukaan_total = hitung_l_selimut + hitung_l_kedua_alas
    print(f'luas tabung adalah {hitung_l_permukaan_total} cm2')
    
def l_prisma_segitiga(alas, tinggi_segitiga, tinggi_prisma, sisi1, sisi2, sisi3):
    hitung_l_alas_segitiga = 1/2 * alas * tinggi_segitiga
    hitung_l_kedua_alas = 2 * hitung_l_alas_segitiga
    hitung_l_sisi_tegak = (sisi1 * tinggi_prisma) + (sisi2 * tinggi_prisma) + (sisi3 * tinggi_prisma)
    hitung_luas_total = hitung_l_kedua_alas + hitung_l_sisi_tegak
    print(f'luas prisma segitiga adalah {hitung_luas_total} cm2')
    
def l_limas_segiempat(panjang, lebar, tinggi_sisi):
    hitung_l_alas = panjang * lebar
    hitung_l_sisi_panjang = 1/2 * panjang * tinggi_sisi
    hitung_l_sisi_lebar = 1/2 * lebar * tinggi_sisi
    hitung_l_luas_sisi_tegak = 2 * (hitung_l_sisi_panjang + hitung_l_sisi_lebar)
    hitung_l_total = hitung_l_alas + hitung_l_luas_sisi_tegak
    print(f'luas limas segiempat adalah {hitung_l_total} cm2')