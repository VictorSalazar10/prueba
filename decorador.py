def decorador(funcion):  # nombre del decorador y nombre de la funcion
    def funcion__envoltura():  # Funcion que anade funcionalidades a la funcion funcion
        print('Antes de la funcion')  # cambio antes de la ejecucion
        funcion()  # ejecuta la funcion
        print('Despues de la funcion')  # hace algo despues

    return funcion__envoltura


@decorador
def funcionPrueba():
      print('Hola funcion')


funcionPrueba()
