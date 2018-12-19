import time
hora=time.strftime("%H:%M:%S")
x=(hora.split(':'))

print(int x(0))
# def decorador(funcion):
#     def cambio():
#         if int(x[0])>=10 and int(x[0])<=16:
#             funcion()
#         else:
#             print('No se mueve la mano pq no es el horario correcto')
#     return cambio
#
# @decorador
# def mover_mano_robot():
#     print('Moviendo mano robot')
#
# mover_mano_robot()