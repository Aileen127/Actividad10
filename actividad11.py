# Tienda de ropa
products = {} # Diccionario

print("Bienvenido a la tienda de ropa")
quantity = int(input("Ingresa cuantos productos quieres ingresar: "))
if quantity > 0:
    for p in range(quantity):
        while True:
            while True:
                code = input("Ingresa el código del producto: ")
                if code not in products:
                    break
                else:
                    print("El código ya ha sido registado")

            name = str(input("Ingresa el nombre del producto: "))
            category = input("Ingresa la categoría del producto (Hombre, Mujer, Niño): ")
            size = input("Ingresa la talla del producto (S, M..): ")
            while True:
                price = float(input("Ingresa el precio del producto en quetzales: "))
                if price > 0:
                    products[code]={"precio": price}
                    break
                else:
                    print("Ingrese un precio mayor a 0")
            while True:
                stock = int(input("Ingresa la cantidad de stock que esta disponible: "))
                if stock > 0:
                    break
                else:
                    print("Dato inválido, intenta de nuevo")
            products[code]={"Nombre:" : name,
                            "Categoría:" : category,
                            "Talla:" : size,
                            "Precio:" : price,
                            "Stock:" : stock}
            break
for clave, valor in products.items():
    print(clave, ":", valor)