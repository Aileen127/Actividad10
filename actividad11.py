# Tienda de ropa
products = {}

print("Bienveniddo a la tienda de ropa")
quantity = int(input("Ingresa cuantos productos quieres ingresar"))
if quantity > 0:
    for p in range(quantity):
        code = input("Ingresa el código del producto")

