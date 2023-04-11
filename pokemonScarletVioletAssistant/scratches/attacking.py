import pandas as pd

pokemon_sv = pd.read_csv("../csv_files/pokemon_fixed.csv")

type_chart = pd.read_csv("../csv_files/type_chart.csv")  # attack_type on left

types = ['normal', 'fire', 'water', 'grass', 'electric', 'ice', 'fighting', 'poison', 'ground',
         'flying', 'psychic', 'bug', 'rock', 'ghost', 'dragon', 'dark', 'steel', 'fairy', 'none']

types_emojis = {'normal': '⚪️', 'fire': '🔥', 'water': '💧', 'grass': '🌱', 'electric': '⚡️', 'ice': '❄️',
                'fighting': '🥊', 'poison': '🟣', 'ground': '🌍', 'flying': '🎈', 'psychic': '🔮', 'bug': '🐛',
                'rock': '🪨', 'ghost': '👻', 'dragon': '🐉', 'dark': '🌘', 'steel': '⚙️', 'fairy': '🎀', 'none': '  '}

types_format = ['normal  ', 'fire    ', 'water   ', 'grass   ', 'electric', 'ice     ', 'fighting', 'poison  ',
                'ground  ',
                'flying  ', 'psychic ', 'bug     ', 'rock    ', 'ghost   ', 'dragon  ', 'dark    ', 'steel   ',
                'fairy   ', 'none    ']

del type_chart['attack_type']

type_chart.index = types

def types_by_number():
    for a in types_format:
        if types_format.index(a) < 9:
            print(
                f"{types_format.index(a)}: {a}        {types_format.index(a) + 10}: {types_format[types_format.index(a) + 10]}")
        elif types_format.index(a) < 10:
            print(f"{types_format.index(a)}: {a}")

types_by_number()

pokedex = pokemon_sv['name']
pokedex_list = list(pokedex)

my_pokemon = input("\nWhat is YOUR pokemon?\n")

my_ineffective = []
my_supereffective = []



def attacker():
    if my_pokemon in pokedex_list:
        my_poke_index = pokemon_sv.loc[pokedex == my_pokemon].index[0]
        my_poke_type1 = pokemon_sv.at[my_poke_index, 'type1']
        my_poke_type2 = pokemon_sv.at[my_poke_index, 'type2']
        my_poke_type1_array = type_chart[my_poke_type1]
        my_poke_type2_array = type_chart[my_poke_type2]
        my_double_type = my_poke_type1_array * my_poke_type2_array
        print(my_double_type)
#        for t in types:
#            if my_double_type[t] < 1:
#                my_ineffective.append(t)
#            elif my_double_type[t] > 1:
#                my_supereffective.append(t)
#        print('\nSUPEREFFECTIVE:')
#        for s in my_supereffective:
#            print(s)
#        print('\nINEFFECTIVE:')
#        for i in my_ineffective:
#            print(i)
    else:
        print("""ERROR!!!
        PLEASE CHECK SPELLING.""")

attacker()