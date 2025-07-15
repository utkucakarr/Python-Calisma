import sqlite3

connection = sqlite3.connect("chinook.db")
cursor = connection.cursor()

# ekleme sorgusu
sql = "INSERT INTO genres(Name) VALUES('Macera')"
cursor.execute(sql)

connection.commit()

# kayıtları getirmek için kodlar
# cursor.execute("select * from customers where City = 'Oslo'")
# customers = cursor.fetchall() # bütün kayıtları getir
# customers1 = cursor.fetchone() # tek bir kayıt getirir
# for customer in customers:
#     print(customer[1] + " " + customer[2])


connection.close()
print("Veri tabanı bağlantısı hazır.")