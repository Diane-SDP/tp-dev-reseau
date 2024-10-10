from os import system
import re
from sys import argv

response = system(f"ping {argv[1]} > nul")

if not re.search("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", argv[1]):
    print("invalid ip")
elif response == 0 :
    print("UP !")
else :
    print("DOWN !")
