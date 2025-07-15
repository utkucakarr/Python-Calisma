# dosya sonunda 6 numaralı bir marka alanı ekleyiniz.

# with open("Brands.txt", "a", encoding="utf-8") as file:
#     file.write("6-BMW")

# birinci satıra eklemek için

# with open("Brands.txt", "r+", encoding="utf-8") as file:
#     brands = file.read()
#     brands = "1-Toyota\n" + brands
#     file.seek(0)
#     file.write(brands)

# with open("Brands.txt", "r", encoding="utf-8") as file:
#     print(file.read())


# İstediğin bir konuma eklemek için

with open("Brands.txt", "r+", encoding="utf-8") as file:
    brands = file.readlines()
    brands.insert(2, "3-Renault\n")
    file.seek(0)
    file.writelines(brands) # listeyi olduğu gibi yazdırmak için
