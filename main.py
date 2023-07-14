from cryptography.fernet import Fernet
import os, logging, json

logging.basicConfig(filename='main.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s - %(levelname)s : %(message)s')

def key_gen():

    if not os.path.isfile('key.key'):
        key = Fernet.generate_key()
        logging.info('Key Genarated')
        logging.info(f'Key : {key}')

        #print(f'Key : {key}')
        with open('key.key','wb') as file:
            file.write(key)
            file.close()
    else:
        with open('key.key','r') as file:
            key = file.read()
            logging.info('Key Exists')
            logging.info(f'key : {key}')
            #print('Key Exists')




if os.path.isfile('key.key'):
    with open('key.key','rb') as key_file:
        key = key_file.read()
        key_file.close()
    fernet = Fernet(key)
else:
    print('No key found.')
    if input('Would you like to generate a key now (y/N) : ').lower() == 'y':
        key_gen()

if os.path.isfile('passwords.json'):
    with open('passwords.json', 'rb') as pass_file:
        pass_json_encr = pass_file.read()
        pass_file.close()
    pass_json = fernet.decrypt(pass_json_encr)
    pass_json = json.loads(pass_json)
else:
    print('No password file found.')
    if input('Would you like to generate a password file now (y/N) : ').lower() == 'y':
        #file_gen()
