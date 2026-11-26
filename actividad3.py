
# Configuración de registros del medidor SDM630

power_sdm = {
    "0x00": {
        "phase": "L1",
        "data_format": "Float32",
        "alarm_threshold": 250
    },
    "0x06": {
        "phase": "L1",
        "data_format": "Float32",
        "alarm_threshold": 100
    },
    "0x46": {
        "phase": "System",
        "data_format": "Float32",
        "alarm_threshold": 52
    }
}

# Consultar los registros del medidor SDM630

print("=== CONSULTA DE REGISTROS DEL MEDIDOR SDM630 ===")

intentos = 0
max_intentos = 5

while intentos < max_intentos:
    direccion = input(
        "\nIngrese una direccion hexadecimal (0x00, 0x06, 0x46) "
        "o escriba 'salir': "
    ).strip().lower()

    if direccion == "salir":
        print("Consulta finalizada.")
        break

    registro = power_sdm.get(direccion)

    if registro is not None:
        print("\n=== REGISTRO ENCONTRADO ===")
        print("Direccion:", direccion)
        print("Fase:", registro.get("phase", "No definida"))
        print("Formato de datos:", registro.get("data_format", "No definido"))
        print("Umbral de alarma:", registro.get("alarm_threshold", "No definido"))
    else:
        print("\nError: la direccion ingresada no existe en el diccionario.")

    intentos += 1

if intentos >= max_intentos:
    print("\nSe alcanzo el limite de 5 consultas.")

print("\n=== FIN DE LA CONSULTA ===")