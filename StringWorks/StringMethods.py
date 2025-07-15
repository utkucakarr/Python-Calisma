message = "BTK Akademi Python Kursu"

result = message.upper()
result1 = message.lower()
result2 = message.capitalize()
result3 = message.title()

result4 = "abc".isupper()
result5 = "abc".islower()

result6 = message.strip() # MEsajın başındaki boşluk karakterini siler.
result7 = message.split() # Her boşluk karakterinden sonraki kelimeyi ayırır.
result8 = message.split(',')
result9 = message.index("Akademi")
result10 = message.startswith("B")
result11 = message.replace("Python", "javascipt")

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