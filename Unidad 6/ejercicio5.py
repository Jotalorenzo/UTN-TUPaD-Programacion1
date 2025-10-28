def segundos_a_horas(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos_restantes = segundos % 60
    print(f"{segundos} segundos son {horas} horas, {minutos} minutos y {segundos_restantes} segundos.")

segundos_a_horas(int(input("Ingrese la cantidad de segundos a convertir: ")))