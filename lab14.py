###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 14 - Pulo do Gato
# Nome: Matheus Eduardo Artero
# RA: 251597
###################################################

def catch_the_snack(cat, wall):
    x, y = len(wall), len(wall[0])
    if cat[0] == x or cat[0] < 0 or cat[1] == y or cat[1] < 0:
        return False
    
    if cat in history:
        return False

    history.append(cat)
    value = wall[cat[0]][cat[1]]
    if value == "*":
        return True

    if value == "V":
        a = catch_the_snack([cat[0]+1, cat[1]], wall)
        b = catch_the_snack([cat[0]-1, cat[1]], wall) 
        return a or b

    if value == "H":
        a = catch_the_snack([cat[0], cat[1]+1], wall)
        b = catch_the_snack([cat[0], cat[1]-1], wall)
        return a or b 


def main():
    n = int(input())
    wall = list(input() for _ in range(n))

    cat = list(int(i) for i in input().split())

    global history
    history = []
    if catch_the_snack(cat, wall):
        print("Petisco capturado")
    else:
        print("Petisco não capturado")


main()