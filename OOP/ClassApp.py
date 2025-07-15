"""
** BankaHesabi isminde bir sınıf tanımlayınız.
** Üretilen her bir nesne "hesapSahibi" isminde biz özelliği sahip olmalıdır. BankaHesabi("Utku Çakar")
** Üretilen her bir nesne "bakiye" isminde bir özelliğe sahip olup başlangıçta 0.0 değerinde olmalıdır.
** Üretilen her bir nesne için "paraYatir" metodu oluşturun ve dışarıdan yatırılacak miktar bilgisini alıp bakiye üzerine ekleyin ve bakiye miktarını geriye döndürün.
** Üretilen her bir nesne için "paraCek" metodu oluşturun ve dışarıdan çekilecek miktar bilgisini alıp bakiye değerinden çıkarıp geriye döndürün.

    hesap = BankaHesabi("Utku Çakar")
    hesap.hesapSahibi => Utku Çakar
    hesap.bakiye => 0.0
    hesap.paraYatir(1000) -> 1000
    hesap.paraCek(500) -> 500
"""

class BankaHesabi:
    def __init__(self, hesapSahibi):
        self.hesapSahibi = hesapSahibi
        self.bakiye = 0

    def getBakiye(self):
        return self.bakiye
        
    def paraYatir(self, yatirilacakTutar):
        self.bakiye += yatirilacakTutar
        return self.bakiye
    
    def paraCek(self, paraCek):
        self.bakiye -= paraCek
        return self.bakiye
    
hesap = BankaHesabi("Utku Çakar")
print(hesap.paraYatir(1200))
print(hesap.paraCek(500))
print(hesap.getBakiye())


