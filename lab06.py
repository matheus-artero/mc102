###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 6 - Nota de MC102
# Nome: Matheus Eduardo Artero
# RA: 251597
###################################################

# Leitura de dados
n = int(input())
notas = list(float(input()) for _ in range(n))
pesos = list(float(input()) for _ in range(n))

# Cálculo da média ponderada dos laboratórios
media = sum((nota*peso for nota, peso in zip(notas, pesos))) / sum(pesos)
print("Media laboratorios:", format(media, ".1f").replace(".", ","))

# Verificação da situação do aluno
if media >= 5:
    # Caso o aluno tenha sido aprovado por nota
    print("Situacao: Aprovado por nota")
elif media < 2.5:
    # Caso o aluno tenha sido reprovado por nota
    print("Situacao: Reprovado por nota")
else:
    # Cálculo da nota do exame, caso o aluno tenha ido para o exame
    m = int(input())
    exames = list(int(input()) for _ in range(m))
    notas = list(float(input()) for _ in range(m))

    pesos = list(pesos[exame-1] for exame in exames)

    media_exame = sum((nota*peso for nota, peso in zip(notas, pesos))) / sum(pesos)
    media = (media + media_exame) / 2

    if media >= 5:
        # Caso o aluno tenha sido aprovado no exame
        print("Situacao: Aprovado no exame")
    else:
        # Caso o aluno tenha sido repravado no exame
        print("Situacao: Reprovado no exame")

# Saída de dados
nota_final = media
print("Nota final:", format(nota_final, ".1f").replace(".", ","))