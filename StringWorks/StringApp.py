title = "Python ile Programlama Dersleri"

titleCount = len(title)
titlePython = title[0:7]
titleFirst5 = title[0:5]
titleLast5 = title[-6:-1]
reverse = title[::-1]


print(titleCount)
print(titlePython)
print(titleFirst5)
print(titleLast5)
print(reverse)


student = input("Lütfen öğrenci adını giriniz: ")
grade1 = int(input("Lütfen öğrencinin 1. notunu giriniz: "))
grade2 = int(input("Lütfen öğrencinin 2. notunu giriniz: "))

averageGrade = (grade1 + grade2) / 2

print(f"{student} isimli öğrencinin 1.notu {grade1}, 2. notu {grade2} ve not ortalaması {averageGrade} olarak hesaplanmıştır.")