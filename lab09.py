###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 9 - Criptografia Cíclica
# Nome: Matheus Eduardo Artero
# RA: 251597
###################################################

# Leitura da entrada
chave = input()
mensagem = input()


# Decodificação da mensagem
decode = ""
for letra in mensagem:
    try:
        index = chave.index(letra.lower())
        decode += chave[index-1] if letra.islower() else chave[index-1].upper()
    except:
        decode += letra


# Impressão da saída
print(decode)