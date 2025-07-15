#args tupple yapısında gelir
#keyword argument bir dictionary yapısında gelir

def displayUser(**kwargs):
    # print(type(kwargs))
    # print(kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    print("\n")

displayUser(userName = "utkuçakar")
displayUser(userName = "utkuçakar", email= "utku@hotmail.com")


def myFunc(a,b,c,*args,**kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

myFunc(10,20,30,40,50,60,key1="value1", key2= "value2")
