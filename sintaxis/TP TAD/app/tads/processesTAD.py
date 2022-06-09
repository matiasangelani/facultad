from datetime import datetime

def createQueue():
  #Crea una cola
  queue = []
  return queue

def createProcess():
  #Crea un proceso
  process = ["","","","",""]
  return process

def addProcess(queue, process, name, processType, size, priority):
  #Agrega proceso a la cola
  process[0] = name
  process[1] = processType
  process[2] = size
  process[3] = priority
  process[4] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

  queue.append(process)

  return 'Process added'

def listAllProcess(queue):
  print ('\n\t{:<5} {:<10} {:<10} {:<10} {:<10} {:<10}'.format('#','Nombre','Tipo', 'Tamaño', 'Prioridad', 'Fecha'))
  for i, process in enumerate(queue):
    name, processType, size, priority, date = process
    print('\t{:<5} {:<10} {:<10} {:<10} {:<10} {:<10}'.format(i, name, processType, size, priority, date))

def modProcess(queue, index, name, processType, size, priority):
  #Modifica un proceso
  for i, process in enumerate(queue):
    if index == i:      
      process[0] = name
      process[1] = processType
      process[2] = size
      process[3] = priority
      process[4] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')

  return 'Process modified'

def delProcess(queue):
  return 'Process deleted'

def searchProcess(queue, index):
  for i, process in enumerate(queue):
    if i == index:
      return True

  return False

def modPriority(queue, index, priority):
  #Modifica prioridad de un proceso
  if priority == 1:
    priority = 'LOW'
  elif priority == 2:
    priority = 'MID'
  elif priority == 3:
    priority = 'HIGH'

  for i, process in enumerate(queue):
    if index == i:      
      process[3] = priority

  return 'Priority modified'