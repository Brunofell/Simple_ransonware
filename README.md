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

**Este projeto é apenas para fins educacionais. Não deve ser utilizado para atividades maliciosas. O uso de ransomware ou qualquer ferramenta que comprometa a segurança de dados de outras pessoas é ilegal e antiético. **
