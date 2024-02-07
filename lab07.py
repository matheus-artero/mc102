###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 7 - Gráfico de Recorrência
# Nome: Matheus Eduardo Artero
# RA: 251597
###################################################

def abs_minus(value, term):
    minus = value - term
    return minus if minus >= 0 else -minus 

# Leitura de dados
n = int(input())
valores = list(float(input()) for _ in range(n))
l = float(input())

teste = list(list((1 if abs_minus(valor, i) > l else 0) for i in valores) for valor in valores)

# Impressão do gráfico de recorrência
for linha in teste: print(" ".join(str(i) for i in linha))
