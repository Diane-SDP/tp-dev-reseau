from socket import gethostbyname
from sys import argv
import os 
import time
import datetime
from re import search
import psutil


def lookup(ip) :
    if search("[a-z]+\.+[a-z]", ip):
        return(gethostbyname(ip))
    else :
        return("invalid input")

def ping(ip) :
    response = os.system(f"ping {ip} > nul")
    if not search("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", ip):
        return("invalid input")
    if response == 0 :
        return("UP !")
    else :
        return("DOWN !")

def ip() :
    infos = str(psutil.net_if_addrs()['Wi-Fi'][1])
    netmask = infos.split('\'')[3].split(".")
    counter = list()
    for octet in netmask:
        counter.append(str(bin(int(octet))).count("1")) 

    return(infos.split('\'')[1] + "/" + str(sum(counter)) + "\n" +str(2**(32-sum(counter))) + " adresses")

def getresponse() :
    if argv[1] == "lookup" :
        response = lookup(argv[2])
    elif argv[1] == "ip":
        response = ip()
    elif argv[1] == "ping" :
        response = ping(argv[2])
    else :
        response = f"{argv[1]} is not an available command. Déso."
    return response

def makelog(output) :
    status = f" [INFO] Command {argv[1]} called successfully"
    if len(argv) > 2 :
        status += f" with argument {argv[2]}"
    if output == "invalid input" :
        status = " [ERROR] called with bad arguments : " + argv[2]
    elif output == f"{argv[1]} is not an available command. Déso." :
        status = f" [ERROR] Command {argv[1]} unknown"

    pathfold = os.path.join(os.getenv('localappdata'), "Temp", "network_tp3")
    LOG_PATH = os.path.join(os.getenv('localappdata'), "Temp", "network_tp3", "network.log")

    if not(os.path.exists(pathfold) and os.path.isdir(pathfold)):
        os.makedirs(pathfold)

    logfile = open(LOG_PATH, "a")
    ts = time.time()
    log = str(datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S') + status + ".\n")
    logfile.write(log)


output = getresponse()
print(output)
makelog(output)



