import psutil

infos = str(psutil.net_if_addrs()['Wi-Fi'][1])
netmask = infos.split('\'')[3].split(".")
counter = list()
for octet in netmask:
    counter.append(str(bin(int(octet))).count("1")) 

print(infos.split('\'')[1] + "/" + str(sum(counter)))
print(str(2**(32-sum(counter))) + " adresses")