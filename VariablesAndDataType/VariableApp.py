"""
Yorum satiri
"""
#Yorum satiri

customerName = "Utku"
customerSurname = "Çakar"
customerEmail = "utku@hotmail.cpom"
customerPhoneNumber = "5555555555"

product1Name = "Kablosuz Klavye"
product1Price = 550

product2Name = "Kablosuz Mouse"
product2Price = 650

product3Name = "Dizüstü Bilgisayar"
product3Price = 650

kdvRate = 1.18
totalPrice = product1Price + product2Price + product3Price
totalPriceWithKdv = totalPrice * kdvRate

print("Toplam ödenen miktar: ", totalPrice)
print("Toplam ödenen ücret kdv dahil : ", totalPriceWithKdv)