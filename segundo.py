class Empleado:
    def __init__(self):
        self.nombre=''
        self.departamento=''

    def set(self,nombre,departamento):
        self.nombre=nombre
        self.departamento=departamento

    def imprimir(self):
        print(self.nombre)
        print(self.departamento)

class Gestor(Empleado):

    def __init__(self):
        super().__init__()
        self.informes=[1,2,3,4]


class Trabajador(Empleado):

    def __init__(self):
        super().__init__()
        self.proyectos=['proyecto 1','proyecto 2']



class Comercial(Trabajador):

    def __init__(self):
        super().__init__()
        self.participacion=4.5


class Ingeniero(Trabajador):

    def __init__(self):
        super().__init__()
        self.area='El area es :45 u**2'



ing1=Ingeniero()
ing1.set('Victor Salazar','Lima')
ing1.imprimir()
ing1.



