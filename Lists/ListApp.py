# "Toyota, Bmwi Renault, Mercedes" elemanlarına sahip markalar isimli bir liste oluşturunuz.

brands = ["Toyota", "Bmw", "Renault", "Mercedes"]

# Liste kaç elemanlıdır?
print(len(brands))

# Listenin ilk ve son elemanı nedir?
print(brands[:1])
print(brands[-1:])

# "Renault" markasını "Togg" ile güncelleyiniz.
brands[2] = "Togg"
print(brands)

# "Togg" listenin bir elemanımıdır
result = "Togg" in brands
print(result)

# Listenin ilk 2 elemanınını alınız.
result1 = brands[0:2]
print(result1)

# Listenin sonuna "Ford" ve "Citroen" markalarını ekleyiniz.
brands += ["Ford", "Citroen"]
print(brands)

# Listenin son elemanını siliniz
del brands[-1]
print(brands)

# Aşağıdaki verileri liste içerisinde saklayınız.

    # öğrenci1 : Yiğit Bilgi 2010 [70,80,90]
    # öğrenci2 : Utku Çakar 2011 [40,20,100]
    # öğrenci3 : Umut Çakar 2012 [50,70,60]

student1 = ["Yiğit Bilgi", 2010, [70,80,90]]
student2 = ["Utku Çakar", 2011, [40,20,100]]
student3 = ["Umut Çakar", 2012, [50,70,60]]

students = [student1, student2, student3]
print(students)

# Öğrencilerin yaşlarını hesaplayınız
currentYear = 2025
student1Age = currentYear - student1[1]
student2Age = currentYear - student2[1]
student3Age = currentYear - student3[1]
print(f"{student1[0]} yaşı: {student1Age}, {student2[0]} yaşı: {student2Age}, {student3[0]} yaşı: {student3Age}")

# Öğrencilerin not ortalamalarını hesaplayınız
student1AverageGrade = (student1[2][0] + student1[2][1] + student1[2][2]) / 3
student2AverageGrade = (student2[2][0] + student2[2][1] + student2[2][2]) / 3
student3AverageGrade = (student3[2][0] + student3[2][1] + student3[2][2]) / 3

print(f"{student1[0]} öğrencisinin not ortalaması: {student1AverageGrade} {student2[0]} öğrencisinin not ortalaması: {student2AverageGrade} {student3[0]} öğrencisinin not ortalaması: {student3AverageGrade}")