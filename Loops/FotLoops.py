# for => Liste işlemleri için

numbers = [1,2,3,4,5,6,7]
names = ["Utku", "Umut", "Nuray"]
isim = "Utku"
myTuple = [(1,2), (3,4), (5,6)]
myDictionary = {"41": "Kocaeli", "53": "Rize", "35": "İzmir"}

for n in numbers:
    print(n)

for n in numbers:
    print("Marhaba Utku")

for na in names:
    print(na)

for i in isim:
    print(i)

for a,b in myTuple:
    print(a,b)

for x in myDictionary:
    print(myDictionary[x])
#Bu kullanım daha iyi gibi duruyor.
for x in myDictionary.values():
    print(x)

for x in myDictionary.keys():
    print(x)

for x in myDictionary.items():
    print(x)
# while => Koşul işlemlerinde