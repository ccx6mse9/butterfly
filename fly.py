#importing required modules
import argparse
import socket
from slowprint.slowprint import *
import colorama
colorama.init()
text =""
text+="\t\t\t ____        _   _             __ _       \n"
text+="\t\t\t| __ ) _   _| |_| |_ ___ _ __ / _| |_   _ \n"
text+="\t\t\t|  _ \| | | | __| __/ _ \ '__| |_| | | | |\n"
text+="\t\t\t| |_) | |_| | |_| ||  __/ |  |  _| | |_| |\n"
text+="\t\t\t|____/ \__,_|\__|\__\___|_|  |_| |_|\__, |\n"
text+="\t\t\t                                    |___/ \n"
text+="\t\t\t"
info ="\t\t\t   Created by sanjay/ccx6mse9 (version 1.0)    \n"

slowprint(colorama.Fore.RED+text,0.1)
print(colorama.Fore.YELLOW +info)
print(colorama.Fore.RESET)

slowprint("\t\t\t-------------------------------------------",0.3)

def scanPorts(host,ports):
    soc = socket.socket()
    for port in ports:
        try:
            soc.connect((host,port))
            print(f"\t\t\t{colorama.Fore.RED}The IP address: '{host}' with Port: '{port}' is Open")
            print(colorama.Fore.RESET)
        except:
            print(f"\t\t\t{colorama.Fore.GREEN}The IP address: '{host}' with Port: '{port}' is Closed")
            print(colorama.Fore.RESET)
            
    soc.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="butterfly-thePortScanner")
    parser.add_argument('-ip',dest='host',type=str)
    parser.add_argument('-ports',dest='port_range',default='1-65535')
    args = parser.parse_args()
    port_range = args.port_range
    start , last = port_range.split('-')
    start , last = int(start),int(last)
    host = args.host
    ports = [ p for p in range(start, last+1)]
    scanPorts(host,ports)