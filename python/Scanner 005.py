#!/bin/python3

import sys, socket
from datetime import datetime

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
        print("alvo invalido Ou comando errado!!")
        print("python3 Scanner.py <ip>")
        sys.exit()

print("-" * 50)
print("Fazendo o Scan!!" +target)
print("Started Scan: "+str(datetime.now()))
print("-" * 50)

try:
        for port in range(1,10000):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target,port))
            #print("Checking Port {}".format(port))
            if result == 0:
                    print("Port {} is open".format(port))
            s.close()


except KeyboardInterrupt:
    print("\nSaindo do Scanner.")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()
except socket.error:
    print("Couldn't connect to server.")
    sys.exit()

print("-" * 50)
print("Terminou o scan!!" +target)
print("Scan Terminado as : "+str(datetime.now()))
print("-" * 50)

