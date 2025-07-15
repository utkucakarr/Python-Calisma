# value type Bellekte değerleri tutar
x = 10
y = 20

x = y

y = 30

print(x + y)


# referans type bütün liste tipleri referans tiplerdir. Verilerin adresini bellekte tutar.

a = ["elma", "armut"]
b = ["Elma", "Armut"]

# Bellekten a ve b'nin adresleri aynı oldu artık
a = b

print(a)
print(b)

a[0] = "Üzüm"

print(a)
print(b)

# listeler üzerinde bellekleri değilde değerleri eşitlemek için
# liste kopyalama
listeA = [10, 20]
listeB = listeA.copy() # bellekte farklı bir adres ile listeB oluşturdu. 1.Yöntem

listeB = list(listeA) # 2. yöntem


listeA[0] = 20

print(listeA, listeB)