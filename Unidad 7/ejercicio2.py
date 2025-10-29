import ejercicio1

def actualizar_precio(nombre, nuevo_precio):
    lista = ejercicio1.precio_frutas
    if nombre in lista:
        ejercicio1.precio_frutas[nombre] = nuevo_precio
        print(f"El precio de '{nombre}' ha sido actualizado a {nuevo_precio}.")
    else:
        print(f"El producto '{nombre}' no existe en el lista.")

while True:
    actualizar_precio("Banana", 1330)
    actualizar_precio("Manzana", 1700)
    actualizar_precio("Melon", 2800)
    break

lista_actualizada = ejercicio1.precio_frutas
print(lista_actualizada)