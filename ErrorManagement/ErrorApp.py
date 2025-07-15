Liste = ["1","3","5","20b","abc","10a","60"]
# 1: Liste elemanları içindeki sayısal değerleri bulunuz.

for i in Liste:
    try:
        result = int(i)
        print(result)
    except ValueError:
        continue

# 2: Kullanıcı 'quit (q)' değerini girmedikçe aldığınız her inputun sayı olduğundan emin olunuz aksi halde hata mesajını yazınız.
while True:
    value = input("Lütfen bir sayı değeri giriniz:")
    if(value == "q"):
        break

    try:
        result = float(value)
        print(f"girilen sayi: {result}")
    except ValueError:
        print("geçersiz sayi")
        continue

# 3: Dictionary ve key bilgilerini parametre olarak alan get(dict, key) fonksiyonu hazırlayınız


urun = {"urunAdi": "samsung s10"}

# d["fiyat"] => KeyError
# get(product, "price") -> none
# get(product, "productName") => samsung s20

def get(dict, key):
    try:
        return list[key]
    except KeyError:
        return None

result = get(urun, "fiyat")

print(result)