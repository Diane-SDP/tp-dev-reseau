from socket import gethostbyname
from sys import argv
import re

if re.search("[a-z]+\.+[a-z]", argv[1]):
    print(gethostbyname(argv[1]))
else :
    print("invalid hostname")