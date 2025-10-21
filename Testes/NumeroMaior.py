def encontrar_maior_elemento(lista):
    if len(lista) <= 1:
        return lista[0]

    maior_elemento = lista[0]
    for numero in lista[1:]:
        if numero > maior_elemento:
            maior_elemento = numero
    return maior_elemento
    
lista_exemplo = [1, 3, 5, 8 ,9, 7, 2]
maior_elemento = encontrar_maior_elemento(lista_exemplo)
print(f"O maior elemento da lista é: {maior_elemento}")