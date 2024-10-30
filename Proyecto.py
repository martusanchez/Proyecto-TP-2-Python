# Función para asignar un lugar en el sector elegido
def asignar_ubicacion(sector):
    ubicaciones = []
    for i in range(1, 11):  # 10 ubicaciones por sector
        ubicaciones.append("Ubicación " + str(i))  # Agregamos ubicaciones a la lista

    print("Opciones de ubicación:")
    for ubicacion in ubicaciones:  # Imprimimos cada ubicación en una línea
        print(ubicacion, end=", ")
    print()  # Para nueva línea después de imprimir ubicaciones

    seleccion = input("Elige una ubicación (escribe el número de la ubicación, 1-10): ")

    # Verificamos si la selección es válida
    if seleccion.isdigit() and 1 <= int(seleccion) <= 10:  # Verificamos si está en el rango válido
        return "Ubicación " + seleccion  # Retornamos la ubicación seleccionada
    else:
        return "Elección no válida. Por favor, selecciona un número entre 1 y 10."

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
        sector = input(f"Elige un sector en el piso {piso} (A, B, C): ")
        if sector in sectores[piso]:
            break
        else:
            print("Sector no válido. Intenta de nuevo.")
    
    # Asignar ubicación
    ubicacion = asignar_ubicacion(sector)
    
    # Verifica si la asignación de ubicación fue válida
    if "Elección no válida" in ubicacion:
        print(ubicacion)  # Muestra el mensaje de error
        return None  # Termina la función si la elección no fue válida
    
    print(f"Tu vehículo está estacionado en: Piso {piso}, Sector {sector}, {ubicacion}")
    
    # Registro de patente
    patente = input("Ingresa la patente de tu vehículo: ")
    
    # Guardar la información
    return (patente, piso, sector, ubicacion)

# Función para buscar la ubicación del vehículo
def buscar_vehiculo(patente, registro):
    for entrada in registro:  # Cambiado 'entry' a 'entrada'
        if entrada[0] == patente:
            print(f"Tu vehículo {patente} está en: Piso {entrada[1]}, Sector {entrada[2]}, {entrada[3]}")
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
        resultado = registro_patente()
        if resultado:  # Solo agrega al registro si no es None
            registro.append(resultado)
    elif opcion == '2':
        patente = input("Ingresa la patente de tu vehículo: ")
        buscar_vehiculo(patente, registro)
    elif opcion == '3':
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")
