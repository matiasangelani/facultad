'''
Se tiene una Cola de procesos que necesitan ocupar la CPU. De cada proceso se conoce el nombre, tipo de proceso, tamaño, prioridad, fecha y hora de la última modificación. Se deberá desarrollar una aplicación, utilizando los TADs que crea necesarios. Se desea tener un menú con los siguientes puntos:
a) Encolar proceso
b) Modificar la prioridad del proceso
c) Desencolar proceso
d) Listado de procesos
e) Dado un determinado mes, modificar la prioridad de los procesos a baja
f) Eliminar los procesos cuyo tipo sea igual al ingresado
g) Generar una cola con aquellos procesos cuya última modificación se encuentre entre dos horas dadas
'''

'''
Lista de TADs

  tadProceso
    Voy a querer un CRUD de procesos (mostrar individual y toda la cola)

'''

#Importo TAD
#import tads.tadProcesos

from tads.processesTAD import *

def menu():
  print('\n\n', format(' SELECCIONAR UNA OPCION ', '=^50'))
  print('\n1. Encolar Proceso')
  print('\n',format(' Presione 0 para finalizar ', '*^40'))

  option = int(input('Opcion: '))

  return option

queue = createQueue()

option = menu()

while option != 0:
  # if option == 0:
  #   print('\nPrograma terminado')
  if option < 1 or option > 7:
    print('\nLa opcion ingresada es incorrecta, vuelva a intentarlo')
    option = menu()
  else:
    option = menu()

print('\nPrograma terminado')

#print('Message: ', queue)

#Menu





# name = input('Input process name: ')
# type = input('Input process type: ')
# size = input('Input process size: ')
# priority = input('Input process priority: ')
# date = input('Input process date: ')
# hour = input('Input process hour: ')


