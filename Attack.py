import os

h=input(" Input You Host ")
while true:
  os.system(" ping -i .0000 -f  {}".format(h))
