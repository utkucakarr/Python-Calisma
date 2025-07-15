"""
    module1 (db)         : urunler
    module2 (methods)    : urunEkle(), urunGuncelle(), urunleriGetir()
    module3 (app)        :

            yeni ürün ekleme => urunEkle("Iphone 15", 60000)
            ürün güncelle    => urunGüncelle(1, "iphone 15 pro", 80000
            ürünleri listele => urunleriGetir()
"""

from methods import *

result = getAllProduct()
for i in result:
    print(f"id: {i["id"]} ürün adi: {i["productName"]} fiyatı: {i["price"]}")

addProduct("IPhone 20", 70000)
result = getAllProduct()
for i in result:
    print(f"id: {i["id"]} ürün adi: {i["productName"]} fiyatı: {i["price"]}")

reslt1 = getByIdProduct(2)
print(reslt1)

updateProduct(1, "IPhone 15", 80000)
print(result)