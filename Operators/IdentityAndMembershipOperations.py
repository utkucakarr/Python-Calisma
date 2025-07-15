x = [2,4,6]
y = [2,4,6]
z = y

print(x == y) # değerlere bakar
print(x == z)
print(z is y) 
print(x is y) # adreslere bakar
print(x is not y)

# membership
print(2 in x)
print(20 in x)
print(20 not in x)