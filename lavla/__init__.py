# Lavla2
# Source Code
import sys
import os

class lavla2:
  data = ""
  def __init__(view):
    data = open(os.path.join("./views/",view + ".lavla2"),"r").read()
    
  def __data(form):
    return data.format(form)
    
# Starting on the command for the python console

args = sys.argv

web = lavla2(args[0])
form = web.__data(args[1])

print(form)
