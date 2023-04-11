import pandas as pd

pokemon_sv = pd.read_csv("../csv_files/pokemon_fixed.csv")

type_chart = pd.read_csv("../csv_files/type_chart.csv")  # attack_type on left

types = ['normal', 'fire', 'water', 'grass', 'electric', 'ice', 'fighting', 'poison', 'ground',
         'flying', 'psychic', 'bug', 'rock', 'ghost', 'dragon', 'dark', 'steel', 'fairy', 'none']

types_format = ['normal  ', 'fire    ', 'water   ', 'grass   ', 'electric', 'ice     ', 'fighting', 'poison  ',
                'ground  ',
                'flying  ', 'psychic ', 'bug     ', 'rock    ', 'ghost   ', 'dragon  ', 'dark    ', 'steel   ',
                'fairy   ', 'none    ']

del type_chart['attack_type']

type_chart.index = types
transpose_type_chart = type_chart.transpose()

pokedex = pokemon_sv['name']
pokedex_list = list(pokedex)

def searcher():
    print("Thanks for using the Pokemon Searcher.")
    search_type1 = input("What TYPE of pokemon can we help you find today?\n").lower()
    search_type2 = input("What is the 2nd TYPE of the pokemon?\n(Type 'none' for single-type only. Type 'no' if you do not want to specify a 2nd type.)\n").lower()
    if search_type2 != 'no':
        search_query = pokemon_sv.query(f"type1 == '{search_type1}' & type2 == '{search_type2}'")
    else:
        search_query = pokemon_sv.query(f"type1 == '{search_type1}'")
    print(search_query)
    exit


searcher()