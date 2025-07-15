# 1-) Başlangıç ve bitiş değerlerini kullanıcıdan alınız ve bu değerler arasındaki tüm çift sayıları yazdırınız.

start = int(input("Lütfen başlangıç değerini giriniz: "))
end = int(input("Lütfen bitiş değerini giriniz: "))

while(start <= end):
    if(start % 2 == 0):
        print(start)
    start += 1

# 2- (1-100) arasındaki sayıları azalan şekilde yazdırınız.

i = 100
while(i >= 1):
    print(i)
    i -= 1

# Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırınız.

i = 0
numbers = []
while(i < 5):
    number = int(input("Lütfen bir sayi giriniz: "))
    numbers.append(number)
    i += 1

numbers.sort()
print(numbers)


# Klavyeden girişi istenen username bilgisi için boşluk girildiği sürece tekrar username girişi isteyiniz.

username = ""

while(not username):
    username = input("Lütfen boşluk olmadan username giriniz: ")

print(f"girilen kullanici adı: {username}")