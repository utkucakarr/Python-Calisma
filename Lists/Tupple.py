# Tupple listeye benzer ancak içerisindeki elemanlar değiştirlemez yani tuple listesine ekleme, silme ve güncelleme yapamayız.

myList = [1,2,3]
myTupple = (1,2,3) # Veri tabanından bilgileri alıp liste içerisinden verileri göstermek istediğimizde yapılabilir. Bellekte daha az yer kaplar!

print(type(myList))
print(type(myTupple))

result1 = myList[0]
result2 = myTupple[0]
myList[0] = 4
# myTupple[0] = 4
myList.append(5)
result4 = myTupple.count(1)

my_tuple2 = tuple([1,2,3]) # Listeyi tuple dönüştürdük.
my_list2 = list((2,3,4)) # Tuple listeye çevirdik.

print(result1)
print(result1)
print(myList)
print(result4)
print(type(my_tuple2))
print(type(my_list2))
