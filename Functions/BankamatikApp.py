# Bankamatik uygulaması

# Hesap bilgileri tutulacak. (dict)
# menu, paraCekme, bakiyeSorgulama, paraYatirma fonksitonları tanımlanacak.
# cekilmek istenen tutar hesapta yoksa ek hesabun kullnılmak istendiği sorulacak.

accountInformation = [
    {
        "name": "Utku Çakar",
        "cardNo": "12345",
        "balance": 20000,
        "extraAccount": 5000,
        "userName": "utkucakar",
        "password": "1234"
    },
    {
        "name": "Umut Çakar",
        "cardNo": "12345",
        "balance": 30000,
        "extraAccount": 10000,
        "userName": "umutcakar",
        "password": "1234"
    }
]

def menu(account):
    print("\n")

    print(f"Kullanıcı girişi başarılı hoşgeldin {account["name"]}")

    print("1- Bakiye Sorgulama: ")
    print("2- Para Çekme: ")
    print("3- Para Yatırma: ")

    islem = input("Yapmak istediğiniz işlem: ")

    if islem == "1":
        bakiyeSorgula(account)
    elif islem == "2":
        paraCekme(account)
    elif islem == "3":
        paraYatirma(account)
    else:
        print("Yanlış seçim")
    
    menu(account)

def bakiyeSorgula(account):
    print(f"bakiye: {account["balance"]}")
    print(f"ek bakiye: {account["extraAccount"]}")


def paraCekme(account):
    miktar = float(input("Çekmek istediğiniz miktar: "))

    if(account["balance"] >= miktar):
        account["balance"] -= miktar
        print("Paranızı alabilirsiniz.")
    else:
        toplam = account["balance"] + account["extraAccount"]

        if (toplam >= miktar):
            ekHesapKullanimIzni = input("Ek hesap kullanılsın mı= (e/h) ")
            if(ekHesapKullanimIzni == "e"):
                kullanilacakMiktar = miktar - account["balance"]
                account["balace"] = 0
                account["extraAccount"] -= kullanilacakMiktar
                print("Paranızı alabilirsiniz.")
            else:
                print("Üzgünüz bakiyeniz yetersiz")
        else:
            print("Üzgünüz ek hesap izniniz olmadığı için ana bakiyeniz yetersiz")

def paraYatirma(account):
    pass

def login():
    username = input("username: ")
    password = input("password: ")

    isLoggedIn = False

    for account in accountInformation:
        if(account["userName"] == username and account["password"] == password):
            isLoggedIn = True
            menu(account)
            break
        
    if(not isLoggedIn):
        print("username yada password yanlış.")

login()