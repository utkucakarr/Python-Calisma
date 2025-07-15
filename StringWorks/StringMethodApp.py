courseName = "Btk Akademi Python ile Programlama Desrleri"
webSite = "https://www.btkakademi.gov.tr/"

# 1- ' Btk akademi ' karakter dizisinin baş ve sondaki karakterlerini siliniz.
value = " Btk akademi "
result = value.strip()
print(result)

# kursAdı değişkenindeki tüm karakterleri küçük harfe çeviriniz.
result2 = courseName.lower()
print(result2)

# website değişkeninde kaç tane '.' karakteri vardır?
result3 = webSite.count('.')
print(result3)

# website tr ile mi bitiyor?
result4 = webSite.endswith("tr/")
print(result4)

# kursadı değişkenindeki tüm karakterler harsflerden mi oluşuyor
result5 = courseName.isalpha()
print(result5)

# kursadi değişkenindeki tüm boşlukları '_' ile değiştiriniz.
result6 = courseName.replace(" ", "_")
print(result6)

# kuradindaki python kelimesinin reactJs ile değiştiriniz.
result7 = courseName.replace("Python", "ReactJs")
print(result7)

# website değişkeni 'www' içeriyor mu=
result8 = webSite.find("www")
result9 = webSite.index("www")
print(result8)
print(result9)

# kursadı değişkeninin listeye çeviriniz
result10 = courseName.split()
print(result10)