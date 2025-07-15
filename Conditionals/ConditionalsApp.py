# Bir aracın yakıt tipine göre (benzin, dizel, lpg) belirtilen bir mesafede ne kadar yakıt masrafı olduğunu hesaplayan uygulamayı yapınız:
# benzin    : 39.35
# dizel     : 41.71
# lpg       : 20.28

benzin = 39.35
dizel = 41.71
lpg = 20.28
km = int(input("Lütfen ne kadar mesafe gideceğinizi yazınız: "))
yakitTipi = input("Lütfen yakıt tiğinizi yazınız: ")

if(yakitTipi == "benzin"):
    totalPrice = benzin * km
    print(f"Yakıcağınız toplam yakıt fiyatı : {totalPrice}")
elif(yakitTipi == "dizel"):
    totalPrice = dizel * km
    print(f"Yakıcağınız toplam yakıt fiyatı : {totalPrice}")
elif(yakitTipi == "lpg"):
    totalPrice = lpg * km
    print(f"Yakıcağınız toplam yakıt fiyatı : {totalPrice}")
else:
    print("Lütfen doğru yakıt tipi belirtiniz.")