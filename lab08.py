###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 8 - Anagramas
# Nome: Matheus Eduardo Artero
# RA: 251597
###################################################

# Leitura das palavras
n = int(input())
palavras = list(input() for _ in range(n))
aux = palavras.copy()

def ache_anagramas_de(x):

    resultado = []
    for item in palavras:
        if len(x) != len(item): continue
        if {letter: x.count(letter) for letter in x} != {letter: item.count(letter) for letter in item}:
            continue

        resultado.append(item)

    return resultado

# Agrupamento dos anagramas e Impressão da saída
for palavra in palavras:
    if palavra not in aux: continue
    anagramas = ache_anagramas_de(palavra)

    _ = list(aux.remove(anagrama) for anagrama in anagramas)
    print('-'.join(anagramas)) if anagramas else print(palavra)