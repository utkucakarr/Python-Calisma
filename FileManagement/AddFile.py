# "r": (read) okuma, Dosya konumu yoksa hata verir.
# "W": (write) yazma modu.
#       ** Dosyayı konumda oluşturur.
#       ** Dosya içeriğini siler ve yeniden ekleme yapar.
# "a": (Append) ekleme. Dosya konumda yoksa oluşturur.
# "r+" Hem okuma hem y<zma modunda açılır. Dosya konumda yoksa hata verir.

with open("dosya.txt", "r+", encoding="utf-8") as file:
    #file.seek(0) # "a" modunda cursor yer değiştirilmesi yapılamaz.
    file.read() # read ile dosya sonuna ulaşıp dosya sonuna satır ekledik.
    file.write("sonuncu satır\n")