lista = [10, 20, 30, 40, 50]

#Elementos individuais
primeiro_elemento = lista[0]
segundo_elemento = lista[1]
print(f"o primeiro elemento é {primeiro_elemento}")
print(f"o segundo elemento é {segundo_elemento}")

#Adicionando elementos no final
lista.append(60)
print(f"Lista após iserção do 60: {lista}")

#inserir elemento em posição especifica
lista.insert(2, 25)
print(f"Lista pós 25: {lista}")

#removendo elemento da lista
lista.remove(40)
print(f"Lista após remoção do 40: {lista}")

#removendo ultimo elemento
ultimo_elemento = lista.pop()
print(f"numero removido: {ultimo_elemento}")
print(f"Lista pós remoção do ultimo número: {lista}")

#acessando sub-grupo
sub_lista = lista[1:4]
print(f"sublista é : {sub_lista}")

#Lista orndenada
lista.sort()
print(f"Lista ordenada: {lista}")

#iterando sobre elemetos em lista
print(f"iterando elementos")
for elemento in lista:
    print(elemento)
