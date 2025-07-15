number = [2,4,4,6,8,10,12]
names = ["Utku", "Umut", "Ahmet", "Cağla", "Ali"]

result = min(number)
result1 = min(names)
result2 = max(names)
result3 = max(number)

# ekleme
number.append(14)
result4 = number
names.append("Çınar")
result5 = names

# belirtilen index'e ekleme yapar.
number.insert(0, 100)
result6 = number
number.insert(-1, 200)
result7 = number
number.insert(len(number), 300)
result8 = number

# silme
number.pop()
number.pop(1)

# Elemanın kendisini silmek için
names.remove("Ali")
result9 = names

# sıralama
number.sort()
result10 = number
names.sort()
result11 = names

#tersten sıralama
number.reverse()
result12 = number

#count
result13 = number.count(4)
result14 = names.count("Utku")

#arama
result15 = number.index(4)


print(result)
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
print(result7)
print(result8)
print(result9)
print(result10)
print(result11)
print(result12)
print(result13)
print(result14)
print(result14)