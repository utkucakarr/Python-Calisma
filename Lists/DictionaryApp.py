# Bu dictionary içinde tanımlanan değerler bir list, tuple veya bir dictionary olabilir.
students = {
    101: {
        "Name": "Utku",
        "Surname": "Çakar",
        "DateOfBirth": 2010,
        "Grades": (40,80,90)
    },
    102: {
        "Name": "Umut",
        "Surname": "Çakar",
        "DateOfBirth": 2012,
        "Grades": (80,80,80)
    },
    103: {
        "Name": "Nuray",
        "Surname": "Çakar",
        "DateOfBirth": 2014,
        "Grades": (70,70,70)
    }
}

print(students)
print(students[101])
print(students[101]["Name"])

# Klavyeden girilen öğrenci numarasına göre aşağıdaki cümleyi yazdırınız
    # 101 numaralı Utku Çakar ismindeki öğrencinin yaşı 14 ve nor ortalaması 76.

numberOfStudent = int(input("Please enter the number of student: "))
student = students[numberOfStudent]

currentYear = 2025
age = currentYear - student["DateOfBirth"]
avarageOfGrade = (student["Grades"][0] + student["Grades"][1] + student["Grades"][2]) / 3

print(f"{numberOfStudent} numaralı {student["Name"]} {student["Surname"]} öğrencisinin yaşı {age} ve not ortalaması {avarageOfGrade}.")