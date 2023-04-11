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
transpose_type_chart = type_chart.transpose()

pokedex = pokemon_sv['name']
pokedex_list = list(pokedex)

# poke = input(f"Pokemon?\n")

# poke_index = pokemon_sv.loc[pokedex == poke].index[0]
# poke_type1 = pokemon_sv.at[poke_index, 'type1']
# poke_type2 = pokemon_sv.at[poke_index, 'type2']

def note_1():
    for a in types_format:
        b = types_format.index(a) + 10
        if types_format.index(a) < 9:
            print(f"{types_format.index(a)}. {types_emojis[a]} {a}        {b}. {types_emojis[b]} {types_format[b]}")
        elif types_format.index(a) < 10:
            print(f"{types_format.index(a)}. {types_emojis[a]} {a}  ")
    print('-' * 30)

note_1()