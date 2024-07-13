class Curso:
    def __init__(self, codigo, nombre, credito):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__credito = credito
    
    def bienvenido(self):
        print (f"Bienvenido al curso {self.__nombre} tengo {self.__credito} crédito")

    def set_codigo(self,codigo):
        self.__codigo= codigo
    def set_nombre(self, nombre):
        self.__nombre= nombre
    def set_credito(self, credito):
        self.__credito= credito
    def get_codigo(self):
        return self.__codigo
    def get_nombre(self):
        return self.__nombre
    def get_credito(self):
        return self.__credito
