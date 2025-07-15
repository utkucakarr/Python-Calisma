def selamlama(isim):
    return "Merhaba, " + isim

print(selamlama("Utku"))
print(selamlama("Umut"))


def sum(number1, number2):
    return number1 + number2

print(sum(10, 20))
print(sum(20, 30))
print(sum("Utku", "Umut"))


def yasHesapla(dogumYili):
    return 2025 - dogumYili

print(yasHesapla(1998))

def emeklilgeKacYilKaldi(dogumYili, isim):
    yas = yasHesapla(dogumYili)

    kalanSure = 65 - yas
    
    if(kalanSure > 0):
        return f"{isim}, emekliliğinize kalan süre {kalanSure} yıl kaldı"
    else:
        return f"{isim}, zaten {abs(kalanSure)} yıl önce emekli oldunuz."

print(emeklilgeKacYilKaldi(1998, "Utku"))
print(emeklilgeKacYilKaldi(1950, "Umut"))