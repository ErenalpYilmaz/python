# Bir listeden başka bir listeye aktarım
iterable = [12,25,43]
liste = []

for i in iterable:
    liste.append(i)
    
# Kısa yol -> item yerine item**2 de yazabilirdim.
liste = [ item for item in iterable]

# Örnek 2
liste2=[]
for i in range(5):
    liste2.append(i)

# Kısa yol -> (ilk item burada listeye atılacak)
liste2 = [item for item in range(5)]

liste2 = [ item**2 for item in range(10)]
print(liste2) 

kurum = "Btk Akademi"

for i in kurum:
    print(i.upper())
    
sonuc = [ i.upper() for i in kurum]
print(f"sonuc: {sonuc}")

#######################################

# Koşullu Yapılar

for i in range(11):
    if i % 2 == 0:
        print(i)

# i-> listeye eklenecek elemanın durumu. i+=2 deseydim her i değerinin 2 fazlasını eklerdi.
# for içindeki i-> range den gelen değer
# range sonrasındaki if te koşul belirtiyor. Eğer i%2==0 ise listeye ekle. 
sonuc = [i for i in range(11) if i%2 == 0]
#Birden fazla if sorgusu olursa başa koy.
sonuc = [i if i%2 == 0 else "tek sayi" for i in range(11)]
print(sonuc)

urun_fiyatlari = [3000, 1000, 4000, 5000,-200]
vergiler = []

vergiler = [vergi*1.2 for vergi in urun_fiyatlari if vergi>0]
vergiler = [fiyat*1.2 if fiyat > 0 else "vergi hesaplanamadı" for fiyat in urun_fiyatlari]
print(vergiler)