###################################################
# MC102 - Algoritmos e Programação de Computadores
# Laboratório 4 - Batalha Pokémon
# Nome: Matheus Eduardo Artero
# RA: 251597
###################################################

# Leitura do hp e velocidade dos pokémons
hp_ivysaur = int(input())
hp_pikachu = int(input())

speed_ivysaur = int(input())
speed_pikachu = int(input())

pokemons = {
    1: {
        "name": "Ivysaur",
        "hp": hp_ivysaur,
        "speed": speed_ivysaur,
    },
    -1: {
        "name": "Pikachu",
        "hp": hp_pikachu,
        "speed": speed_pikachu,
    }
}


# Leitura dos ataques dos turnos
pokemon = 1 if pokemons[1]["speed"] >= pokemons[-1]["speed"] else -1
while True:
    strength1 = int(input())
    effectiveness1 = float(input())
    damage1 = strength1 * effectiveness1
    
    strength2 = int(input())
    effectiveness2 = float(input())
    damage2 = strength2 * effectiveness2
    
    pokemon = -(pokemon)
    pokemons[pokemon]["hp"] -= damage1

    if pokemons[pokemon]["hp"] <= 0:
        pokemons[pokemon]["hp"] = 0
        print("HP %s = %d" % (pokemons[1]["name"], pokemons[1]["hp"]))
        print("HP %s = %d" % (pokemons[-1]["name"], pokemons[-1]["hp"]))
        break
    
    pokemon = -(pokemon)
    pokemons[pokemon]["hp"] -= damage2

    if pokemons[pokemon]["hp"] <= 0:
        pokemons[pokemon]["hp"] = 0
        print("HP %s = %d" % (pokemons[1]["name"], pokemons[1]["hp"]))
        print("HP %s = %d" % (pokemons[-1]["name"], pokemons[-1]["hp"]))
        break

    print("HP %s = %d" % (pokemons[1]["name"], pokemons[1]["hp"]))
    print("HP %s = %d" % (pokemons[-1]["name"], pokemons[-1]["hp"]))


# Impressão do vencedor
if pokemons[1]["hp"] > 0:
    print("Pokémon Vencedor: %s" % pokemons[1]["name"])
    print("HP do Vencedor: %d" % pokemons[1]["hp"])
else:
    print("Pokémon Vencedor: %s" % pokemons[-1]["name"])
    print("HP do Vencedor: %d" % pokemons[-1]["hp"])