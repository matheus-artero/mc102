###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 15 - Mansão Mal Assombrada II
# Nome: 
# RA: 
###################################################

historico = []

'''
Função para encontrar um caminho até a saída, essa função deve ser implementada
de forma recursiva. A função recebe a matriz representando a mansão, um valor
booleano p, indicando se você já encontrou o escudo e está protegido dos
fantasmas, e valores inteiros a, l e c, representando o andar atual, a linha
atual e a coluna atual, respectivamente. A função deve retornar True, caso
exista uma saída, ou False, caso contrário.'''
def simula_caminho(mansao, p, a, l, c):
    p1, p2, p3, p4, p5, p6 = (False, False, False, False, False, False)
    global historico
    
    try:
        valor = mansao[a][l][c]
    except IndexError:
        return False

    if (a,l,c) in historico:
        return False

    if valor == "=":
        return True
    
    if valor == "F" and not p:
        return False

    if valor == "@":
        p = True
        historico = []

    if valor == "*":
        return False

    historico.append((a,l,c))
    p1 = simula_caminho(mansao, p, a, l, c+1)
    p2 = simula_caminho(mansao, p, a, l, c-1)
    p3 = simula_caminho(mansao, p, a, l+1, c)
    p4 = simula_caminho(mansao, p, a, l-1, c)

    if valor == "#":
        if A > a+1 and mansao[a+1][l][c] == "#":
            p5 = simula_caminho(mansao, p, a+1, l, c)
        if a-1 >= 0 and mansao[a-1][l][c] == "#":
            p6 = simula_caminho(mansao, p, a-1, l, c)
    
    return any((p1, p2, p3, p4, p5, p6))


# Leitura da matriz representando a mansão
A, L = [int(v) for v in input().split()]
mansao = [[] for _ in range(A)]

for andar in range(A-1,-1,-1):
    for _ in range(L):
      mansao[andar].append(list(input()))
    if andar > 0:
        input()

a0, l0, c0 = [int(v) for v in input().split()]

# Simulação do caminho
escapou = simula_caminho(mansao, False, a0, l0, c0)

# Impressão da saída
if escapou:
    print("Caminho para saida encontrado com sucesso.")
else:
    print("Nao existe caminho seguro para a saida.")