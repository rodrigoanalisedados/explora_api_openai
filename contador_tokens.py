import tiktoken

modelo = "gpt-4.1"
codificador = tiktoken.get_encoding("cl100k_base")
lista_tokens = codificador.encode("Você é um categorizador de produtos.")

print("Lista de Tokens: ", lista_tokens)
print("Quantos tokens temos: ", len(lista_tokens))
custo = (len(lista_tokens)/1000) * 0.03
print(f"Custo para o modelo {modelo} é de ${custo:.6f}")

modelo = "gpt-4.1-mini"
# Reutilize o mesmo codificador
lista_tokens = codificador.encode("Você é um categorizador de produtos.")

print("Lista de Tokens: ", lista_tokens)
print("Quantos tokens temos: ", len(lista_tokens))
custo = (len(lista_tokens)/1000) * 0.001
print(f"Custo para o modelo {modelo} é de ${custo:.6f}")