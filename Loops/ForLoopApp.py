numbers = [3,5,7,2,12,32,45]

# "Sayilar" listesindeki her bir elemanı yazdırınız.

for n in numbers:
    print(n)

# "Sayilar" listesinde hangi sayılar 3'ün katıdır=

for n in numbers:
    if(n % 3 == 0):
       print(n)

# sayilar listesindeki tüm sayiların toplamı
sum = 0
for n in numbers:
    sum += n

print(sum)

products = ["samsung s24", "samsung s22", "iphone 15", "iphone 14"]
# "ürünler" listesindeki tüm iphone marka ürünlerini listeleyiniz (find, index)
for p in products:
    if(p.find("iphone") == 0):
        print(p)


# "ürünler" listesinde kaç adet samsung ürünü vardır?
index = 0
for t in products:
    if(t.find("samsung") == 0):
        index += 1
print(index)