from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(key)
with open('key.key','wb') as file:
    file.write(key)
    file.close()