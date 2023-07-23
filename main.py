from cryptography.fernet import Fernet
import os, logging, json

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
    print(pass_json)
else:
    print('No password file found.')
    question = input('Would you like to generate a password file now (y/N) : ').lower()
    if question == 'y':
        file_gen()


