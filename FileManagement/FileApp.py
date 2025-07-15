# Not Uygulaması

# 1- Menü
    # 1- Not Gir
    # 2- Ortalamaları göster (90-100 -> AA, 85-89 -> BA)
    # 3- Notları Kayıt Et
    #- Çıkış

def calculate_grade(satir):
    satir = satir[:-1]
    liste = satir.split(":") # listeyi :'dan ikiye ayırır

    studentName = liste[0]
    grades = liste[1].split(",") # listeyi virgüllerden ayırır

    grade1 = int(grades[0])
    grade2 = int(grades[1])
    grade3 = int(grades[2])

    average = (grade1 + grade2 + grade3) / 3

    if(average >= 90 and average <= 100):
        letter = "AA"
    elif(average >= 80 and average <= 89):
        letter = "BA"
    elif(average >= 75 and average <= 79):
        letter = "BB"
    elif(average >= 70 and average <= 74):
        letter = "CB"
    elif(average >= 65 and average <= 69):
        letter = "CC"
    elif(average >= 60 and average <= 64):
        letter = "DC"
    elif(average >= 50 and average <= 59):
        letter = "DD"
    elif(average >= 40 and average <= 49):
        letter = "FD"
    elif(average >= 0 and average <= 39):
        letter = "FF"

    return f"{studentName} : {letter} ({average})"

def enter_grade():
    name = input("Öğrenci Adi: ")
    surname = input("Öğrenci Soyadi: ")
    grade1 = input("Not 1: ")
    grade2 = input("Not 2: ")
    grade3 = input("Not 3: ")

    with open("exam_grades.txt", "a", encoding="utf-8") as file:
        file.write(name + " " + surname + ": " + grade1 + "," + grade2 + "," + grade3 + "\n")


def read_grades():
    with open("exam_grades.txt", "r", encoding="utf-8") as file:
        for satir in file:
            print(calculate_grade(satir))

def save_grades():
    with open("exam_grades.txt", "r", encoding="utf-8") as file:
        liste = []

        for satir in file:
            liste.append(calculate_grade(satir))

        with open("exam_grades.txt", "w", encoding="utf-8") as file2:
            file2.writelines(liste)

while True:
    proccess = input("1- Not Giriniz\n2- Notları Oku\n3- Notları Kayıt Et\n4- Çıkış\nLütfen yapmak istediğiniz işlemi belirtiniz: ")

    if(proccess == "1"):
        enter_grade()
    elif(proccess == "2"):
        read_grades()
    elif(proccess == "3"):
        save_grades()
    else:
        break