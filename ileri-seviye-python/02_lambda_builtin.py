"""
Lambda, Map ve Fonksiyon Kullanımı Örnekleri
---------------------------------------------
Bu dosya, lambda ifadeleri, map fonksiyonu ve fonksiyonların dinamik kullanımına dair
örnekleri içermektedir.
"""

#---------------------------------------#
# Lambda fonksiyonlarının temel kullanımı
#---------------------------------------#

def kare_al(a):
    """Girilen sayının karesini döndürür."""
    return a ** 2

print(kare_al(5))

# Lambda fonksiyonu doğrudan çağrılıyor
sonuc = (lambda a: a ** 2)(4)
print(f"Lambda => {sonuc}")

# Lambda fonksiyonu bir değişkene atanabilir
kare_al_fonksiyonu = lambda a: a ** 2
sonuc = kare_al_fonksiyonu(10)
print(f"Lambda => {sonuc}")

# Birden fazla parametre alan lambda
toplama = lambda a, b, c: a + b + c
sonuc = toplama(1, 2, 3)
print(f"Toplama sonucu = {sonuc}")

print("#-------------------------------#")

#---------------------------------------#
# Lambda ve fonksiyonun birlikte kullanımı
#---------------------------------------#

def my_func(n):
    """Girilen katsayıya göre çarpan döndüren fonksiyon."""
    return lambda a: a * n

# Fonksiyonun doğrudan çağrılması
sonuc = my_func(2)(3)
print(f"Fonksiyon ve lambda aynı anda kullanımı : {sonuc}")

# Farklı katsayılara sahip fonksiyonlar oluşturma
carpma2 = my_func(2)
carpma3 = my_func(3)
carpma4 = my_func(4)

print(carpma2(3))  # 6
print(carpma3(5))  # 15
print(carpma4(6))  # 24

print("#-------------------------------#")

#---------------------------------------#
# Map Fonksiyonu Kullanımı
#---------------------------------------#

sayilar = [1, 2, 3, 4, 5]
sayilar_str = ["1", "2", "3", "4", "5"]
isimler = ["ali", "veli", "hasan", "ayşe", "zeynep"]
kullanicilar = [
    {"ad": "ali", "soyad": "yılmaz"},
    {"ad": "ahmet", "soyad": "cengiz"}
]

# map() ile liste elemanlarını dönüştürme
# kare_al fonksiyonunu her elemana uygular
sonuc = list(map(kare_al, sayilar))
print(f"Kareler (fonksiyon): {sonuc}")

# Aynı işlem lambda ile
sonuc = list(map(lambda sayi: sayi ** 2, sayilar))
print(f"Kareler (lambda): {sonuc}")

# String -> int dönüşümü
print(f"sayilar_str = {sayilar_str}")
s
