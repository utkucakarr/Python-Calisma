#2000 + 2000 + %18

productAPrice = 2000
productBPrice = 3000
kdvRate = 0.18

print(productAPrice + (productAPrice * kdvRate))     # Product 1
print(productBPrice + (productBPrice * kdvRate))     # Product 2

productTotalPrice = productBPrice + productAPrice

print("Urun Toplam Fiyati :", productTotalPrice)