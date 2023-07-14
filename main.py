from cryptography.fernet import Fernet
import os, logging, json

if os.path.isfile('key.key'):
    with open('key.key','rb') as key_file:
        key = key_file.read()
        key_file.close()
    fernet = Fernet(key)
else:
    print('Please Genarate Key...')

if os.path.isfile('passwords.json'):
    with open('passwords.json', 'rb') as pass_file:
        pass_json_encr = pass_file.read()
        pass_file.close()
    pass_json = fernet.decrypt(pass_json_encr)
    pass_json = json.loads(pass_json)
else:
    print('Please Genarate Password File...')