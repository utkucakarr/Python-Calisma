# Fonksiyondan değer döndürme

def sum(x, y):
    return x + y

result = sum(3, 5)
print(result)

def yil():
    import datetime
    return datetime.datetime.now().year

def clock():
    import datetime
    return datetime.datetime.now().year

def yasHesapla():
    return yil() - 1983

print(yasHesapla())


def hour():
    import datetime
    return datetime.datetime.now().hour


def selamlama():
    if(hour() < 12):
        return "Günaydın"
    else:
        return "Merhaba"
    
print(selamlama())