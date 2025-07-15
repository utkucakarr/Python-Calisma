# Klavueden girilen n sayıdaki öğrenci bilgisini liste içerinde saklayınız.
# ** dicrionary listesi yapısı (ogrenciNo, ogrenciAdi, ogrenciSoyad) şeklinde olsun.
# ** ogrenci ekleme işlemi bittiğinde öğrencileri listeleyiniz.

devamMi = "e"
students = []

while devamMi != "h":
    studentsNumber = input("Öğrenci no: ")
    studentName = input("Öğrenci adı: ")
    studentSurname = input("Öğrenci soyadı: ")

    students.append({
        "studentNo" : studentsNumber, 
        "studentNane" : studentName, 
        "studentSurname" : studentSurname 
    })
    devamMi = input("devam mi= (e/h): ")

for student in students:
    print(f"{student["studentNo"]} numaralı öğrencinin adı {student["studentNane"]} {student["studentSurname"]}")
