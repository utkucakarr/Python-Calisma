# enumerate => liste indexini ve içindeki değeri ekrana yazıdırır
# zip => Elimizde 1'den fazla liste var ise bunları birleştirmek için kullanılır.

brands = ["Opel", "Bmw", "Togg"]

for b in enumerate(brands):
    print(b)

for b,a in enumerate(brands, 1): # burada indexi 1'den başlamasını sağlıyoruz
    print(b, a)

for b in zip(brands):
    print(b)

# zip

number = [100, 200, 300]
students = ["Utku", "Umut", "Nuray", "Mehmet"]
print(list(zip(number, students)))

for no, name in zip(number, students):
    print(no, name)