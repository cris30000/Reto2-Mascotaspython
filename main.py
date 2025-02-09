#prueba 1 RETO 2 SISTEMA VETERINARIO ELABORADO POR CRISTINA SAMBONI SANDOVAL 2/02/2025

# Variables globales que se usan en todo el programa
clientes = []
mascotas = []
citas = []  # Agregamos la lista global de citas

YELLOW = '\033[93m'
RESET='\033[97m'
BLUE= '\033[94m'
GREEN= '\033[92m'
WHITE= '\033[97m'
RED = '\033[91m'

# Clases principales
class SistemaVeterinaria:
    class Persona:
        id_counter = 1

        def __init__(self, nombre, contacto):  # Constructor de la clase Persona
            self.id = SistemaVeterinaria.Persona.id_counter
            self.nombre = nombre
            self.contacto = contacto
            SistemaVeterinaria.Persona.id_counter += 1  # Autoincrementa el ID para cada nueva persona

    class Cliente(Persona):
        def __init__(self, nombre, contacto, direccion):  # Constructor de la clase Cliente
            super().__init__(nombre, contacto)
            self.direccion = direccion
            self.mascotas = []

        def agregar_mascota(self, mascota):  # Método para agregar mascotas al cliente
            self.mascotas.append(mascota)

    class Mascota:
        id_counter = 1

        def __init__(self, nombre, especie, raza, edad):  # Constructor de la clase Mascota
            self.id = SistemaVeterinaria.Mascota.id_counter
            self.nombre = nombre
            self.especie = especie
            self.raza = raza
            self.edad = edad
            self.historia_clinica = []
            SistemaVeterinaria.Mascota.id_counter += 1
            
                    print(f"- Tu mascota {self.nombre} tuvo una cita de {cita.servicio} el día {cita.fecha} a las {cita.hora} con el veterinari@ {cita.veterinario}")

    class Cita:
        id_counter = 1

        def __init__(self, fecha, hora, servicio, veterinario, mascota):  # Constructor de la clase Cita
            self.id = SistemaVeterinaria.Cita.id_counter
            self.fecha = fecha
            self.hora = hora
            self.servicio = servicio
            self.veterinario = veterinario
            self.mascota = mascota
            SistemaVeterinaria.Cita.id_counter += 1


# Funciones principales


def registrar_cliente():
    
    
    print(f"{YELLOW}***** BIENVENIDO A LA APLICACIÓN DE SISTEMA VETERINARIO ***** ")
    print("\n")
    print(f"{GREEN}1. *******INGRESE LOS DATOS DEL CLIENTE*******")
    print(f"{WHITE}\n")
    nombre = input("Ingrese el nombre del cliente: ")
    contacto = input("Ingrese el contacto del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    cliente = SistemaVeterinaria.Cliente(nombre, contacto, direccion)
    clientes.append(cliente)
    print(f"{BLUE}\n¡Cliente registrado con éxito! con ID: {cliente.id}\n")


def registrar_mascota():
    print(f"{BLUE}***** AHORA INGRESA LOS DATOS DE LA MASCOTA *****")
    print(f"{WHITE}\n")
    cliente_id = int(input("Ingrese el ID del cliente para asociar la mascota: "))
    cliente = next((c for c in clientes if c.id == cliente_id), None)

    if not cliente:
        print("Cliente no encontrado.")
        return

    nombre_mascota = input("Ingrese el nombre de la mascota: ")
    especie = input("Ingrese la especie de la mascota: ")
    raza = input("Ingrese la raza de la mascota: ")
    edad = input("Ingrese la edad de la mascota: ")

    mascota = SistemaVeterinaria.Mascota(nombre_mascota, especie, raza, edad)
    cliente.agregar_mascota(mascota)
    mascotas.append(mascota)
    print(f"{BLUE}\n¡¡¡Mascota registrada con éxito!!!, ID: {mascota.id}\n")


def programar_cita():
    print(f"{BLUE}***** PROGRAMAR UNA CITA *****")
    cliente_id = int(input("Ingrese el ID del cliente: "))
    cliente = next((c for c in clientes if c.id == cliente_id), None)

    if not cliente:
        print("Cliente no encontrado.")
        return

    mascota_nombre = input("Ingrese el nombre de la mascota: ")
    mascota = next((m for m in cliente.mascotas if m.nombre == mascota_nombre), None)

    if not mascota:
        print("Mascota no encontrada.")
        return

    fecha = input("Ingrese la fecha de la cita (dd/mm/yyyy): ")
    hora = input("Ingrese la hora de la cita (HH:MM): ")
    servicio = input("Ingrese el tipo de servicio (Vacunacion, Consulta, Examen, otras): ")
    veterinario = input("Ingrese el nombre del veterinario: ")

    cita = SistemaVeterinaria.Cita(fecha, hora, servicio, veterinario, mascota)
    mascota.agregar_historia(cita)
    citas.append(cita)  # Agrega la cita a la lista global

    print(f"{BLUE}\n***** CITA PROGRAMADA EXITOSAMENTE *****\n")


def consultar_historia():
    print(f"{BLUE}***** CONSULTAR HISTORIA CLÍNICA *****")

    cliente_id = int(input("Ingrese el ID del cliente: "))
    cliente = next((c for c in clientes if c.id == cliente_id), None)

    if not cliente:
        print("Cliente no encontrado.")
        return

    mascota_nombre = input("Ingrese el nombre de la mascota: ")
    mascota = next((m for m in cliente.mascotas if m.nombre == mascota_nombre), None)

    if not mascota:
        print("Mascota no encontrada.")
        return

    mascota.mostrar_historial()


def mostrar_clientes():
    print(f"{BLUE}***** LISTA DE CLIENTES *****")
    for cliente in clientes:
        print(f"ID: {cliente.id}, Nombre: {cliente.nombre}, Contacto: {cliente.contacto}, Dirección: {cliente.direccion}")


def mostrar_mascotas():
    print(f"{BLUE}***** LISTA DE MASCOTAS *****")
    for mascota in mascotas:
        print(f"ID: {mascota.id}, Nombre: {mascota.nombre}, Especie: {mascota.especie}, Raza: {mascota.raza}, Edad: {mascota.edad}")


def mostrar_citas():
    print(f"{BLUE}***** LISTA DE CITAS *****")
    for cita in citas:
        print(f"ID: {cita.id}, Fecha: {cita.fecha}, Hora: {cita.hora}, Servicio: {cita.servicio}, Veterinario: {cita.veterinario}, Mascota: {cita.mascota.nombre}")


def mostrar_menu():
    print(f"{YELLOW}***** BIENVENIDO A LA APLICACIÓN DE SISTEMA VETERINARIO ***** {RESET}\n")# alt 92 para sacar el baseslach
    print(f"{GREEN}1. Registrar cliente")
    print("2. Registrar mascota")
    print("3. Programar cita")
    print("4. Consultar historia clínica")
    print("5. Mostrar clientes")
    print("6. Mostrar mascotas")
    print("7. Mostrar citas")
    print("8. Salir")

    opcion = input("Ingrese una opción: ")
    return opcion


if __name__ == "__main__":
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            registrar_cliente()
        elif opcion == "2":
            registrar_mascota()
        elif opcion == "3":
            programar_cita()
        elif opcion == "4":
            consultar_historia()
        elif opcion == "5":
            mostrar_clientes()
        elif opcion == "6":
            mostrar_mascotas()
        elif opcion == "7":
            mostrar_citas()
        elif opcion == "8":
            print("Gracias por utilizar nuestro Sistema Veterinario. ¡Hasta pronto!")
            break