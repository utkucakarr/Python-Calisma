# 1- Faktoriyel fonksiyonu oluşturunuz ve fonksiyona gelen değer için hata mesajlarını verin.

def fact(x):
    x = int(x)
    
    if(x < 0):
        raise ValueError("Negatif değer")

    sonuc = 1

    for i in range(1, x + 1):
        sonuc *= i

    return sonuc


for i in [3,6,7,"2a",-1,-7,-79]:
    try:
        x = fact(i)
    except ValueError as e:
        print(e)
        continue
    else:
        print(x)

# 2- Girilen parola içinde türkçe karakter hatası veriniz

def controlPassword(password):
    turkce_karakterler = "şçğüöif"

    for i in password:
        if i in turkce_karakterler:
            raise TypeError("Parola türkçe karakter içeremez")
    print("geçerli parola")

password = input("Lütfen parolanızı giriniz: ")
try:
    controlPassword(password)
except TypeError as e:
    print(e)