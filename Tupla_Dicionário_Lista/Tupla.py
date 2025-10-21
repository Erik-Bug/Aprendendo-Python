tupla_heterogeneo = (1, "Olá", 3.14, [2, 3, 5, 7], {"chave": "valor"})

# Acessando e imprimindo elementos individuais
print(f"Inteiro: {tupla_heterogeneo[0]}")
print(f"string: {tupla_heterogeneo[1]}")
print(f"float: {tupla_heterogeneo[2]}")
print(f"Lista: {tupla_heterogeneo[3]}")
print(f"dicionario: {tupla_heterogeneo[4]}")

# Modificando a lista dentro da tupla
tupla_heterogeneo[3].append(11)
print(f"lista modificada: {tupla_heterogeneo[3]}")

# Acessando valor do dicionario dentro da tupla
valor_dict = tupla_heterogeneo[4]["chave"]
print(f"Valor no dicionario: {valor_dict}")

# Iterando sobre tupla e imprimindo o valor de cada elemento
for elemento in tupla_heterogeneo:
    print(f"Elemento: {elemento}, tipo: {type(elemento)}")
