###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 2 - Um Lanche Antes da Aula
# Nome: Matheus Eduardo Artero
# RA: 251597
###################################################

_preco_passagem = 6
_limite_tempo = 45

# Leitura da entrada
t = float(input())
l1 = float(input())
l2 = float(input())
p1 = float(input())
p2 = float(input())
p3 = float(input())


# Comparação entre as opções e impressão da saída
class Route():
    time = 0
    cost = 0

    def __init__(self, cost, time):
        self.cost = cost
        self.time = time


def faster_route(tempo1, tempo2):
    if tempo1 < tempo2:
        return True

    if tempo1 > tempo2:
        return False
    
    return True


def cheaper_route(custo1, custo2):
    if custo1 < custo2:
        return True

    if custo1 > custo2:
        return False
    
    return True


def valid_route(tempo1, tempo2):
    if tempo1 < _limite_tempo <= tempo2:
        return 1
    
    if tempo1 >= _limite_tempo > tempo2:
        return 2

    if tempo1 >= tempo2 > _limite_tempo or tempo2 >= tempo1 > _limite_tempo:
        return 3
    
    return 0


def find_best_route(route1, route2):
    valid = valid_route(route1.time, route2.time)

    if valid == 1:
        return True
    
    if valid == 2:
        return False
    
    if valid == 3: # nenhuma dá tempo
        return faster_route(route1.time, route2.time)
    
    if valid == 0: # duas dão tempo
        return cheaper_route(route1.cost, route2. cost) 
    

route1 = Route(
    cost=(l1 + _preco_passagem * 2),
    time=(t + p1 + p2)
)

route2 = Route(
    cost=(l2 + _preco_passagem),
    time=(t + p3)
)

print(find_best_route(route1, route2))
