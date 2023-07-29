from cryptography.fernet import Fernet
from time import sleep
import os, logging, json, sys

version = '1.0.0'

def clear():
 
    # for windows
    if os.name == 'nt':
        os.system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        os.system('clear')


logging.basicConfig(filename='main.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s - %(levelname)s : %(message)s')

# load settings
with open('settings.json', 'r') as file:
    settings = json.loads(file.read())
    file.close()


def write_settings():
    with open('settings.json', 'w') as file:
        file.write(json.dumps(settings, indent=4))

def key_gen():
    if not os.path.isfile(settings['key_filename']):
        key = Fernet.generate_key()
        logging.info('Key Genarated')
        logging.info(f'Key : {key}')

        #print(f'Key : {key}')
        with open(settings['key_filename'],'wb') as file:
            file.write(key)
            file.close()
    else:
        with open(settings['key_filename'],'rb') as file:
            key = file.read()
            file.close()
            logging.info('Key Exists')
            logging.info(f'key : {key}')
            #print('Key Exists')


def file_gen():
    question = input('file name (password.json) : ').lower()
    if question != '': 
        settings['passwords_filename'] = f'{question}.json'
        write_settings()
    with open(settings['passwords_filename'], 'wb') as file:
        data = fernet.encrypt(bytes('{}', encoding='utf8'))
        
        
        file.write(data)
        logging.info('Password database created')

        file.close()

    

        
if os.path.isfile(settings['key_filename']):
    with open(settings['key_filename'],'rb') as key_file:
        key = key_file.read()
        key_file.close()
    fernet = Fernet(key)
else:
    print('No key found.')
    if input('Would you like to generate a key now (y/N) : ').lower() == 'y':
        key_gen()
    with open(settings['key_filename'],'rb') as key_file:
        key = key_file.read()
        key_file.close()
    fernet = Fernet(key)

if os.path.isfile(settings['passwords_filename']):
    with open(settings['passwords_filename'], 'rb') as pass_file:
        pass_json_encr = pass_file.read()
        pass_file.close()
    pass_json = fernet.decrypt(pass_json_encr)
    pass_json = json.loads(pass_json)
else:
    print('No password file found.')
    question = input('Would you like to generate a password file now (y/N) : ').lower()
    if question == 'y':
        file_gen()
def mainMenu():
    inp = input('>')

    inp = inp.split(' ')
    cmd = inp[0]
    inp.pop(0)

    if cmd == 'help': helpCmd()
    if cmd == 'add': addCmd(inp[0])
    if cmd == 'show': showCmd()
    if cmd == 'edit': editCmd()
    if cmd == 'exit': exitCmd()
    if cmd == 'clear': 
        clear() 
    if cmd != '':
        print(f"'{cmd}' is not a command use the 'help' command to se a list")
    mainMenu()

def exitCmd():
    sys. exit()

def helpCmd():
    print('''
    help - Shows this help dialog

    clear - clears the screen
                   
    add - (add x y) x = name y = type (if none defult to password) - used to add new passwords and keys
          
    show - (show x) x = name - shows a prexisting password or key
          
    edit - (edit x) x = name - used to edit a prexisting password or key

    exit - exits the program
''')
    mainMenu()

def addCmd(type):
    if type == 'key':
        print(type)
    elif type == 'pass':
        print(type) 
    else:
        print(f"'{type}' is not 'pass' or 'key'")
    mainMenu()

sleep(1)
clear()
print(f'Chopper Ver : {version}')
mainMenu()