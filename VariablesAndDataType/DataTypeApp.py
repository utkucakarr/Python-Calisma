pi = 3.14
radius = float(input("Please enter the radius for circle: "))

area = pi * (radius ** 2)
perimeter = 2 * pi * radius

print("Dairenin alanı: " + str(area) + " Dairenin Çevresi: " + str(perimeter))


km = int(input("Please enter the km information : "))
mil = km / 1.609344
mil = round(mil, 2)
print(str(km) + " km " + str(mil) + " yapar. ")