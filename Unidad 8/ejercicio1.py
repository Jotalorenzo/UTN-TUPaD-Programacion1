import os

archivo = "productos.txt"

# Punto 1: 
if not os.path.exists(archivo):
    with open(archivo, "w", encoding="utf-8") as f:
        f.write("Lapicera,120.5,30\n")
        f.write("Cuaderno,250,50\n")
        f.write("Mochila,1200,15\n")

# Punto 2 y 4: 
productos = []
with open(archivo, "r", encoding="utf-8") as f:
    for linea in f:
        linea = linea.strip()
        if linea:
            partes = linea.split(",")
            if len(partes) == 3:
                nombre, precio, cantidad = partes
                producto = {
                    "nombre": nombre,
                    "precio": float(precio),
                    "cantidad": int(cantidad)
                }
                productos.append(producto)
            else:
                print(f"Línea ignorada por formato incorrecto: {linea}")

# Punto 2:
print("---- Productos actuales ----")
for p in productos:
    print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")

# Punto 3: 
while True:
    print("\nIngrese un nuevo producto o escriba 'salir' para terminar:")
    nuevo_nombre = input("Nombre: ").strip()
    if nuevo_nombre.lower() == "salir":
        break

    nuevo_precio = float(input("Precio: "))
    nueva_cantidad = int(input("Cantidad: "))

    nuevo_producto = {
        "nombre": nuevo_nombre,
        "precio": nuevo_precio,
        "cantidad": nueva_cantidad
    }
    productos.append(nuevo_producto)
    print(f"Producto '{nuevo_nombre}' agregado correctamente.")

# Punto 5: 
busqueda = input("\nIngrese el nombre del producto a buscar: ").strip()
encontrado = False
for p in productos:
    if p['nombre'].lower() == busqueda.lower():
        print(f"Producto encontrado: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print("Error: Producto no encontrado.")

# Punto 6: 
with open(archivo, "w", encoding="utf-8") as f:
    for p in productos:
        f.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

print("\nProductos actualizados guardados correctamente.")
