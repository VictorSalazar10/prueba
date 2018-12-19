def decor(func):
    def wrap():
        print('='*12)
        func()
        print('='*12)

    return wrap #retorno el metodo wrap

def decor2(f): #como parametro se pasa una funcion que va en el parametro F
    def xxx():  #Funcion que va extender la funcionalidad de la funcion basica
        f()     #Se ejecuta la funcion
        print('decor2') #Se agrega algo a la funcion basica

    return xxx

@decor2
@decor
def print_text():
    print('hola mundo')
    a=5



print_text()