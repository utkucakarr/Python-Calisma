# error: Hata bize bir durum karşısında uygulama çalışmasını durdurur ve bize bir hata döner.

# error handling : Hatayı düzgün bir şekilde ele alma. Hata durumunda uygulama çalışmayı durdurmasın çalışmaya devam etsin

try:
    x = int(input("x : "))
    y = int(input("y : "))
    print(x + y)
except:
    print("Hata Oluştu")