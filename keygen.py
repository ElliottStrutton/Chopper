from cryptography.fernet import Fernet
import os


if not os.path.isfile('key.key'):
    key = Fernet.generate_key()
    print(f'Key : {key}')
    with open('key.key','wb') as file:
        file.write(key)
        file.close()
else:
    print('Key Exists')