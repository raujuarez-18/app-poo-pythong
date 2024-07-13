class Persona:

    def __init__(self, nombre, apellido, dni, email):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.email = email
        
    def saludar (self):
        print(f"Hola, Soy el objeto {self.nombre}")
