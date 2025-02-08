#variables globales que se usan en todo el programa
clientes = []
mascotas = []   

#Clases principales
class SistemaVeterinaria:
    class Persona:
        id_counter = 1
        def __init__(self, nombre, contacto): # Constructor de la clase Persona
            self.id = SistemaVeterinaria.Persona.id_counter
            self.nombre = nombre
            self.contacto = contacto
            SistemaVeterinaria.Persona.id_counter += 1  # Autoincrementa el ID para cada nueva persona
            
    class Cliente(Persona):
        def __init__(self, nombre, contacto, direccion): # Constructor de la clase Cliente
            super().__init__(nombre, contacto)
            self.direccion = direccion  
            self.mascotas = []
            
        def agregar_mascota(self, mascota): # Método para agregar mascotas al cliente
            self.mascotas.append(mascota)
            
            
    class Mascota:
        id_counter = 1
        def __init__(self, nombre, especie, raza, edad): # Constructor de la clase Mascota
            self.id = SistemaVeterinaria.Mascota.id_counter
            self.nombre = nombre
            self.especie = especie
            self.raza = raza
            self.edad = edad
            self.historia_clinica = []
            SistemaVeterinaria.Mascota.id_counter += 1
        def agregar_historia(self, cita): # Método para agregar citas a la historia clínica de la mascota
            self.historia_clinica.append(cita)
            
        def mostrar_historial(self): # Método para mostrar el historial clínico de la mascota
            if not self.historia_clinica:
                print("No hay historial clínico para esta mascota.")
            else:
                print(f"\nHistorial clínico de {self.nombre}:")
                for cita in self.historia_clinica:
                    print(f"- Tu mascota {self.nombre} tuvo una cita de {cita.servicio} el  dia {cita.fecha} a las {cita.hora} con el veterinario {cita.veterinario}")
    
    class Cita:
        id_counter = 1
        def __init__(self, fecha, hora, servicio, veterinario, mascota): # Constructor de la clase Cita
            self.id = SistemaVeterinaria.Cita.id_counter
            self.fecha = fecha
            self.hora = hora
            self.servicio = servicio
            self.veterinario = veterinario
            self.mascota = mascota
            SistemaVeterinaria.Cita.id_counter += 1

#Funciones principales
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
    
"""def registrar_mascota():
    print("***** AHORA  INGRESA LOS DATOS DE LA MASCOTA *****")
    nombre_mascota = input("Ingrese el nombre de la mascota: ")
    especie = input("Ingrese la especie de la mascota: ")
    raza = input("Ingrese la raza de la mascota: ")
    edad = input("Ingrese la edad de la mascota: ")
    
    mascota = SistemaVeterinaria.Mascota(nombre_mascota, especie, raza, edad)
    mascotas.append(mascota)
    print("\n¡Mascota registrada con éxito!\n") 
    
def registrar_cita():
    pass
    print("***** INGRESE LOS DATOS DE LA CITA *****")
    fecha = input("Ingrese la fecha de la cita: ")
    hora = input("Ingrese la hora de la cita: ")
    servicio = input("Ingrese el servicio de la cita: ")
    veterinario = input("Ingrese el veterinario de la cita: ")
    mascota = input("Ingrese el nombre de la mascota: ")
    
    cita = SistemaVeterinaria.Cita(fecha, hora, servicio, veterinario, mascota)
    citas.append(cita)
    print("\n¡Cita registrada con éxito!\n")     """      
    
def mostrar_clientes():
    print("***** LISTA DE CLIENTES *****")
    for cliente in clientes:
        print(f"ID: {cliente.id}, Nombre: {cliente.nombre}, Contacto: {cliente.contacto}, Direccion: {cliente.direccion}")
        
        
def mostrar_mascotas():
    print("***** LISTA DE MASCOTAS *****")
    for mascota in mascotas:
        print(f"ID: {mascota.id}, Nombre: {mascota.nombre}, Especie: {mascota.especie}, Raza: {mascota.raza}, Edad: {mascota.edad}")
        
def mostrar_citas():
    pass    

    """for cita in citas:   
        print(f"ID: {cita.id}, Fecha: {cita.fecha}, Hora: {cita.hora}, Servicio: {cita.servicio}, Veterinario: {cita.veterinario}, Mascota: {cita.mascota}")""" 
        
def mostrar_menu():
    print("***** BIENVENIDO A LA APLICACIÓN DE SISTEMA VETERINARIO *****")
    print("1. Registrar cliente")    
    print("2. Registrar mascota")
    print("3. Registrar cita")    
    print("4. Mostrar clientes")
    print("5. Mostrar mascotas")    
    print("6. Mostrar citas")
    print("7. Salir")
    
    opcion = input("Ingrese una opcción: ")
    return opcion   

if __name__ == "__main__":    
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            registrar_cliente()
        elif opcion == "2":
            pass #registrar_mascota()
        elif opcion == "3":
            pass #registrar_cita()
        elif opcion == "4":
            mostrar_clientes()
        elif opcion == "5":
            mostrar_mascotas()
        elif opcion == "6":
            mostrar_citas()
        elif opcion == "7":
            print("Gracias por usar el Sistema Veterinario. ¡Hasta pronto!")
            break
         
    
    
     
              
    