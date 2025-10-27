import math

#Formula de baskara, vulgo calculo fundamental da equação de 2° grau

def calcular_raizes(a, b, c):
    delta = b ** 2 - (4 * a * c)

    #calcular a raiz de delta
    if delta > 0:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        return(raiz1, raiz2)
    elif delta == 0:
        raiz = -b / (2 * a)
        return(raiz)
    else:
        parte_real = -b / (2 * a)
        parte_imaginária = math.sqrt(-delta) / (2 * a)
        raiz1 = complex(parte_real, parte_imaginária)
        raiz2 = complex(parte_real, -parte_imaginária)
        return(raiz1, raiz2)
    
#solicitação dos coeficientes do usuario

a = float(input("Selecione o coeficiente de a: "))
b = float(input("Selecione o coeficiente de b: "))
c = float(input("Selecione o coeficiente de c: "))

raizes = calcular_raizes(a, b, c)

if len(raizes) == 2:
    print(f"As raízes da equação são respectivamente: {raizes[0]} e {raizes[1]}")
else:
    print(f"E raíz da equação é: {raizes[0]}")

    