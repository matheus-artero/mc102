###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 5 - A Última Rodada
# Nome: Matheus Eduardo Artero
# RA: 251597
###################################################


def get_premio(ganho, valor):
    sinal, valor, operador = valor.split()

    valor = ganho * float(valor)/100 if operador == "%" else float(valor)
    valor = valor if sinal == "+" else -valor
    
    premio = ganho + valor  
    return premio if ganho >= -valor else 0


# Leitura da primeira linha
N, V, P = input().split()
N = int(N)
V = int(V)
P = int(P)

# Leitura da roleta
roleta = list(input() for _ in range(N))

# Calculo da probabilidade
premios = []
sucessos = 0

for caso in roleta:
    premio = get_premio(P, caso)
    premios.append(premio)

    if premio >= V: sucessos += 1

prob_viagem = (sucessos/N) * 100
premio_medio = sum(premios)/len(premios)

# Imprime a probabilidade do premio final ser suficiente para a viagem
print("{:.2f}%".format(prob_viagem))
# Imprime o valor médio do premio final a ser recebido
print("R$ {:.2f}".format(premio_medio))