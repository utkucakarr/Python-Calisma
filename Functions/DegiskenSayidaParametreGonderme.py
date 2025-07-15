# numbers = (10,20,30,40)
# def toplam(liste):
#     result = 0
#     for i in liste:
#         result += i
#     return result

# result1 = toplam(numbers)

# print(result1)


# buradaki * bunun değişken sayıda parametre alabileceğini belirtir.

def toplam(*args):
    print(args)
    print(type(args))
    result = 0
    for i in args:
        result += i
    return result

result1 = toplam(10,20)
result2 = toplam(10,20,30)
result3 = toplam(10,20,30,40)

print(result1)
print(result2)
print(result3)