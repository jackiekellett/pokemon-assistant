import pandas as pd
from type_mapping import typez

pokemon_sv = pd.read_csv("csv_files/pokemon_fixed.csv")

type_chart = pd.read_csv("csv_files/type_chart.csv")  # attack_type on left

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


def defender(check_pokemon):
    poke_index = pokemon_sv.loc[pokedex == check_pokemon].index[0]
    poke_type1 = pokemon_sv.at[poke_index, 'type1']
    poke_type2 = pokemon_sv.at[poke_index, 'type2']
    return typez(poke_type1, poke_type2, check_pokemon)
