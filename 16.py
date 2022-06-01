class myexception(Exception):
   def __init__(self, value):
      self.value = value
   def __str__(self):
      return(repr(self.value))
try:
   raise(myexception("User defined error"))
   
except myexception as error:
   print('A New Exception occured:',error.value)
