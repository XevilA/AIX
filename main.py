import os
import socket 
import string

class Network:
    net_protocal = "https"
    net_port = "8080"


class OSx:
    os_name = os.name
    os.system('cd aix')
    print(os_name)
    print(os.system)

class User:
    user_promt = os.system('ping www.bodin2.ac.th')
    
    uinput = int(input("Press 1 for ping"))

    if uinput == 1 :
        print(user_promt)

    else:
        print('ERROR')   
        
