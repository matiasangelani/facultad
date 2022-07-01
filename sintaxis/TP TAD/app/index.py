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

from os import system
from tads.processesTAD import *
from tads.queueTAD import *

def menu():
  system('clear')
  print('\n\n', format(' SELECCIONAR UNA OPCION ', '=^50'))
  print('\n1. Encolar proceso')
  print('\n2. Modificar prioridad de proceso')
  print('\n3. Desencolar proceso')
  print('\n4. Listar procesos')
  print('\n5. Cambiar a prioridad baja todos los procesos dado un mes')
  print('\n6. Eliminar todos los procesos de un tipo particular')
  print('\n7. Generar nueva cola a partir de intervalo horario')

  print('\n',format(' Presione 0 para finalizar ', '*^40'))

  option = input('\nOpcion: ')

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

      response = addProcess(process, name, processType, size, priority, date, hour)
      
      if response:
        uploadQueue(queue, process)
        print('\n', response)

    elif option == 2:
      print('\nMétodo de búsqueda')
      print('1. ID')
      print('2. Nombre')
      search = input('Seleccionar método: ')
      print('\n1. LOW')
      print('2. MID')
      print('3. HIGH')
      priority = input('\nSeleccionar prioridad: ')
      response = modPriority(queue, search, priority)

      if response:
        print('\n', response)

    elif option == 3:
      id = input('\nIngresar ID de proceso: ')
      response = deleteProcess(queue, id)

      print(response)

    elif option == 4:
      cont = 0
      for i in range(0, queueSize(queue)):
        cont = 1
        process = readQueue(queue, i)
        if i == 0:
          print('\n\t{:^40} {:<10} {:<10} {:<10} {:<10} {:<15} {:<10}'.format('ID','NOMBRE','TIPO', 'TAMAÑO', 'PRIORIDAD', 'FECHA', 'HORA'))
        print('\n\t{:^40} {:<10} {:<10} {:<10} {:<10} {:<15} {:<10}'.format(readId(process), readName(process), readProcessType(process), readSize(process), readPriority(process), readDate(process), readHour(process)))

      if not cont:
        print('\n\nLa cola está vacía')

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

      newQueue = newQueueByHour(queue, hour, secondHour)
      
      cont = 0
      for i in range(0, queueSize(newQueue)):
        cont = 1
        if isinstance(newQueue, str):
          print(newQueue)
          break
        process = readQueue(newQueue, i)
        if i == 0:
          print('\n\t{:^40} {:<10} {:<10} {:<10} {:<10} {:<15} {:<10}'.format('ID','NOMBRE','TIPO', 'TAMAÑO', 'PRIORIDAD', 'FECHA', 'HORA'))
        print('\n\t{:^40} {:<10} {:<10} {:<10} {:<10} {:<15} {:<10}'.format(readId(process), readName(process), readProcessType(process), readSize(process), readPriority(process), readDate(process), readHour(process)))

      if not cont:
        print('\n\nLa cola está vacía')

    input('\n\nPresione enter para continuar')
    option = menu()

print('\nPrograma terminado')
