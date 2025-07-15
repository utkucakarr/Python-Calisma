# local scope
# global scope

x = "global scope"

def myFunc():
    x = "local scope"
    print(x)

myFunc()
print(x)


name = "Çınar"

def changeName(newName):
    global name # global bir değeri fonksiyon içinde değiştirmek için
    name = newName
    return print(f"{name}")

changeName("Utku")
print(name)


name1 = "global string"
def greeting():
    name1 = "Utku"
    def hello():
        name1 = "Umut"
        print("hello", name1)
    hello()

greeting()

x = 50

def test():
    global x
    print(f"x: {x}")

    x = 100
    print(f"changed x to {x}")

test()
print(x)