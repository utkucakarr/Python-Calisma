liste = [1,2,3,4]

# 1'den 100'e kadar 2şer 2 şer artsın

# for i in range(1,100,2):
#     print(i)

rng = range(10)
rng = range(10, 20)
rng = range(100, 200, 10)
rng = range(0, -20, -1)

liste = list(rng)
print(liste)

for i in range(50,250):
    if(i % 2 != 0):
        print(i)