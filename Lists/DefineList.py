programming_language = ["Python", "C#", "Java", "JavaScript"]

result = programming_language
result1 = type(programming_language)
result2 = programming_language[0:2]
result3 = programming_language[:2]
result4 = programming_language[0:]
result5 = programming_language[-3: -1]
result6 = programming_language[-3:]
programming_language[-1] = "Php"
result7 = len(programming_language)
result8 = programming_language + ["Go", "Delphi"]
result9 = "Python" in programming_language
result10 = "React" in programming_language

print(result)
print(result1)
print(result2)
print(result2)
print(result4)
print(result5)
print(result6)
print(programming_language)
print(result7)
print(result8)
print(result9)
print(result10)

for pl in programming_language:
    print(pl)

del programming_language[0] # del komutu ile eleman silme işlemi

print(programming_language)