def taximetro(distancia):
    def calc_mult():
        if distancia < 5:
            return 1.2
        else:
            return 1
        
    multiplicador = calc_mult()
    largada = 3
    km_rodado = 2
    valor = (largada + distancia * km_rodado) * multiplicador
    return valor

dist = eval(input("Entre com a distancia percorrida em Km: "))
pagamento = taximetro(dist)
print(f'o valor a pagar é R$ {pagamento}')
