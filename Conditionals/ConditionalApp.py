# Bir öğrencinin 2 yazılı bir sözlü notunu alarak ortalama hesaplayınız ve hesaplanan ortalamaya göre not aralığına karşılık gelen değerlendirmeyi yazdırınız.

# 0-24  => 0
# 25-44  => 1
# 45-54  => 2
# 55-69  => 3
# 70-84  => 4
# 85-100  => 5

grade1 = int(input("Plase enter your grade1 : "))
grade2 = int(input("Plase enter your grade2 : "))
grade3 = int(input("Plase enter your grade3 : "))
averageGrade = (grade1 + grade2 + grade3) / 3

if(averageGrade >= 0 and averageGrade <= 24):
    print(0)
elif(averageGrade >= 25 and averageGrade <= 44):
    print(1)
elif(averageGrade >= 45 and averageGrade <= 54):
    print(2)
elif(averageGrade >= 55 and averageGrade <= 69):
    print(3)
elif(averageGrade >= 70 and averageGrade <= 84):
    print(4)
elif(averageGrade >= 85 and averageGrade <= 100):
    print(5)
else:
    print("Lütfen girdiğiniz notları 0 ile 100 arasında giriniz.")