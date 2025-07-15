# parametre sıralarını istediğimiz gibi vermek için
# -> 'den sonra geri dönüş tipini belirtiyoruz

def fullName(firsname: str, surname: str, age: int) -> str:
    return f"Your name is : {firsname} {surname} {age}"

result1 = fullName("Utku", "Çakar", 10)
result2 = fullName(surname="Çakar", firsname="Utku", age=10)
result3 = fullName(age=10, firsname="Utku", surname="Çakar")

print(result1)
print(result2)
print(result3)