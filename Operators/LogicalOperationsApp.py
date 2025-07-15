# Yaşı 18'den büyük ya da veli izni varsa bir işte çalışabilir durumunu kontrol ediniz.

age = int(input("Plase enter your age: "))
isPermission = input("Please enter your permission: ")
result1 = (age > 18) and (isPermission == "var")
print(f"Çalışabilir: {result1}")

# Ders notu 50-100 arasındaysa geçti değilse kalsın bilgisini yazdırınız.
grade = 101
result2 = (grade >= 50) and (grade <= 100)
print(f"Geçti: {result2}")

# Not ortalaması en az 70 puan ve zayıfı yoksa teşekkür belgesi alabilme durmunu kontrol ediniz

averageGrade = 70
hasBadGrade = False
resul3 = (averageGrade >= 70) and (hasBadGrade == False)
print(f"Teşekkür belgesi alamaya hak kazandı mı : {resul3}")


# İşe girmek için en az önlisans ya da lisan mezunu olma durumunu kontrol ediniz. Sigara kullanmama koşulu.

onlisans = True
lise_mezunu = False
sigara = False

result4 = ((onlisans == True) or (lise_mezunu == True)) and (sigara == False)
print(f"İşe girebilir : {result4}")

# Uygulamaya giriş kontrolünü "username yada email" ve "parala" için yapalım.
userName = "Utku"
email = "utku1@hotmail.com"
password = 123456
result5 = ((userName == "Utku") or (email == "utku@hotmail.com")) and (password == 123456)
print(result5)