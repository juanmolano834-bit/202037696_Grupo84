sistema_activo = True
temperatura = 110
umbral_emergencia = 130
lecturas = 0
max_lecturas = 10

while sistema_activo and lecturas < max_lecturas:
    if temperatura > umbral_emergencia:
        print("Temperatura:", temperatura, "°C")
        print("ALERTA CRÍTICA: Parada de emergencia")
        sistema_activo = False

    elif temperatura < 115:
        print("Temperatura:", temperatura, "°C")
        print("Estado: Calentando autoclave")
        temperatura += 2

    elif temperatura >= 115 and temperatura <= 121:
        print("Temperatura:", temperatura, "°C")
        print("Estado: Fase estable de esterilización")
        temperatura += 1

    else:
        print("Temperatura:", temperatura, "°C")
        print("Estado: Enfriamiento activo")
        temperatura -= 3

    lecturas += 1