import uuid
from datetime import datetime
from tads.validationsTAD import *


def createQueue():
  #Crea una cola
  queue = []
  return queue


def createProcess():
  #Crea un proceso
  process = ["", "", "", 0, "", "", ""]
  return process


def addProcess(queue, process, name, processType, size, priority, date, hour):
  #Agrega proceso a la cola
  size = verifyInt(size)
  date = isValidDate(date)
  hour = isValidHour(hour)

  if size == -1 or not date or not hour:
    return False
  
  process[0] = str(uuid.uuid4())
  process[1] = name
  process[3] = size
  process[5] = date
  process[6] = hour

  if processType == '1':
    process[2] = 'KERNEL'
  elif processType == '2':
    process[2] = 'USER'
  else:
    print('\nOpción incorrecta, vuelva a intentarlo')
    return 'Value error'

  if priority == '1':
    process[4] = 'LOW'
  elif priority == '2':
    process[4] = 'MID'
  elif priority == '3': 
    process[4] = 'HIGH'
  else:
    print('\nOpción incorrecta, vuelva a intentarlo')
    return 'Value error'

  queue.append(process)

  return 'Process added'


def listProcess(queue, search = 1):
  #Lista todos los procesos
  count = 0
  if not len(queue):
    return '\n\nLista vacía'

  search = verifyInt(search)

  if search == -1:
    return False

  print('\n\t{:^40} {:<10} {:<10} {:<10} {:<10} {:<15} {:<10}'.format('ID','NOMBRE','TIPO', 'TAMAÑO', 'PRIORIDAD', 'FECHA', 'HORA'))
  
  position = 0
  value = ''
  if search == 2:
    position = 2
    value = 'KERNEL'
  elif search == 3:
    position = 2
    value = 'USER'
  elif search == 4:
    position = 4
    value = 'LOW'
  elif search == 5:
    position = 4
    value = 'MID'
  elif search == 6:
    position = 4
    value = 'HIGH'

  for process in queue:
    id, name, processType, size, priority, date, hour = process
    if search == 1 or process[position] == value:
      count = 1
      print('\n\t{:^40} {:<10} {:<10} {:<10} {:<10} {:<15} {:<10}'.format(id, name, processType, size, priority, date, hour))

  if not count:
    print('\n\nDatos existe datos, use otro filtro')
  

def modProcess(queue, index, name, processType, size, priority):
  #Modifica un proceso
  for i, process in enumerate(queue):
    if index == i:      
      process[1] = name
      process[2] = processType
      process[3] = size
      process[4] = priority
      process[5] = datetime.today().strftime('%Y-%m-%d')
      process[6] = datetime.today().strftime('%H:%M')

  return '\nProcess modified'


def delProcess(queue, id):
  #Elimina proceso por ID
  for i, process in enumerate(queue):
    if id == process[0]:
      queue.pop(i)
      return '\nProcess deleted'

  return '\nProcess not found'


def modPriority(queue, search, priority):
  #Modifica prioridad de un proceso
  name = ''
  id = ''
  
  if search == '1':
    id = input('\nIngresar ID: ')
  elif search == '2':
    name = input('\nIngresar nombre: ')

  process = searchProcess(queue, id, name)

  if process:
    if priority == '1':
      priority = 'LOW'
    elif priority == '2':
      priority = 'MID'
    elif priority == '3':
      priority = 'HIGH'
    else:
      print('\nOpción incorrecta, vuelva a intentarlo')
      return 'Value error'
    
    process[4] = priority
    process[5] = datetime.today().strftime('%Y-%m-%d')
    process[6] = datetime.today().strftime('%H:%M')

    return '\nPriority modified'
  
  return '\nProcess not found'


def searchProcess(queue, id, name):
  #Busca un proceso
  for process in queue:
    if id == process[0] or name == process[1]:
      return process

  return False


def lowPriorityByMonth(queue, month):
  #La prioridad de todos los procesos que pertenezcan al mes ingresado cambiará a LOW
  count = 0
  month = isValidMonth(month)

  if not month:
    return False

  for process in queue:
    if process[5][5:7] == month:
      count = 1
      process[4] = 'LOW'
      process[5] = datetime.today().strftime('%Y-%m-%d')
      process[6] = datetime.today().strftime('%H:%M')

  if count:
    return '\nPrioridad de procesos del mes {month} modificados a LOW'.format(month = month)

  return '\nNingún proceso encontrado con mes {month}'.format(month = month)


def delByType(queue, processType):
  #Elimina todos los procesos que pertenezcan al tipo ingresado
  if processType == '1':
    processType = 'KERNEL'
  elif processType == '2':
    processType = 'USER'
  else:
    print('\nOpción incorrecta, vuelva a intentarlo')
    return 'Value error'

  for process in reversed(queue):
    if process[2] == processType:
      queue.remove(process)

  return '\nTodos los procesos tipo {processType} han sido eliminados'.format(processType = processType)


def newQueueByHour(queue, hour, secondHour):
  #Genera y muestra una nueva cola a partir de un intervalo horario ingresado
  newQueue = []
  hour = isValidHour(hour)
  secondHour = isValidHour(secondHour)

  if not hour or not secondHour:
    return False

  oldHour = hour
  oldSecondHour = secondHour
  hour = hour.split(':')
  secondHour = secondHour.split(':')

  if (int(secondHour[0]) - int(hour[0]) < 0) or (int(hour[0]) - int(secondHour[0]) == 0 and int(hour[1]) > int(secondHour[1])):
    return '\nPor favor, ingresar horario en orden inverso'

  for process in queue:
    processHour = int(process[6].split(':')[0])
    processMinute = int(process[6].split(':')[1])
    if processHour > int(hour[0]) and processHour < int(secondHour[0]):
      newQueue.append(process)
    elif processHour == int(hour[0]) and processMinute >= int(hour[1]) and processMinute <= int(secondHour[1]):
      newQueue.append(process)
    elif processHour == int(secondHour[0]) and processMinute >= int(hour[1]) and processMinute <= int(secondHour[1]):
      newQueue.append(process)
      
  response = listProcess(newQueue)

  if response:
    return response

  return '\nNueva cola en intervalo {oldHour} - {oldSecondHour} creada'.format(oldHour = oldHour, oldSecondHour = oldSecondHour)