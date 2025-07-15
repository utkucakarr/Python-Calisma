# Dictionary Methods

recipes = {
    "foodName" : "Musakka",
    "recipes" : "tarif açıklaması",
    "image": "1.jpg"
}

# acces items
result1 = recipes["foodName"]
print(result1)
result2 = recipes.get("foodName")
print(result2)
result3 = recipes.keys()
print(result3)
result4 = recipes.values()
print(result4)
result5 = recipes.items() # liste olarak döner
print(result5)

# update items
# recipes["foodName"] = "Mantı"
# recipes["foodName2"] = "Mantı"

recipes.update({"foodName" : "Mantı"})
result6 = recipes
print(result6)

recipes.update({"foodName2" : "Mantı"})
result7 = recipes
print(result7)

# delete items
recipes.pop("foodName")
result8 = recipes
print(result8)

recipes.popitem() # listeye son eklenen elemanı siler
recipes.clear() # liste içerisindeki bütün elemanları siler

# copy => referans
