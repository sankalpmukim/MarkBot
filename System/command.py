##run commands on the system's shell
l = '''\
██████╗ ██████╗  ██████╗      ██╗███████╗ ██████╗████████╗    
██╔══██╗██╔══██╗██╔═══██╗     ██║██╔════╝██╔════╝╚══██╔══╝   
██████╔╝██████╔╝██║   ██║     ██║█████╗  ██║        ██║      
██╔═══╝ ██╔══██╗██║   ██║██   ██║██╔══╝  ██║        ██║       
██║     ██║  ██║╚██████╔╝╚█████╔╝███████╗╚██████╗   ██║      
╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚══════╝ ╚═════╝   ╚═╝       

            ███╗   ███╗ █████╗ ██████╗ ██╗  ██╗
            ████╗ ████║██╔══██╗██╔══██╗██║ ██╔╝
            ██╔████╔██║███████║██████╔╝█████╔╝ 
            ██║╚██╔╝██║██╔══██║██╔══██╗██╔═██╗ 
            ██║ ╚═╝ ██║██║  ██║██║  ██║██║  ██╗
            ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
'''

def get_platform():
    with open("System/preferences.txt","r") as f:
        line = f.readline()
        garbage, platform = line.split('=')
        platform = platform.strip().replace('"','')
        return platform

import os, time
import subprocess as s
from colorama import init as i, Fore, deinit as di
i(autoreset = True)

pf = get_platform()

def execute(code, params=None, origin='main',role='administrator'):
    
    if code == 'l' or code == 'logo':
        if origin == 'main':
            if pf == "Windows":
                os.system('cls')
            elif pf == "Linux":
                os.system('clear')
            print(Fore.CYAN+l)
            return [0]
        else:
            return '$l'
        return [0]
    
    elif code == 'cmd' or code == 'terminal' or code == 'command':
        if role == 'administrator':
            command = ''
            for i in params:
                command+=i+' '
            command = command.lstrip(' \n').rstrip(' \n')
            cmdoutput = os.popen(command).read()
            if origin == 'main':
                return [1,Fore.MAGENTA+cmdoutput]
            else:
                return cmdoutput
        else:
            if origin == 'main':
                return [1,Fore.RED+'Error: You don\'t have the required role for this command']
            else:
                return 'Error: You don\'t have the required role for this command'
    
    elif code == 'install':
        if origin == 'script':
            try:
                os.system("pip3 install -r requirements.txt")
            except:
                os.system("pip install -r requirements.txt")
            print("Done!")
            time.sleep(2)
            if pf == "Windows":
                os.system("cls")
            elif pf == "Linux":
                os.system("clear")
            return [0]
        elif origin == 'main':
            return [1,Fore.RED+'Error: Cannot run this command manually, only script has access to this command']
    
    elif code == 'clear' or code == 'cls':
        if origin == 'main':
            if pf == "Windows": os.system('cls')
            elif pf == "Linux": os.system('clear')
            return [0]
        else:
            return '$clear'

    elif code == 'input' or code == 'inp' or code == 'nlp' or code == 'nlpu':
        string = ''
        for i in params:
            string+=i+' '
        string.rstrip(' \n')
        if origin == 'main':
            return ['nlpu',string]
        else:
            return 'An Error occured. The control of the program should not have reached here!'

    elif code == 'exit' or code == 'quit':
        if role=='administrator':
            if origin != 'main':
                print(Fore.CYAN+"Quit command recieved from server") 
            print(Fore.CYAN+"Goodbye, Come back soon!")
            return ['quit']
        else:
            if origin == 'main':
                return [1,Fore.RED+'Error: Permission Denied. User does\'nt have the required role']
            else:
                return 'Error: Permission Denied. User does\'nt have the required role'

    elif code == 'start-server' or code == 'server-start':
        if role=='administrator':
            if origin == 'main':
                return ['server_start']
            else:
                return 'Server already running'
        else:
            if origin == 'main':
                return [1,Fore.RED+'Error: Permission Denied. User does\'nt have the required role']
            else:
                return 'Error: Permission Denied. User does\'nt have the required role'

    if code == 'stop-server' or code == 'server-stop':
        if role=='administrator':
            if origin == 'main':
                return ['server_stop']
            else:
                ####################
                #Not implemented yet
                ####################
                pass
            
        else:
            if origin == 'main':
                return [1,Fore.RED+'Error: Permission Denied. User does\'nt have the required role']
            else:
                return 'Error: Permission Denied. User does\'nt have the required role'
    
    else:
        if origin == 'main':
            message = Fore.RED+'Error: Command not recognized'
            return [1,message]
        else:
            return 'Error: Command not recognized'
        
    

