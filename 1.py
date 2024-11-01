def ordenar_matriz_por_patente(registro):
    n = len(registro)
    for i in range(n):
        for j in range(0, n-i-1):
            # Comparar las patentes (registro[j][0] es la patente)
            if registro[j][0] > registro[j+1][0]:
                aux= registro[j]
                registro[j] = registro[j+1]
                registro[j+1] = aux
    return registro   

def buscar_vehiculo_2(registro, piso, letra, ubicacion):
    encontrado = False
    i = 0
    while i < len(registro) and not encontrado:
        if registro[i][1] == piso:
            if registro[i][2] == letra:
                if registro[i][3] == ubicacion:
                    encontrado = True
        i += 1
    return encontrado

def validar_ubicacion_ocupada(registro, piso, letra, ubicacion):
    # Llama a la función buscar_vehiculo_2
    if buscar_vehiculo_2(registro, piso, letra, ubicacion):
        print("La ", ubicacion, " en el piso ", piso , " sector " , letra , " está ocupada.")
        return True  # La ubicación está ocupada
    else:
        print(f"La ubicación {ubicacion} en el piso {piso}, sector {letra} está libre.")
        return False 

# Función para asignar una ubicación en el sector elegido
def asignar_ubicacion(sector):
    ubicaciones = []
    ubicaciones_validas = []
    i = 1
    while i <= num_ubicaciones:
        ubicaciones.append("Ubicación " + str(i))
        ubicaciones_validas.append(i)
        i += 1

    print("Opciones de ubicación:")
    j = 0
    while j < len(ubicaciones):
        if j == len(ubicaciones) - 1:
            print(ubicaciones[j])
            j+=1
        else:
            print(ubicaciones[j], end=", ")
            j += 1
    print()

    seleccion = int(input("Elige una ubicación (escribe el número de la ubicación): "))

    # Validación de la selección
    while seleccion not in ubicaciones_validas:
        print("Elección no válida, por favor selecciona un número entre 1 y", num_ubicaciones)
        seleccion = int(input("Elige una ubicación: "))
    
    return "Ubicación " + str(seleccion)

# Función para registrar una patente
def registro_patente(pisos):
    # Solicitar el piso
    print("Elige un piso:", end=" ")
    for p in pisos:
        print(p, end=" ")
    print()

    piso = int(input("Ingresa el piso: "))
    if piso not in pisos:
        print("Piso no válido, intenta de nuevo.")
        return None  # Manejo de error si el piso no es válido

    # Solicitar el sector
    sector = ""  # Inicializar sector
    while sector not in sectores:  # Mientras el sector no sea válido
        print("Elige un sector en el piso", piso, "(A, B, C):")
        sector = input("Ingresa el sector: ")
        if sector not in sectores:
            print("Sector no válido, intenta de nuevo.")

    # Asignar ubicación
    ubicacion = asignar_ubicacion(sector)
    if validar_ubicacion_ocupada(registro, piso, sector, ubicacion):
        print("No se puede registrar el vehículo porque la ubicación está ocupada.")
        return None  # Si está ocupada, no se registra el vehículo

    print("Tu vehículo está estacionado en: Piso", piso, ", Sector", sector, ",", ubicacion)
    

    # Registro de patente
    patente = input("Ingresa la patente de tu vehículo (máximo 7 caracteres): ")

    while len(patente) == 0 or len(patente) > 7:
        print("Patente no válida. Debe tener un máximo de 7 caracteres.")
        patente = input("Ingresa la patente de tu vehículo: ")

    print("Patente registrada:", patente)
    
    return (patente, piso, sector, ubicacion)



# Función para buscar la ubicación de un vehículo por patente
def buscar_vehiculo(patente, registro):
    encontrado = False
    i = 0
    while i < len(registro) and not encontrado:
        if registro[i][0] == patente:
            print("Tu vehículo", patente, "está en: Piso", registro[i][1], ", Sector", registro[i][2], ",", registro[i][3])
            encontrado = True
        i += 1
    if not encontrado:
        print("Patente no encontrada.")
# 

# Función para generar un informe de los vehículos registrados
def generar_informe(registro):
    if len(registro) == 0:
        print("No hay vehículos registrados.")
    else:
        print("\nInforme de vehículos registrados:")
        print("Patente    Piso    Sector    Ubicación")
        print("--------------------------------------")
        i = 0
        while i < len(registro):
            print(registro[i][0], "    ", registro[i][1], "    ", registro[i][2], "    ", registro[i][3])
            i += 1
        print("--------------------------------------")


# Definición de constantes
num_ubicaciones = 10
sectores = ["A", "B", "C"]
# Crear lista de pisos según la entrada del usuario
num_pisos = int(input("Ingresa la cantidad de pisos que deseas (1-10): "))
while num_pisos < 1 or num_pisos > 10:
    num_pisos = int(input("Ingresa la cantidad de pisos que deseas (1-10): "))

# Generación de la lista de pisos sin usar `range` ni comprensiones
def generar_listapisos(num_pisos):
    pisos=[]
    for i in range(1,num_pisos+1):
        pisos.append(i)
    return pisos

pisos=generar_listapisos(num_pisos)


    

# Registro de vehículos estacionados
registro = []

# Ciclo principal
print("\n1. Registrar vehículo")
print("2. Buscar vehículo")
print("3. Generar informe")
print("4. Ordenar por patentes")
print("5. Salir")
opcion = int(input("Ingresar opción del menú: "))
while opcion != 5:
    # Validación de opciones en el menú principal
    if opcion == 1:
        resultado = registro_patente(pisos)
        if resultado:
            registro.append(resultado)
    elif opcion == 2:
        patente = input("Ingresa la patente de tu vehículo: ")
        buscar_vehiculo(patente, registro)
    elif opcion == 3:
        generar_informe(registro)
    elif opcion == 4:
        ordenar_matriz_por_patente(registro)
    else:
        print("Opción no válida. Intenta de nuevo.")
    print("\n1. Registrar vehículo")
    print("2. Buscar vehículo")
    print("3. Generar informe")
    print("4. Ordenar por patentes")
    print("5. Salir")
    # Pedir la opción nuevamente al usuario
    opcion = int(input("Elige una opción (1-5): "))

print("Saliendo del programa.")

