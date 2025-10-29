precio_frutas = {
    'Banana': 1200,
    'Ananas': 2500,
    'Melon': 3000,
    'Uva': 1450
    }

def agregar_fruta(nombre, precio):

    precio_frutas[nombre] = precio

    return precio_frutas

while True:
    agregar_fruta("naranja", 1200)
    agregar_fruta("Manzana", 1500)
    agregar_fruta("Pera", 2300)
    break

print(precio_frutas)
