###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 3 - Investimento em Renda Fixa
# Nome: Matheus Eduardo Artero
# RA: 251597
###################################################

# leitura de dados
mont_inicial = float(input())
dias_aplicados = int(input())

juros_acumulados_perc = float(input()) / 100
juros_fixados_tesouro = float(input()) / 100


# cálculo dos rendimentos
poupanca = mont_inicial * juros_acumulados_perc
tesouro = mont_inicial * juros_fixados_tesouro

if dias_aplicados <= 180:
	perc_imp_renda = 22.5 / 100
elif 181 <= dias_aplicados <= 360:
	perc_imp_renda = 20 / 100
elif 361 <= dias_aplicados <= 720:
	perc_imp_renda = 17.5 / 100
else:
	perc_imp_renda = 15 / 100

tesouro = tesouro - (tesouro * perc_imp_renda)


# Impressão da saída
print("Rendimento poupança: {:.2f}".format(poupanca))
print("Rendimento tesouro: {:.2f}".format(tesouro))

if poupanca > tesouro:
	print("Maior rendimento: poupança")
else:
	print("Maior rendimento: tesouro")