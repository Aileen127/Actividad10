# Tienda de ropa
products = {} # Diccionario

print("Bienvenido a la tienda de ropa")
quantity = int(input("Ingresa cuantos productos quieres ingresar: "))
if quantity > 0:
    for p in range(quantity):
        code = input("Ingresa el código del producto: ")
        name = input("Ingresa el nombre del producto: ")
        category = input("Ingresa la categoría del producto (Hombre, Mujer, Niño): ")
        size = input("Ingresa la talla del producto: ")
        price = float(input("Ingresa el precio del producto en quetzales: "))
        while code not in products:
            print("El código ha sido registrado")
            products[code] = code
        else:
            print("El código ya ha sido registado")


    if price > 0:
        print("Hola")
    mount = int(input("Ingresa la cantidad de stock que esta disponible: "))
    if price > 0:
        print("Hola")

