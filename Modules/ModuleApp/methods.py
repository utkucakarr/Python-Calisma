from db import *


def addProduct(productName, price):
    products.append({
        "id": len(products) + 1,
        "productName": productName,
        "price": price
    })


def updateProduct(id, productName, price):
    for product in products:
        if(product["id"] == id):
            product["productName"] = productName,
            product["price"] = price
            break


def getByIdProduct(id):
    for product in products:
        if(product["id"] == id):
            return product

def getAllProduct():
    return products
