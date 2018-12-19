class Vehiculo:

    def __init__(self):
        self.__color='color privada'
        self.__ruedas='ruedas privada '

    def set_ruedas(self,valor):
        self.__ruedas=valor
    def get_ruedas(self):
        return  self.__ruedas

    def set_color(self, valor):
        self.__color = valor

    def get_color(self):
        return self.__color

class Coche(Vehiculo):
    def __init__(self):
        # super().__init__()
        self.velocidad='velocdiad en km/h'
        self.cilindrada='cilindrada en CC'


carro=Coche()
carro.set_color('verde')
print(carro.get_color())
