orgaanisation = "BTK AKADEMİ".split() # str to list
print(type(orgaanisation))
print(orgaanisation[0])
print(orgaanisation[1])

numbers = [1,2,3,4,5]
names = ["Utku", "Umut", "Nuray"]

print(type(numbers))
print(type(numbers[0]))
print(type(names))
print(type(names[0]))

student = ["Ahmet", "Turan", 60, 70, 50]
print(student[0] + " " + student[1])

average = (student[2] + student[3] + student[4]) / 3

print(average)

students = [["Ahmet", "Turan", 60, 70, 50], ["Utku", "Çakar", 40, 50, 60]]

print(students[0])
print(students[0][0])
print(students[1])
print(students[1][2])