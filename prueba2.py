#variables globales que se usan en todo el programa
clientes = []
mascotas = [] 
citas= []
 

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
    clientes.append(cliente)
    print(f"\n¡Cliente registrado con éxito! con ID: {cliente.id}\n")
    


    
def registrar_mascota():
    
    print("***** AHORA  INGRESA LOS DATOS DE LA MASCOTA *****")
    cliente_id = int(input("Ingrese el ID del cliente para asociart la mascota: "))
    # y hacems la busqueda del cliente
    
    cliente= next((c for c in clientes if c.id == cliente_id), None)
    
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
    print(f"\n!!!!Mascota registrados con éxito!!!, ID: {mascota.id} \n  ")
    

    

    

def programar_cita():
    print("***** PROGRAMAR UNA CITA *****")
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
    
    

    cita = SistemaVeterinaria.Cita (fecha, hora, servicio, veterinario, mascota)
    mascota.agregar_historia(cita)

    print("\n***** CITA PROGRAMADA EXITOSAMENTE *****\n")
  
def mostrar_clientes():
    print("***** LISTA DE CLIENTES *****")
    for cliente in clientes:
        print(f"ID: {cliente.id}, Nombre: {cliente.nombre}, Contacto: {cliente.contacto}, Direccion: {cliente.direccion}")
        
        
def mostrar_mascotas():
    print("***** LISTA DE MASCOTAS *****")
    for mascota in mascotas:
        print(f"ID: {mascota.id}, Nombre: {mascota.nombre}, Especie: {mascota.especie}, Raza: {mascota.raza}, Edad: {mascota.edad}")
        
"""def mostrar_citas():
    print("***** LISTA DE CITAS *****")  

    for cita in citas:   
        print(f"ID: {cita.id}, Fecha: {cita.fecha}, Hora: {cita.hora}, Servicio: {cita.servicio}, Veterinario: {cita.veterinario}, Mascota: {cita.mascota}")
  """
def mostrar_citas():
    print("***** LISTA DE CITAS *****")
    
    for cita in citas:   
        print(f"ID: {cita.id}, Fecha: {cita.fecha}, Hora: {cita.hora}, Servicio: {cita.servicio}, Veterinario: {cita.veterinario}, Mascota: {cita.mascota.nombre}")
      
def mostrar_menu():
    print("***** BIENVENIDO A LA APLICACIÓN DE SISTEMA VETERINARIO *****")
    print("1. Registrar cliente")    
    print("2. Registrar mascota")
    print("3. Programar cita")    
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
            registrar_mascota()
        elif opcion == "3":
            programar_cita()
        elif opcion == "4":
            mostrar_clientes()
        elif opcion == "5":
            mostrar_mascotas()
        elif opcion == "6":
            mostrar_citas()
        elif opcion == "7":
            print("Gracias por usar el Sistema Veterinario. ¡Hasta pronto!")
            break
         
    
    
     
              
    