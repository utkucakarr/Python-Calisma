products = [
    {"productName": "Hp Victus", "price": 32999},
    {"productName": "Lenovo Thinkpad", "price": 25499},
    {"productName": "Appple Macbook", "price": 49999},
    {"productName": "Huawei Matebook", "price": 26999},
    {"productName": "Casper Nirvana", "price": 20000},
]

# Aşağıdaki örnek cümleyi tüm ürünlere uygulayınız.
#   "Hp victus marka ürünün fiyatı 32999 Türk Lirasıdır."
for t in products:
    print(f"{t["productName"]} marka ürünün fiyatı {t["price"]} Türk Lirası.")

# Ürünlerin fiyatları toplamı nedir
sum = 0
for p in products:
    sum += p.get("price")
print(sum)

# 25000 ile 40000 arasındaki ürünleri listeleyiniz
for n in products:
    price = n.get("price")
    if(price >= 25000 and price <= 40000):
        print(price)

# Kullanıcıdan alınan anahtar kelimeye göre ürünleri listeleyiniz.

kelime = input("Aramak istediğiniz ürün adi: ")

for r in products:
    if(r["productName"].lower().find(kelime.lower()) == 0):
        print(r)