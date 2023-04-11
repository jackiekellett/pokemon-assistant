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

pokemon_sv['name'] = pokemon_sv['name'].str.strip()

plz_fix_names = pokemon_sv.query(
    "name.str.contains('tauros') or name.str.contains('paldean') or name.str.contains('oricorio')", engine="python")

query = pokemon_sv.count(pokemon_sv.query())

print(query)
