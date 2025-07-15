customers = ["utkucakar", "umutcakar", "ahmetsaygili", "fuatfidangul"]
order_totals = [12000, 13000, 5000, 15000]

# 'utkucakar' kullanıcı adıyla yapılan 5000 liralık siparişi listeye ekleyiniz
customers.append("utkucakar")
order_totals.append(5000)

result1 = customers
result2 = order_totals
print(customers, order_totals)

# son eklenen siparişi siliniz
customers.pop()
order_totals.pop()
print(customers)
print(order_totals)

# Tüm müşteriler için aşağıdaki özet cümleyi yazdırınız
    # '<username>' isimli müşterinin sipariş toplamı '<10000>' liradır.

print(f"{customers[0]} isimli kullaninin sipariş toplamı {order_totals[0]} liradır.")
print(f"{customers[1]} isimli kullaninin sipariş toplamı {order_totals[1]} liradır.")

# Müşterileri alfabetik olarak sıralayınız.
customers.sort()
print(customers)

# Sipariş toplamlarını azalan şekilde sıralayınız.
order_totals.sort()
order_totals.reverse()
print(order_totals)

# En düşük sipariş hangisidir
result3 = min(order_totals)
print(result3)

# 'utkucakar' isimli kullanıcının kaç tane siparişi vardır
result4 = customers.count("utkucakar")
print(result4)

# Customers üzerinden 'umutcakar' isimli kullanıcıyı siliniz
customers.remove("umutcakar")
print(customers)

# Listenin tüm içeriklerini siliniz
customers.clear()
order_totals.clear()
print(customers)
print(order_totals)

#Kullanıcıdan aldığınız kullanıcı adı ve sipariş toplamlarını listeye ekleyiniz.
user = input("Lütfen bir kullanıcı giriniz: ")
customers.append(user)
orderPrice = int(input("Lütfen sipariş toplamını giriniz: "))
order_totals.append(orderPrice)

print(customers)
print(order_totals)