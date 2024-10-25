import random

# Función para asignar un lugar aleatorio en el sector elegido
def asignar_ubicacion(sector):
    ubicaciones = [f"Ubicación {i+1}" for i in range(10)]  # 10 ubicaciones por sector
    return random.choice(ubicaciones)

# Función principal
def registro_patente():
    # Listas para los sectores
    sectores = {
        '1': ['A', 'B', 'C'],
        '2': ['A', 'B', 'C'],
        '3': ['A', 'B', 'C'],
        '4': ['A', 'B', 'C'],
    }
    
    # Solicitar al usuario que elija un piso
    while True:
        piso = input("Elige un piso (1, 2, 3, 4): ")
        if piso in sectores:
            break
        else:
            print("Piso no válido. Intenta de nuevo.")
    
    # Solicitar al usuario que elija un sector
    while True:
        sector = input(f"Elige un sector en el piso {piso} ({', '.join(sectores[piso])}): ")
        if sector in sectores[piso]:
            break
        else:
            print("Sector no válido. Intenta de nuevo.")
    
    # Asignar ubicación
    ubicacion = asignar_ubicacion(sector)
    print(f"Tu vehículo está estacionado en: Piso {piso}, Sector {sector}, {ubicacion}")
    
    # Registro de patente
    patente = input("Ingresa la patente de tu vehículo: ")
    
    # Guardar la información
    return (patente, piso, sector, ubicacion)

# Función para buscar la ubicación del vehículo
def buscar_vehiculo(patente, registro):
    for entry in registro:
        if entry[0] == patente:
            print(f"Tu vehículo {patente} está en: Piso {entry[1]}, Sector {entry[2]}, {entry[3]}")
            return
    print("Patente no encontrada.")

# Registro de vehículos estacionados
registro = []

# Ciclo principal
while True:
    print("1. Registrar vehículo")
    print("2. Buscar vehículo")
    print("3. Salir")
    opcion = input("Elige una opción: ")

    if opcion == '1':
        registro.append(registro_patente())
    elif opcion == '2':
        patente = input("Ingresa la patente de tu vehículo: ")
        buscar_vehiculo(patente, registro)
    elif opcion == '3':
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")