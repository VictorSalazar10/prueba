class ClaseEjemplo:
    def publico (self):
        print('Soy publico')

    def __private(self):
        print('Soy privado')#Esta funcion en privada

ejemplo=ClaseEjemplo()
ejemplo.publico()
ejemplo.__private()
