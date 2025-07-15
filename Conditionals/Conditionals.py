email = "utku@hotmail.com"
password = 123456
login = (email == "utku@hotmail.com") and (password == 123456)

# if(login):
#     print("Login olundu.")
# else:
#     print("email yada password hatalı.")

# if(not(login)):
#     print("email yada password hatalı.")
# else:
#     print("Login olundu.")

if(email == "utku@hotmail.com"):
    if(password == 123456):
        print("Login olundu")
    else:
        print("Parola hatalı.")
else:
    print("Email hatalı.")


x = 30
y = 30
if (x < y):
    print("x y den küçük")
elif(y < x):
    print("y x den küçük")
else:
    print("x ve y eşit")