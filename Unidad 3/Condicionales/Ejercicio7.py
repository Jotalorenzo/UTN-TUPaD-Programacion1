# Ejercicio 7: cadenas

frase : str = input("Ingrese una frase o palabra: ")
frase = frase.lower().strip()

if frase and frase[-1] in "aeiou":
    print(frase + "!")
else:
    print(frase)

    


