# (yas >= 18) ==> true, false
# (mezunyet == "lise") ya da (mezuniyet == "üniversite")
# result = (yas >= 18) ve (mezuniyet == "lise") veya (mezuniyet == "Üniversite")

x = 11
result1 = (x > 5) and (x < 10)
print(result1)

# And
result2 = (x > 0) and (x % 2 == 0)
print(result2)

# Or
result3 = (x > 0) or (x % 2 == 0)
print(result3)

# not
result4 = not (x > 0)
print(result4)