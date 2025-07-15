# x = 10

# if(x > 5):
#     raise ValueError("x 5' den büyük olamaz")

def renklendir(text, renk):
    renkler = ("blue", "red", "white", "black", "orange")
    if type(text) is not str:
        raise TypeError("text str tipinde olmalıdı")
    
    if type(renk) is not str:
        raise TypeError("renk str tipinde olmalıdır")
    
    if renk in renkler:
        raise ValueError("Geçersiz bir renk")
    
    print(f"{text} {renkler} olarak yazıldı.")


try:
    renklendir(10, "red")
    renklendir("selam", "red")
    renklendir("merhaba", "yellow")
except (TypeError, ValueError) as ex:
    print(ex)