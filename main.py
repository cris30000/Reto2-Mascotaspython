#clases principales


# variables globales
# nuestras variasbles globales son los clientes 

Cliente =[]

class SistemaVeterinaria:
    def __init__(self, veterinarios, clientes, mascotas, citas):
        self.__veterinarios = veterinarios
        self.__clientes = clientes
        self.__mascotas = mascotas
        self.__citas = citas

class Persona:
    id_counter = 1
    def __init__(self, nombre, apellido,contacto, edad):
        self.__id = SistemaVeterinaria.Persona.id_counter
        self.__nombre = nombre
        self.__apellido = apellido
        self.__contacto = contacto
        self.__edad = edad
        
        SistemaVeterinaria.persona.id_counter += 1  
        
class Cliente(Persona):
    def __init__(self, nombre, apellido, edad, dni,direccion):
        super().__init__(nombre, apellido, edad)
        self.__dni = dni    

class Mascotas:
    def __init__(self, nombre, raza, edad):
        self.__nombre = nombre
        self.__raza = raza
        self.__edad = edad
        
class Veterinario(Persona):
    def __init__(self, nombre, apellido, edad, matricula):
        super().__init__(nombre, apellido, edad)
        self.__matricula = matricula
        
class Cita:
    def __init__(self, fecha, hora, cliente, veterinario, mascota):
        self.__fecha = fecha
        self.__hora = hora
        self.__cliente = cliente
        self.__veterinario = veterinario
        self.__mascota = mascota
        
    #Funciones con def
    
    def registrarCliente(self, cliente):
        self.__clientes.append(cliente)
        
    def registrar_Mascota(self, mascota):
        self.__mascotas.append(mascota) 
        
    def programarCita(self, cita):
        self.__citas.append(cita)   
        
    def consultar_historia(self, mascota):
        for cita in self.__citas:
            if cita.mascota == mascota:
                return cita.cliente 
    def crearCita(self, fecha, hora, cliente, veterinario, mascota):
        cita = Cita(fecha, hora, cliente, veterinario, mascota)
        self.__citas.append(cita)
        
    def menu_pricipal():
        while True:
            print("************Menu Principal************")
            print("1. Registrar Cliente")
            print("2. Registrar Mascota")
            print("3. Programar Cita")
            print("4. Consultar Historial de servicios")
            print("5. Salir")
            opcion = input("Ingrese una opcion: ")
            if opcion == "1":
                registrar_cliente()
            elif opcion == "2":
                registrar_mascota()
            elif opcion == "3":
                programar_cita()
            elif opcion == "4":
                consultar_historia()
            elif opcion == "5":
                break
            else:
                print("Opcion invalida")