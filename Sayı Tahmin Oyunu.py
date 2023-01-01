import time
import random

print("""
Sayı Tahmin Oyunu
1 - 40 arasında rastgele tahmin edin. (40 dahil)
""")

tahmin_hakki = 7
rastgele_sayi = random.randint(1,40)

while True:

    tahmin = int(input("Tahmininiz: "))

    if (tahmin == rastgele_sayi):
        print ("Sayı Sorgulanıyor...")
        time.sleep(1)
        print("Tebrikler!")
        print("Sayı", rastgele_sayi)
        break

    elif (tahmin < rastgele_sayi):
        print ("Sayı Sorgulanıyor...")
        time.sleep(1)
        tahmin_hakki=-1
        print ("Lütfen Daha Yüksek Bir Sayı Söyleyin.")
        print ("Tahmin Hakkı: ", tahmin_hakki)

    else:
        print ("Sayı Sorgulanıyor...")
        time.sleep(1)
        tahmin_hakki=-1
        print ("Lütfen Daha Düşük Bir Sayı Söyleyin.")
        print ("Tahmin Hakkı: ", tahmin_hakki)
    
    if (tahmin_hakki == 0):
        print ("Tahmin Hakkınız Bitti.")
        print ("Sayımız: ", rastgele_sayi)
        break