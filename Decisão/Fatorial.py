# Implementação procedural (função simples)
def fatorial(n):
    if n == 0:
        return 1
    else: 
        return n * fatorial(n-1)

print("Fatorial de 5 (procedural):", fatorial(6))

# Implementação orientada a objetos
class Fatorial:
    def calcular(self, n):
        if n == 0:
            return 1
        else:
            return n * self.calcular(n-1)

f = Fatorial()  # Note o F maiúsculo (nome da classe)
print("Fatorial de 5 (orientado a objetos):", f.calcular(6))
            
            