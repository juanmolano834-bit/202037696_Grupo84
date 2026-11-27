# ESCENARIO 2: Dosificación de Presión en Red de Gas Natural
# Transductor XMLP010BC71F
# Carlos Andres Legro

presion = float(input("Ingrese la presión inicial en Bar: "))
for lectura in range(10):
    print(f"\nLectura {lectura + 1}: {presion:.2f} Bar")
    if presion >= 6.0:
        print("CRÍTICO: Ruptura inminente. Abortar.")
        break
    elif presion < 2.0:
        print("Acción: Inyectando presión a la red")
        presion += 0.5
    elif 2.0 <= presion <= 4.5:
        print("Acción: Flujo nominal estabilizado")
        presion += 0.1
    else:
        print("Acción: Purga de emergencia abierta")
        presion -= 0.8