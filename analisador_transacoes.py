from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()
cliente = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
modelo = "gpt-4.1-mini"

def carrega(nome_do_arquivo):
    try:
        with open(nome_do_arquivo, "r", encoding="utf-8") as arquivo:
            dados = arquivo.read()
            return dados
    except IOError as e:
        print(f"Erro: {e}")
    except UnicodeDecodeError as e:
        print(f"Erro de codificação ao ler o arquivo: {e}")

def salva(nome_do_arquivo, conteudo):
    try:
        with open(nome_do_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write(conteudo)
    except IOError as e:
        print(f"Erro ao salvar arquivo: {e}")