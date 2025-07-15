"""
        Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.

        Kullanımı           : open(dosya_adi, dosya_erişime_modu)
        dpsya erişme_modu   : dosyayo hangi amaçla açtığımızı belirtir.
        "r" okuma modu      : okuma modu: belirtilen konumda dosya olmalıdır.
        seek                : cursor konumu
"""

f = open("log.txt", encoding="utf-8")

print(f.read())
f.seek(0)
print(f.readline()) # readline() tek satır okumak için
f.seek(0)
print(f.readlines()) # readlines() her satırı liste halinde bize verir
print(f.read())
print(f.closed) # dosya kapalımı bilgisin verir.
f.close() # dosyayı kapatır.
print(f.closed) # dosya kapalımı bilgisin verir.