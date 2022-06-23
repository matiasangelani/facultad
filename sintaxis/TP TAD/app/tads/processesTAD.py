import os
import uuid
from datetime import datetime
import time

def createQueue():
  #Crea una cola
  queue = []
  return queue

def createProcess():
  #Crea un proceso
  process = ["","","","","","",""]
  return process

def addProcess(queue, process, name, processType, size, priority, date, hour):
  #Agrega proceso a la cola
  size = verifyInt(size)
  # priority = verifyInt(priority)
  #date = verifyInt(date)
  date = isValidDate(date)
  hour = isValidHour(hour)

  if size == -1 or not date or not hour:
    return False
  
  # file = open("db.txt", "a")

  process[0] = str(uuid.uuid4())
  # file.write(process[0])
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

  # process[5] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

  queue.append(process)

  # file.close()

  return 'Process added'

def listAllProcess(queue):

  if not len(queue):
    return '\n\nLista vacía'

  print ('\n\t{:^40} {:<10} {:<10} {:<10} {:<10} {:<15} {:<10}'.format('ID','NOMBRE','TIPO', 'TAMAÑO', 'PRIORIDAD', 'FECHA', 'HORA'))

  for process in queue:
    id, name, processType, size, priority, date, hour = process
    print('\n\t{:^40} {:<10} {:<10} {:<10} {:<10} {:<15} {:<10}'.format(id, name, processType, size, priority, date, hour))

  # file = open("db.txt", "r")
  # print(file.read())
  

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

  return 'Process modified'

def delProcess(queue, id):
  #Elimina proceso por ID
  for i, process in enumerate(queue):
    if id == process[0]:
      queue.pop(i)
      return 'Process deleted'

  return 'Process not found'

def modPriority(queue, id, priority):
  #Modifica prioridad de un proceso
  # index = verifyInt(index)
  # priority = verifyInt(priority)

  # if index == -1 or priority == -1:
  #   return False

  process = searchProcess(queue, id)

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

    return 'Priority modified'
  
  return 'Process not found'

def searchProcess(queue, id):
  #index = verifyInt(index)
  #if index != -1:
  for process in queue:
    if id == process[0]:
      return process

  return False

def lowPriorityByMonth(queue, month):

  month = isValidMonth(month)

  if not month:
    return False

  for process in queue:
    if process[5][5:7] == month:
      process[4] = 'LOW'
      process[5] = datetime.today().strftime('%Y-%m-%d')
      process[6] = datetime.today().strftime('%H:%M')

  return True

def delByType(queue, processType):

  if processType == '1':
    processType = 'KERNEL'
  elif processType == '2':
    processType = 'USER'
  else:
    print('\nOpción incorrecta, vuelva a intentarlo')
    return 'Value error'

  # Tengo que recorrer la cola al revés
  for process in queue:
    if process[2] == processType:
      queue.remove(process)

  return 'Todos los procesos tipo {processType} han sido eliminados'.format(processType = processType)

def verifyInt(value):
  try:
    value = int(value)
    return value
  except ValueError:
    print('\nDato ingresado incorrecto')
    return -1

def isValidDate(date):
  try:
    datetime.strptime(date, '%Y-%m-%d')
    #return date.strftime('%Y-%m-%d')
    return date
  except ValueError:
    print('\nFormato de fecha incorrecto, vuelva a intentarlo') 
    return False

def isValidHour(hour):
  try:
    time.strptime(hour, '%H:%M')
    #return hour.strftime('%H:%M')
    return hour
  except ValueError:
    print('\nFormato de hora incorrecto, vuelva a intentarlo') 
    return False

def isValidMonth(month):
  try:
    time.strptime(month, '%m')
    return month
  except ValueError:
    print('\nFormato de mes incorrecto, vuelva a intentarlo') 
    return False