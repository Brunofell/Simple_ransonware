# vai criptografar arquivos de texto
# pip install cryptography

import os

from cryptography.fernet import Fernet

files = []

key = Fernet.generate_key()

with open("chave.key", "rb") as key:
    secretkey = key.read()

for file in os.listdir():
    if file == 'madara.py' or file == 'chave.key' or file == "decrypt.py": 
        continue
    if os.path.isfile(file):
        files.append(file)

for file in files:
    with open(file, "rb") as arquivo:
        conteudo = arquivo.read()
    conteudo_decrypted = Fernet(secretkey).decrypt(conteudo)
    with open(file, "wb") as arquivo:
        arquivo.write(conteudo_decrypted)