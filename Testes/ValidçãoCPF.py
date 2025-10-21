def validar_cpf(cpf):
    #Remover carcteres numéricos
    cpf = ''.join(filter(str.isdigit, cpf))

    #verificar se tem 11 digitos
    if len(cpf) != 11:
        return False
    
    #verificar se todos os digitos são iguais
    if cpf == cpf[0] * 11:
        return False
    
    #calculo do primeiro digito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    resto = soma % 11
    if resto < 2:
        verificador_1 = 0
    else:
        verificador_1 = 11 - resto
    
    #Verificando erros no primeiro digito verificador
    if int(cpf[9]) != verificador_1:
        return False 
    
    #Calculo do segundo digito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    resto = soma % 11
    if resto < 2:
        verificador_2 = 0
    else:
        verificador_2 = 11 - resto
    
    #Verificando erros no primeiro digito verificador
    if int(cpf[10]) != verificador_2:
        return False
    

    #CPF VÁLIDO
    return True

#Testando a função
cpf = "077.241.503.03"
if validar_cpf(cpf):
    print(f"\nO CPF {cpf} é Válido\n")
else:
    print(f"\nO CPF {cpf} NÃO é válido\n")