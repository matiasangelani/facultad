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

from os import system
from time import sleep
from tads.processesTAD import *

def menu():
  system('clear')
  print('\n\n', format(' SELECCIONAR UNA OPCION ', '=^50'))
  print('\n1. Encolar proceso')
  print('\n2. Modificar prioridad de proceso')
  print('\n3. Desencolar proceso')
  print('\n4. Listar todos procesos')
  print('\n5. Cambiar a prioridad baja todos los procesos dado un mes')
  print('\n6. Eliminar todos los procesos de un tipo particular')
  print('\n7. Generar nueva cola a partir de intervalo horario')
  #print('\n8. Listar un proceso')

  print('\n',format(' Presione 0 para finalizar ', '*^40'))

  option = input('\nOpcion: ')

  #option = verifyInt(option)
  try:
    option = int(option)
  except ValueError:
    print('\nDato ingresado incorrecto')
    option = -1

  return option

queue = createQueue()

option = menu()

while option != 0:
  if option < 1 or option > 7:
    print('\n\nLa opcion ingresada es incorrecta, vuelva a intentarlo')
    input('\n\nPresione enter para continuar')

    option = menu()
  else:
    if option == 1:
      process = createProcess()
      name = input('\nIngresar nombre: ')
      print('\nTipo')
      print('1. KERNEL')
      print('2. USUARIO')
      processType = input('\nIngresar: ')
      size = input('\nIngresar tamaño: ')
      print('\nPrioridad')
      print('1. LOW')
      print('2. MID')
      print('3. HIGH')
      priority = input('Ingresar: ')
      date = input('\nFecha (YYYY-MM-DD): ')
      hour = input('\nHora (hh:mm): ')

      response = addProcess(queue, process, name, processType, size, priority, date, hour)
      
      if response:
        print('\n', response)

    elif option == 2:
      id = input('\nIngresar ID de proceso: ')
      print('\n1. LOW')
      print('2. MID')
      print('3. HIGH')
      priority = input('\nSeleccionar prioridad: ')
      response = modPriority(queue, id, priority)

      if response:
        print('\n', response)

    elif option == 3:
      id = input('\nIngresar ID de proceso: ')
      response = delProcess(queue, id)

      print(response)

    elif option == 4:
      response = listAllProcess(queue)

      if response:
        print('\n', response)

    elif option == 5:
      month = input('\nIngresar mes (MM): ')
      response = lowPriorityByMonth(queue, month)

      if response:
        print('\n', response)

    elif option == 6:
      print('\nTipo')
      print('1. KERNEL')
      print('2. USUARIO')
      processType = input('\nIngresar: ')
      response = delByType(queue, processType)

      print('\n', response)

    elif option == 7:
      hour = input('\nIngresar primer hora (hh:mm): ')
      secondHour = input('\nIngresar segunda hora (hh:mm): ')

      response = newQueueByHour(queue, hour, secondHour)

      if response:
        print('\n', response)

    input('\n\nPresione enter para continuar')
    option = menu()

print('\nPrograma terminado')
