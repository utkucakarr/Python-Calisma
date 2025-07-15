# Sets kullanırsak liste listelenemez, sıralanamaz, güncellenemez, elemanlar tekrarlanamaz, eleman siler yada ekleyebiliriz.

fruits = {"Elma", "Armut", "Kiraz", "Elma"}
fruits2 = {"Elma", "Armut", "Kiraz", "Kavun"}

print(type(fruits))
print(fruits)

for x in fruits:
    print(x)

result1 = "Elma" in fruits
print(result1)

fruits.add("Karpuz")
print(fruits)

fruits.update(fruits2)
print(fruits)

fruits.remove("Elma") # liste üzerinden silme yapar.
print(fruits)
fruits.discard("Armut") # liste üzerinden silme yapar
print(fruits)
fruits.discard("Vişne") # listede eleman yoksa hata göndermez.
print(fruits)
# fruits.remove("Vişne") # listede eleman yoksa hata verir
fruits.clear()
print(fruits)