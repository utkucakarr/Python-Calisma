file = open("log.txt", encoding="utf-8")

print(file.read())

file.close()

with open("log.txt", encoding="utf-8") as file:
    print(file.read(10)) # 10 karakter okumamızı sağlar
    print(file.tell()) # cursor konumunu söyler
    print(file.read())
    print(file.tell())


with open("log.txt", encoding="utf-8") as file:
    for i in file:
        print(i, end="") # end ile sonunda karakter okumadan satır satır okur

print("\n")

try:
    with open("log2.txt", encoding="utf-8") as file:
        for i in file:
            print(i, end="") # end ile sonunda karakter okumadan satır satır okur
except FileNotFoundError as e:
    print("dosya okuma hatası",)