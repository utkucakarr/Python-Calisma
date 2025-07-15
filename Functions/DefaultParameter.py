def selamlama(isim = "umut", mesaj = "Selam"):
    return f"{mesaj} {isim}"

result = selamlama("Utku", "Marhaba")
print(result)

result1 = selamlama()
print(result1)

def usAlma(taban, us=2):
    return taban ** us

sonuc = usAlma(2,3)
sonuc = usAlma(5)

print(sonuc)


def toplam(a,b):
    return a+b

def cikarma(a,b):
    return a-b

def islem(a,b,fn = toplam):
    return fn(a,b)

result1 = islem(10,20, cikarma)
result2 = islem(10,20, toplam)
result3 = islem(10,20,)

print(result1)
print(result2)