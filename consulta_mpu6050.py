# PASO 4: SCRIPT DE CONSULTA SEGURA
# ESCENARIO 2: SENSOR MPU6050
# Curso: Lenguajes Interpretados
# =====================================================

# Diccionario anidado con los registros del sensor
registro_mpu = {
    "0x3B": {
        "register_name": "ACCEL_XOUT_H",
        "bit_mask": 0xFF,
        "sampling_rate": 1000
    },
    "0x3D": {
        "register_name": "ACCEL_YOUT_L",
        "bit_mask": 0xE0,
        "sampling_rate": 1000
    },
    "0x6B": {
        "register_name": "PWR_MGMT_1",
        "bit_mask": 0x40,
        "sampling_rate": 100
    }
}

# Limite maximo de consultas
MAX_CONSULTAS = 5


# Funcion para consultar por direccion o nombre
def consultar_registro(busqueda):
    busqueda = busqueda.strip()
    busqueda_mayuscula = busqueda.upper()

    # Buscar primero por direccion exacta
    datos = registro_mpu.get(busqueda)
    direccion = busqueda if datos is not None else None

    # Si no encuentra la direccion, comparar sin distinguir mayusculas
    if datos is None:
        for clave, informacion in registro_mpu.items():

            if clave.upper() == busqueda_mayuscula:
                datos = informacion
                direccion = clave
                break

            nombre = informacion.get("register_name", "")

            if nombre.upper() == busqueda_mayuscula:
                datos = informacion
                direccion = clave
                break

    # Mostrar las especificaciones del registro
    if datos is not None:
        print("\n--- REGISTRO ENCONTRADO ---")
        print("Direccion:", direccion)
        print("Nombre:", datos.get("register_name"))
        print("Mascara de bits:", hex(datos.get("bit_mask")))
        print(
            "Frecuencia de muestreo:",
            datos.get("sampling_rate"),
            "Hz"
        )
    else:
        print("\nCONSULTA ERRONEA CONTROLADA")
        print("No existe un registro con esa direccion o nombre.")


# Programa principal
print("========================================")
print(" CONSULTA DE REGISTROS DEL SENSOR MPU6050")
print("========================================")
print("Busque por direccion hexadecimal o nombre.")
print("Ejemplos: 0x3B, 0x3D, 0x6B")
print("Tambien puede escribir ACCEL_XOUT_H.")
print("Escriba SALIR para terminar.")

# Ciclo limitado a cinco consultas
for intento in range(MAX_CONSULTAS):
    print(f"\nConsulta {intento + 1} de {MAX_CONSULTAS}")

    busqueda = input("Ingrese direccion o nombre: ")

    if busqueda.strip().upper() == "SALIR":
        print("Programa finalizado por el usuario.")
        break

    consultar_registro(busqueda)

else:
    print("\nSe alcanzo el limite de consultas.")
    print("Programa finalizado de forma segura.")