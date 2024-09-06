# Ransomware Simples

Este repositório contém dois scripts que simulam um ransomware simples. O `madara.py` é responsável por criptografar arquivos, enquanto o `decrypt.py` faz a descriptografia, restaurando os dados.

## Descrição dos Scripts

- **madara.py**: Este script criptografa todos os arquivos da pasta onde é executado (exceto o próprio script e o arquivo da chave). Ele gera uma chave de criptografia e a armazena em um arquivo chamado `chave.key`.
- **decrypt.py**: Este script descriptografa os arquivos criptografados usando a chave gerada no processo de criptografia. Ele restaura os arquivos ao seu estado original.

## Como Funciona

1. **madara.py**:
   - Gera uma chave usando a biblioteca `cryptography`.
   - Criptografa todos os arquivos da pasta, exceto o próprio script e a chave gerada.
   - Salva a chave no arquivo `chave.key`.

2. **decrypt.py**:
   - Lê a chave armazenada no arquivo `chave.key`.
   - Descriptografa todos os arquivos criptografados pela chave.

## Requisitos

- Python 3.x
- Biblioteca `cryptography`

Instale a dependência com:

```bash
pip install cryptography
```

**Este projeto é apenas para fins educacionais. Não deve ser utilizado para atividades maliciosas. O uso de ransomware ou qualquer ferramenta que comprometa a segurança de dados de outras pessoas é ilegal e antiético. **


  

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



# Simple Ransomware

This repository contains two scripts that simulate a simple ransomware. The `madara.py` script is responsible for encrypting files, while `decrypt.py` decrypts them, restoring the data.

## Script Descriptions

- **madara.py**: This script encrypts all files in the folder where it is executed (except the script itself and the key file). It generates an encryption key and stores it in a file called `chave.key`.
- **decrypt.py**: This script decrypts the files encrypted using the key generated during encryption. It restores the files to their original state.

## How It Works

1. **madara.py**:
   - Generates an encryption key using the `cryptography` library.
   - Encrypts all files in the folder, except for the script itself and the generated key.
   - Saves the key in the `chave.key` file.

2. **decrypt.py**:
   - Reads the key stored in the `chave.key` file.
   - Decrypts all files encrypted by the key.

## Requirements

- Python 3.x
- `cryptography` library

## Install the dependency with:

```bash
pip install cryptography
```

** Disclaimer **
This project is for educational purposes only. It should not be used for malicious activities. The use of ransomware or any tool that compromises other people's data security is illegal and unethical. 
