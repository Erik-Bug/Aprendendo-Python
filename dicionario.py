dicionario = {
    "nome": "Alice",
    "idade": "22",
    "cidade": "Ceará",
}


# Acessando e imprimindo valores individuais em chaves
nome = dicionario["nome"]
idade = dicionario["idade"]
cidade = dicionario["cidade"]

print(f"nome: {nome}")
print(f"idade: {idade}")
print(f"cidade: {cidade}")

# Adicionando um novo valor chave-valor ao dicionario
dicionario["profissão"] = "Engenheira"
print(f"Dicionário após adição de profissão: {dicionario}")

# Modificação do dicionário
dicionario["idade"] = 24
print(f"dicionario apos modificar idade: {dicionario}")

# Removendo um par chave de dicionario
del dicionario["cidade"]
print(f"dicionario pós remoção: {dicionario}")

# Acessando todas as chaves e valores
chaves = dicionario.keys()
valores = dicionario.values()

print(f"Chaves do dicionario: {list(chaves)}")
print(f"Valores do dicionario: {list(valores)}")

# iteração valores e chaves
for chaves, valores in dicionario.items():
    print(f"{chaves}:{valores}")

# Verificando se uma chave existeno dicionário
if "nome" in dicionario:
    print(f"O nome no dicionario é:{dicionario['nome']}")
else:
    print(f"A chave nome não existe em dicionario")

# Usando metodo get() para acessar valores de forma segura
profissao = dicionario.get("profissão", "desconhecido")
print(f"profissão: {profissao}")

# Limpando o dicionario
dicionario.clear()
print(f"Dicionario após limpeza: {dicionario}")
