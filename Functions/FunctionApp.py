# 1- Kendisine gönderiken bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız.

def write(kelime, sayac):
    return kelime * sayac

print(write("Utku ", 5))


# 2- Dikdörtgenin alan ve çevresini hesaplayan fonksiyonu yazınız.

def dikdortgen(a, b):
    alan = a * b
    cevre = 2 * (a + b)
    return f"Dikdörtgenin alanı : {alan} ve çevresi : {cevre}"

print(dikdortgen(4, 5))


# 3- Yazı tura uygulamasını fonksiyon kullanarak yapınız. (Random modüle)
import random
sayi = random.random()
print(random.random())

def yaziTura():
    import random
    sayi = random.random()

    if(sayi >= 0.5):
        return "Tura"
    else:
        return "Yazi"

sonuc = yaziTura()
print(sonuc)


# 4- Kendisine gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyonu yazınız

def asalmi(sayi1, sayi2):
    for sayi in range(sayi1, sayi2+1):
        if (sayi > 1):
            for i in range(2, sayi):
                if (sayi % i == 0):
                    break
            else:
                print(sayi)

asalmi(1,10)



# 5- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonksiyonu yazınız.

def tamBolenler(sayi):
    tamBolen = []
    for i in range(2, sayi):
        if(sayi % i == 0):
            tamBolen.append(i)
    return tamBolen

print(tamBolenler(10))