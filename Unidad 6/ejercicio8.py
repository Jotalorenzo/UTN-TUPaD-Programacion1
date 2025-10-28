def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = input("Ingrese su peso en kg: ")
altura = input("Ingrese su altura en metros: ")

imc = calcular_imc(peso, altura)
print(f"Su Índice de Masa Corporal (IMC) es: {imc}")

