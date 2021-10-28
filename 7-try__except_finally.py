'''
The try block lets you test a block of code for errors.

The except block lets you handle the error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.
'''

#x=3

try:
  print(x)
except:
  print("An exception occurred")
finally:
  print("The 'try except' is finished")
  
  
'''
Print one message if the try block raises a NameError and another for other errors: 
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
#else keyword to define a block of code to be executed if no errors were raised: 
else:
  print("Nothing went wrong")
'''  
