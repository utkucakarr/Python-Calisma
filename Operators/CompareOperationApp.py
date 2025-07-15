# Girilen 2 sayıdan hangisi büyüktür?
number1 = int(input("Plase enter the number1: "))
number2 = int(input("Please enter the number2: "))
result = number1 > number2

print(f"{number1} {number2}'den büyüktür {result}")

# Girilen bir sayının tek çift kontrülünü yapınız

number3 = int(input("Please enter the number3: "))
number4 = int(input("Please enter the number4: "))
result1 = number3 % 2 == 0
result2 = number4 % 2 == 0
print(f"{number3} çifttir {result1} ve {number4} çifttir {result2}")

# Bir öğrencinin girilen 3 notuna göre başarı durumunu kontrol ediniz. 50 ve üstünde başarılı.

grade1 = int(input("Please enter the grade1: "))
grade2 = int(input("Please enter the grade2: "))
grade3 = int(input("Please enter the grade3: "))

result3 = grade1 >= 50
result4 = grade2 >= 50
result5 = grade3 >= 50
print(f"Öğrencinin 1.dersten başarı durumu: {result3} Öğrencinin 2.dersten başarı durumu: {result4} Öğrencinin 3.dersten başarı durumu: {result5}")