import pandas as pd

pokemon_sv = pd.read_csv("/Users/ishmael/Downloads/pokemon_fixed.csv")

type_chart = pd.read_csv("/Users/ishmael/Downloads/type_chart.csv")  # attack_type on left

types = ['normal', 'fire', 'water', 'grass', 'electric', 'ice', 'fighting', 'poison', 'ground',
         'flying', 'psychic', 'bug', 'rock', 'ghost', 'dragon', 'dark', 'steel', 'fairy', 'none']

types_format = ['normal  ', 'fire    ', 'water   ', 'grass   ', 'electric', 'ice     ', 'fighting', 'poison  ',
                'ground  ',
                'flying  ', 'psychic ', 'bug     ', 'rock    ', 'ghost   ', 'dragon  ', 'dark    ', 'steel   ',
                'fairy   ', 'none    ']

del type_chart['attack_type']

type_chart.index = types

poke_type_chart_transposed = type_chart.transpose()  # attack_type at TOP

def funny():
    for a in types_format:
        if types_format.index(a) < 9:
            print(
                f"{types_format.index(a)}: {a}        {types_format.index(a) + 10}: {types_format[types_format.index(a) + 10]}")
        elif types_format.index(a) < 10:
            print(f"{types_format.index(a)}: {a}")

funny()

opposing_pokemon = input("Opposing pokemon's name?\n")

opp_poke_index = pokemon_sv.loc[pokemon_sv['name'] == opposing_pokemon].index[0]
opp_poke_type1 = pokemon_sv.at[opp_poke_index, 'type1']
opp_poke_type2 = pokemon_sv.at[opp_poke_index, 'type2']
opp_poke_type1_array = type_chart[opp_poke_type1]
opp_poke_type2_array = type_chart[opp_poke_type2]

double_type = opp_poke_type1_array * opp_poke_type2_array

ineffective = []
supereffective = []

for t in types:
    if double_type[t] < 1:
        ineffective.append(t)
    elif double_type[t] > 1:
        supereffective.append(t)


print("\nSUPEREFFECTIVE:")
for e in supereffective:
    print(e)

print("\nINEFFECTIVE:")
for i in ineffective:
    print(i)