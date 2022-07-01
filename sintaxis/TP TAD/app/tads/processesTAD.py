import uuid
from validations import *

# Create Process
def createProcess():
  process = ["", "", "", 0, "", "", ""]
  return process

# Upload Process
def addProcess(process, name, processType, size, priority, date, hour):
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

  #uploadQueue(queue, process)
  #queue.append(process)
  return 'Process added'

# Read Process Id
def readId(process):
  return process[0]

# Read Process Name
def readName(process):
  return process[1]

# Read Process Type
def readProcessType(process):
  return process[2]

# Read Process Size
def readSize(process):
  return process[3]

# Read Process Priority
def readPriority(process):
  return process[4]

# Read Process Date
def readDate(process):
  return process[5]

# Read Process Hour
def readHour(process):
  return process[6]