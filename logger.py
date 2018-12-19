def log(f):
    def wrap(a,b):
        print('valor a :',a)
        print('valor b :',b)
        return f(a,b)
    return wrap
@log
def suma (a,b):
    return a+b
print(suma(1,2))


