from datetime import datetime
from validations import *

# Create queue
def createQueue():
  queue = []
  return queue

# Queue size
def queueSize(queue):
  return len(queue)

# Upload queue
def uploadQueue(queue, process):
  queue.append(process)
  return queue

# Read queue
def readQueue(queue, i):
  return queue[i]

# Delete queue
def deleteProcess(queue, id):
  for i, process in enumerate(queue):
    if id == process[0]:
      queue.pop(i)
      return '\nProcess deleted'

  return '\nProcess not found'

# Update Process Priority
def modPriority(queue, search, priority):
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

# Search Process
def searchProcess(queue, id, name):
  for process in queue:
    if id == process[0] or name == process[1]:
      return process

  return False

# Update Process Priority to low by month
def lowPriorityByMonth(queue, month):
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

# Delete all Process with equal type
def delByType(queue, processType):
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

# Create new queue by range hour
def newQueueByHour(queue, hour, secondHour):
  newQueue = []
  hour = isValidHour(hour)
  secondHour = isValidHour(secondHour)

  if not hour or not secondHour:
    return []

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

  return newQueue