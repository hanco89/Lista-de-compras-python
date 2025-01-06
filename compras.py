#Ejercicios completos

#Lista de compras:
#Creá un programa que:
#Le permita al usuario ingresar productos para armar una lista de compras.
#Cada vez que escriba un producto, agregalo a la lista.
# Si escribe "salir", terminá el programa y mostrá la lista final ordenada alfabéticamente.

# Inventario:
# Tenés un inventario que es un diccionario:

inventario = {"tornillos": 10, "tuercas": 15, "arandelas": 7}

#Permití que el usuario:
#Agregue productos (pidiendo el nombre y la cantidad).
#Quite productos del inventario.
#Si escribe "mostrar", mostrale el inventario completo.
#Si escribe "salir", terminá el programa.

#Mensaje de bienvenida:
print("Bienvenido, haz las compras que necesites indicando producto y cantidad")

while True:

#Introduccion a los comandos:
    print("Utiliza algunas de estas opciones: Agregar/Eliminar/Mostrar/Salir")

    #Variables para definir las opciones:

    agregar = "agregar"

    eliminar = "eliminar"

    mostrar = "mostrar"

    salir = "salir"

#Input para opciones extra:
    user_extra = input("Ingresa el comando: ").lower()

    if user_extra != agregar and user_extra != mostrar and user_extra != salir and user_extra != eliminar:
        print("Por favor proporciona un comando valido")

#Opcion de agregar:
    if user_extra == "agregar":
        user_product = input("Agrega el producto: ")
        try:
#Añadir la cantidad de unidades que quiere del producto
            user_amount = int(input(f"¿Cuantas unidades de {user_product} quieres agregar? "))

            #Comprobando si es un numero con coma
            if type(user_amount) == float:
                print("Error: por favor, ingresá una cantidad válida (número entero).")

#Comprobando si el producto ya existe
            if user_product in inventario:
                inventario[user_product] += user_amount
                print(f"Se añadieron {user_amount} unidades al inventario de {user_product}.")
            else:
                inventario[user_product] = user_amount  # Crear nuevo producto
                print(f"Se agregó {user_amount} unidades de {user_product} al inventario.")

        except ValueError:
            print("Error: por favor, ingresá una cantidad válida (número entero).")

 #Opcion de eliminar:
    elif user_extra == "eliminar":
        user_eliminate = input("Ingresa el producto que quieras eliminar: ")
        try:
            if user_eliminate in inventario:
                user_eliminate_amount = int(input("Ingresa la cantidad que quieres borrar: "))
                inventario[user_eliminate] -= user_eliminate_amount
                print(f"Se han eliminado {user_eliminate_amount} unidades del producto {user_eliminate}")

            else:
                 print(f"El producto {user_eliminate} no existe")    

        except ValueError:
            print("Error, Por favor proporciona un numero valido")        

#Borrando automaticamente los productos con valor 0 (inexistentes):

#Variable para almacenar los productos borrados:
    delete_product = []

#Buscando productos con valor 0 para eliminar:
    for producto , cantidad in inventario.items():
        if cantidad <= 0:
            delete_product.append(producto)


#Borrando los elementos con valor 0 del inventario:
    for producto in delete_product:
        del inventario[producto]

#Opcion de mostrar:    

    if user_extra == "mostrar":
        for inventory in sorted(inventario.items()):
            product = inventory[0]
            amount = inventory[1]
            print(f"Producto: {product} Cantidad: {amount}")

#Opcion de salir
    elif user_extra == "salir":
        print("Las compras han terminado, gracias por comprar con nosotros")
        break




 