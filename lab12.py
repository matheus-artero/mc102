###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 12 - Mansão Mal Assombrada I
# Nome: Matheus Eduardo Artero
# RA: 251597
###################################################

class Hunter():
    def __init__(self, x, y, z):
        self.position = [x, y, z]
        self.is_captured = False
    

class Ghost():
    def __init__(self, x, y, z):
        self.position = [x, y, z]
        self.history = [[x, y, z]]
        
        self.is_gone = (not (0 <= x < A)) or (not (0 <= y < L)) or (not (0 <= z < C))
        self.is_captured = False
    
    def moveTo(self, direction):
        if self.is_gone: return

        if direction == 'C':
            if self.position[0] == A-1: self.is_gone = True
            self.position = [self.position[0]+1, self.position[1], self.position[2]]

        elif direction == 'B':
            if self.position[0] == 0: self.is_gone = True
            self.position = [self.position[0]-1, self.position[1], self.position[2]]

        elif direction == 'N':
            if self.position[1] == 0: self.is_gone = True
            self.position = [self.position[0], self.position[1]-1, self.position[2]]
        
        elif direction == 'S':
            if self.position[1] == L-1: self.is_gone = True
            self.position = [self.position[0], self.position[1]+1, self.position[2]]

        elif direction == 'O':
            if self.position[2] == 0: self.is_gone = True
            self.position = [self.position[0], self.position[1], self.position[2]-1]

        elif direction == 'L':
            if self.position[2] == C-1: self.is_gone = True
            self.position = [self.position[0], self.position[1], self.position[2]+1]

        elif direction == 'X':
            self.is_gone = True
            self.is_captured = True

        if self.position in self.history:
            self.is_gone = True
        else:
            self.history.append(self.position)


def main():
    global A
    global L
    global C

    A, L = [int(v) for v in input().split()]
 
    mansao = [[] for _ in range(A)]
    for andar in range(A-1,-1,-1):
        for _ in range(L):
            mansao[andar].append(list(input()))
        if andar > 0:
            input()

    C = len(mansao[0][0])

    N = int(input())
    fantasmas = list(
        Ghost(*(int(i) for i in input().split())) for _ in range(N)
    )

    M = int(input())
    cacadores = list(
        Hunter(*(int(i) for i in input().split())) for _ in range(M)
    )

    fantasmas_capturados = 0
    cacadores_capturados = 0

    while not all(f.is_gone for f in fantasmas):
        for fantasma in fantasmas:
            if fantasma.is_gone: continue

            for cacador in cacadores:
                if cacador.is_captured or fantasma.position != cacador.position:
                    continue

                cacador.is_captured = True
                cacadores_capturados += 1

            a, l, c = fantasma.position
            direcao = mansao[a][l][c]

            fantasma.moveTo(direcao)
            if fantasma.is_captured: fantasmas_capturados += 1
    
    print(f"fantasmas capturados: {fantasmas_capturados}")
    print(f"caçadores capturados: {cacadores_capturados}")

main()