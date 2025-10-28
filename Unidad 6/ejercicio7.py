def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        division = "Error: División por cero"
    
    return {suma, resta, multiplicacion, division}


a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
resultado = operaciones_basicas(a, b)

