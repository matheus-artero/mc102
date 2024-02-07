#####################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 10 - Caçadores de Tesouros
# Nome: Matheus Eduardo Artero
# RA: 251597
#####################################################


class Player():
    def __init__(self, x, y, board):
        self.position = [x, y]
        self.reward = board[x][y]
        board[x][y] = 0
    
    def moveTo(self, direction, limits, board):
        if direction == 'N' and self.position[0] != 0:
            self.position = [self.position[0]-1, self.position[1]]
        
        elif direction == 'S' and self.position[0] != limits[0]-1:
            self.position = [self.position[0]+1, self.position[1]]

        elif direction == 'O' and self.position[1] != 0:
            self.position = [self.position[0], self.position[1]-1]

        elif direction == 'L' and self.position[1] != limits[1]-1:
            self.position = [self.position[0], self.position[1]+1]

        self.handle_reward(board)

    def handle_reward(self, board):
        reward = board[self.position[0]][self.position[1]]
        if self.reward < reward:
            board[self.position[0]][self.position[1]] = self.reward
            self.reward = reward


def main():
    n, m = [int(i) for i in input().split()]

    mapa = []
    for _ in range(n):
        linha = [int(i) for i in input().split()]
        mapa.append(linha)

    q = int(input())

    for i in range(q):
        pos = tuple(int(x) for x in input().split())
        player = Player(pos[0], pos[1], mapa)

        moves = input()

        for move in moves:
            player.moveTo(move, (n, m), mapa)
        
        print(f"Caçador {i+1}: {player.reward}")

main()
