# Key ve value türünde bilgi saklanır.
# Güncellenebilir, Sıralanabilir, Tekrarlanmaz.

# uzun yol
# cities = ["Sakarya", "İstanbul", "Bolut"]
# licance_plate = [54, 34, 16]

# print(licance_plate[0], cities[0])
# print(licance_plate[1], cities[1])

# print(licance_plate[cities.index("Sakarya")])
# print(licance_plate[cities.index("İstanbul")])

# Dictionary kısa yol

licance_plate = {
    54: "Sakarya",
    34: "İstanbul",
    35: "İzmirr"
}

licance_plate[35] = "İzmir" # ekleme yapma işlemi

print(type(licance_plate))
print(licance_plate[54])
print(licance_plate[34])
print(licance_plate[35])