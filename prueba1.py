# Variables globales
clientes = []  # Esta variable global almacena la información de los clientes con sus mascotas

# Clases principales
class SistemaVeterinaria:
    class Persona:
        id_counter = 1
        def __init__(self, nombre, contacto):
            self.id = SistemaVeterinaria.Persona.id_counter
            self.nombre = nombre
            self.contacto = contacto
            SistemaVeterinaria.Persona.id_counter += 1  # Autoincrementa el ID para cada nueva persona

    class Cliente(Persona):
        def __init__(self, nombre, contacto, direccion):
            super().__init__(nombre, contacto)
            self.direccion = direccion
            self.mascotas = []
            
        def agregar_mascota(self, mascota):
            self.mascotas.append(mascota)

    class Mascota:
        id_counter = 1
        def __init__(self, nombre, especie, raza, edad):
            self.id = SistemaVeterinaria.Mascota.id_counter
            self.nombre = nombre
            self.especie = especie
            self.raza = raza
            self.edad = edad
            self.historia_clinica = []
            SistemaVeterinaria.Mascota.id_counter += 1

    class Citas:
        id_counter = 1
        def __init__(self, fecha, hora, servicio, veterinario):
            self.id = SistemaVeterinaria.Citas.id_counter
            self.fecha = fecha
            self.hora = hora
            self.servicio = servicio
            self.veterinario = veterinario
            SistemaVeterinaria.Citas.id_counter += 1

# Funciones principales
def registrar_cliente():
    print("***** INGRESE LOS DATOS DEL CLIENTE *****")
    nombre = input("Ingrese el nombre del cliente: ")
    contacto = input("Ingrese el contacto del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    cliente = SistemaVeterinaria.Cliente(nombre, contacto, direccion)
    
    print("***** AHORA  INGRESA LOS DATOS DE LA MASCOTA *****")
    nombre_mascota = input("Ingrese el nombre de la mascota: ")
    especie = input("Ingrese la especie de la mascota: ")
    raza = input("Ingrese la raza de la mascota: ")
    edad = input("Ingrese la edad de la mascota: ")
    
    mascota = SistemaVeterinaria.Mascota(nombre_mascota, especie, raza, edad)
    cliente.agregar_mascota(mascota)
    clientes.append(cliente)
    print("\n!!!!Cliente y mascota registrados con éxito!!! \n  ")

def programar_cita():
    print("***** PROGRAMAR UNA CITA *****")
    fecha = input("Ingrese la fecha de la cita (dd/mm/yyyy): ")
    hora = input("Ingrese la hora de la cita (HH:MM): ")
    servicio = input("Ingrese el tipo de servicio: ")
    veterinario = input("Ingrese el nombre del veterinario: ")
    cita = SistemaVeterinaria.Citas(fecha, hora, servicio, veterinario)
    print("\n ***** CITA PROGRAMADA EXITOSAMENTE *****\n")

def consultar_historia():
    print("Consultar historial de citas")
    
    cliente_id = int(input("Ingrese el ID del cliente: "))
    cliente = next((c for c in clientes if c.id == cliente_id), None)
    
    if not cliente:
        print("Cliente no encontrado.")
        return
    
    mascota_nombre = int(input("Ingrese el nombre del mascota: "))
    mascota = next((m for m in cliente.mascotas if m.nombre_mascota == mascota_nombre), None)
    
    if not mascota:
        print("Mascota no encontrado.")
        return

    mascota.mostar_historial()


  

# Menú principal
def menu_principal():
    while True:
        print("Bienvenido al Sistema Veterinario")
        print("1. Registrar Cliente y Mascota")
        print("2. Programar Cita")
        print("3. Consultar Historia Clínica")
        print("4. Salir")
        opc = input("Ingrese una opción: ")
        
        if opc == "1":
            registrar_cliente()
        elif opc == "2":
            programar_cita()
        elif opc == "3":
            consultar_historia()
        elif opc == "4":
            print("Gracias por usar el Sistema Veterinario. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida")

menu_principal()