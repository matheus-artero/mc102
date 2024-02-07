###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 11 - Loteamento
# Nome: Matheus Eduardo Artero
# RA: 251597
###################################################

# Leitura de dados
ruas_x = tuple(int(x) for x in input().split())
ruas_y = tuple(int(x) for x in input().split())

loteamento = list(list(("." if i in ruas_x or j in ruas_y else "x") for j in range(15)) for i in range(15))

## compradores
n = int(input())

# Processamento
for index in range(n):
  coords = tuple(int(x) for x in input().split())

  aux_loteamento =  list(list(item for item in linha) for linha in loteamento)
  is_valid = True

  for i in range(coords[0], coords[2]+1):
    for j in range(coords[1], coords[3]+1):
      if aux_loteamento[i][j] == 'x':
        aux_loteamento[i][j] = str(index+1)
      else:
        is_valid = False

  if not is_valid: continue
  loteamento = list(list(item for item in linha) for linha in aux_loteamento)

# Impressão da saída
for linha in loteamento:
  print(" ".join(linha))