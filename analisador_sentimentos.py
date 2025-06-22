from openai import OpenAI
from dotenv import load_dotenv
import os

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

def analisador_sentimentos(produto):
    prompt_sistema = f"""
        Você é um analisador de sentimentos de avaliações de produtos.
        Escreva um parágrafo com até 50 palavras resumindo as avaliações e 
        depois atribua qual o sentimento geral para o produto.
        Identifique também 3 pontos fortes e 3 pontos fracos identificados a partir das avaliações.

        # Formato de Saída

        Nome do Produto:
        Resumo das Avaliações:
        Sentimento Geral: [utilize aqui apenas Positivo, Negativo ou Neutro]
        Ponto fortes: lista com três bullets
        Pontos fracos: lista com três bullets
    """

    prompt_usuario = carrega(f"dados/avaliacoes-{produto}.txt")
    print(f"Iniciou a análise de sentimento do produto {produto}")

    if prompt_usuario is None:
        print(f"Arquivo de avaliações para {produto} não encontrado.")
        return

    lista_mensagens = [
        {
            "role": "system",
            "content": prompt_sistema
        },
        {
            "role": "user",
            "content": prompt_usuario
        }
    ]

    resposta = cliente.chat.completions.create(
        messages = lista_mensagens,
        model = modelo
    )

    texto_resposta = resposta.choices[0].message.content
    salva(f"dados/analise-{produto}.txt", texto_resposta)

lista_de_produtos = ["Maquiagem_Mineral", "Fone_de_ouvido", "Panela_Antiaderente"]

for um_produto in lista_de_produtos:
    analisador_sentimentos(um_produto)
