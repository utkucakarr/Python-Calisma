# "w": (write) yazma modu.
#   ** Dosya konumda yoksa o dosya oluşturulur.
#   ** Eğer konumda aynı dosya varsa dosyayı siler ve yeni oluşturur.

with open("dosya.txt", "w", encoding="utf-8") as file:
    file.write("Utku Çakar\n")
    file.write("Umut Çakar\n")

with open("dosya.txt", "r", encoding="utf-8") as file:
    for i in file:
        print(i, end="")