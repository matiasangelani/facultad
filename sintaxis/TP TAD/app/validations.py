from datetime import datetime
import time

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
    return date
  except ValueError:
    print('\nFormato de fecha incorrecto, vuelva a intentarlo') 
    return False

def isValidHour(hour):
  try:
    time.strptime(hour, '%H:%M')
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