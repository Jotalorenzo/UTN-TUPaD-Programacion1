contactos = {}

def agregar_contacto(nombre, telefono):
    contactos[nombre] = telefono
    return contactos

while True:
    contacto = input("Ingrese el nombre del contacto ")
    telefono = input("Ingrese el número de teléfono ")
    agregar_contacto(contacto, telefono)
    continuar = input("¿Desea agregar otro contacto? (s/n) ")
    if continuar.lower() != 's':
        break

print(contactos)

