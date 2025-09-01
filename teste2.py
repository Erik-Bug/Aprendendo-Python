hamburguer = 10.50
batata_frita = 4.50
Refrigerante = 3.00

quant_hamburguer = int(input("Digite a quantidade de hambúrgueres desejados: "))
quant_batata = int(input("Digite a quantidade de Batata frita desejados: "))
quant_Refrigerante = int(input("Digite a quantidade de refrigerante desejados: "))

Preço_total = (hamburguer * quant_hamburguer) + (batata_frita * quant_batata) + (Refrigerante * quant_Refrigerante)

print(f"O preço total é de: {Preço_total: .2f}")