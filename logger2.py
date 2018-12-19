def log(debug  =False):
    def _log(f): #decorador de nombre _log
        def wrap(a,b): #funcion que extiende las fucionanildades de sums=F
            if debug:
            print('valor a :',a)
            print('valor b :',b)
        return f(a,b)
    return wrap
@log(debug=True)
def suma (a,b):
    return a+b
print(suma(1,2))


