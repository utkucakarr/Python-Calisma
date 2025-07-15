# Class
# instance, Nesne

class Product:
    # attribute, property
    def __init__(self, name, price, isActive):
        self.name = name
        self.price = price
        self.isActive = isActive

    # method
    def get_product(self):
        return f"ürün adı: {product.name} ürün fiyatı : {self.kdv_price}"
    
    def kdv_price(self):
        return self.price * 1.20
    

p1 = Product("IPhone 15", 1500, True) # product sınıfından türetilen bir nesne
p2 = Product("IPhone 15 Pro", 2000, False)

print(type(p1))
print(type(p2))

result1 = p1.name, p1.price, p1.isActive
result2 = p2.name, p2.price, p2.isActive
print(result1)
print(result2)

products = [p1, p2]

for product in products:
    if(product.isActive):
        print(product.get_product())
        print(product.kdv_price())