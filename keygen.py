from cryptography.fernet import Fernet
import os, logging

logging.basicConfig(filename='main.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s - %(levelname)s : %(message)s')


def gen():

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

gen()