a, b, c = 4, 8, (12, 2)

# Kullanıcıdan aldığınız 2 sayının çarğımı ile a,b,c toplamının farkı nedir=
number1 = int(input("Please enter the number 1: "))
number2 = int(input("Please enter the number 2: "))

multiply = number1 * number2
sumOfNumbers = a + b + c[0] + c[1]
minusOfNumbers = multiply - sumOfNumbers

print(minusOfNumbers)

# c' nin B'ye kalansız bölümünü hesaplayınız
sum = c[0] + c[1]
divide = sum // b
print(divide)

# (a,b,c) toplamının mod 7'si nedir?
sum = a + b + (c[0] + c[1])
result = sum % 7
print(result)

# B' nin a' kuvvetini hesaplayınız
result1 = b ** a
print(result1)

# a, *b, c = (2,4,6,8,13) işlemine göre c' nin küpü nedir?
a, *b, c = (2,4,6,8,13)
print(a, b, c)

result2 = c ** 3
print(result2)

# a, b, *c = (2,4,6,8,13) işlemine göre c'nin değerleri toplamı nedir
a, b, *c = (2,4,6,8,13)

sum = c[0] + c[1] + c[2]
print(sum)