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
  print('\n5. Listar un proceso')
  print('\n6. Cambiar a prioridad baja todos los procesos dado un mes')
  print('\n7. Eliminar todos los procesos de un tipo particular')
  print('\n8. Generar nueva cola a partir de intervalo horario')

  print('\n',format(' Presione 0 para finalizar ', '*^40'))

  #Modificar porque si ingreso número decimal se rompe
  #option = int(input('Opcion: '))
  optionInput = input('\nOpcion: ')

  try:
    option = int(optionInput)
  except ValueError:
    option = -1

  return option

queue = createQueue()

option = menu()

while option != 0:
  if option < 1 or option > 8:
    print('\n\nLa opcion ingresada es incorrecta, vuelva a intentarlo')
    print('\n\n------------------------------------------------------')
    print('\n\nCLEARING...')
    sleep(1.5)
    option = menu()
  else:
    if option == 1:
      process = createProcess()
      name = input('\nIngresar nombre: ')
      processType = input('Ingresar tipo: ')
      size = input('Ingresar tamaño: ')
      priority = input('Ingresar prioridad: ')

      response = addProcess(queue, process, name, processType, size, priority)

      print('\n',response)
      sleep(0.5)
    elif option == 2:
      index = int(input('\nIngresar indice de proceso: '))
      search = searchProcess(queue, index)
      if search:
        print('\n1. LOW')
        print('2. MID')
        print('3. HIGH')
        inputPriority = input('\nSeleccionar prioridad: ')

        try:
          priority = int(inputPriority)
        except ValueError:
          priority = -1

        response = modPriority(queue, index, priority)

        print(response)
      else:
        print('\nEl proceso no existe')

    elif option == 12:
      index = int(input('Ingresar indice de proceso: '))
      search = searchProcess(queue, index)
      if search:
        name = input('Ingresar nombre: ')
        processType = input('Ingresar tipo: ')
        size = input('Ingresar tamaño: ')
        priority = input('Ingresar prioridad: ')

        response = modProcess(queue, index, name, processType, size, priority)

        print(response)
      else:
        print('\nEl proceso no existe')
    elif option == 4:
      listAllProcess(queue)
      input('\n\nPresionar enter para mostrar menú')

    option = menu()




print('\nPrograma terminado')