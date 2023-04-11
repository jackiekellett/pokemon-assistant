import sys
import time

import pandas as pd
from Levenshtein import distance as lev
from tqdm import tqdm
import defending

pokemon_sv = pd.read_csv("csv_files/pokemon_fixed.csv")

type_chart = pd.read_csv("csv_files/type_chart.csv")  # attack_type on left

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

pokemon_sv['name'] = pokemon_sv['name'].str.strip()

plz_fix_names = pokemon_sv.query(
    "name.str.contains('tauros') or name.str.contains('paldean') or name.str.contains('oricorio')", engine="python")

b = '*' * 80
d = '-' * 80
super_short = 0.0001
short = 0.003
med = 0.005
long = 0.008
very_long = 0.01


def load(interval: float):
    """
    :param interval:
    :return:
    """
    for t in tqdm(range(100),
                  desc="Loading…",
                  ascii=False, ncols=75):
        time.sleep(interval)

def inper():
    print(f"""{d}
┌─┐┌─┐┬┌─┌─┐┌┬┐┌─┐┌┐┌  ┌┐┌┌─┐┌┬┐┌─┐  ┌─┐
├─┘│ │├┴┐├┤ ││││ ││││  │││├─┤│││├┤    ┌┘
┴  └─┘┴ ┴└─┘┴ ┴└─┘┘└┘  ┘└┘┴ ┴┴ ┴└─┘   o """)
    check_pokemon = input("Pokemon name? >>> ").lower()
    load(short)
    if check_pokemon in pokedex_list:
        return defending.defender(check_pokemon)
    elif check_pokemon == 'exit':
        print('❌ Aborting!')
        sys.exit()
    else:
        return pokec(check_pokemon)


def pokec(check_pokemon):
    counter_pokec_1 = 0
    lev_vals = {}
    min_lev_vals = []
    for p in pokedex_list:
        lev_vals[p] = lev(check_pokemon, p)
    min_lev = min(lev_vals.values())
    while len(min_lev_vals) < 10:
        for k, v in lev_vals.items():
            if v == min_lev:
                min_lev_vals.append(k)
        min_lev += 1
    print(f"Hmmm...\n⚠️ Unable to find...'{check_pokemon.upper()}'...")
    time.sleep(0.45)
    print(f"Did you mean one of these?")
    time.sleep(0.45)
    print(d)
    for m in range(5):
        print(f"{m}. {min_lev_vals[m].capitalize()}")
    time.sleep(0.5)
    num_response = input("\nPlease type the NUMBER of the correct pokemon.\nType 'no' if no matches.\n>>> ")
    lnr = num_response.lower()
    if lnr == 'none' or lnr == 'restart' or lnr == 'no':
        print("Okay! Let's start over...\n")
        return inper()
    elif lnr == 'exit' or counter_pokec_1 >= 1:
        print("❌ Aborting!")
        return sys.exit()
    else:
        while check_pokemon not in pokedex_list:
            counter_pokec_1 += 1
            try:
                int_num_response = int(num_response)
                check_pokemon = min_lev_vals[int_num_response]
                break
            except ValueError:
                print('⚠️ INPUT ERROR. TRY AGAIN.')
                num_response = input("Please type the NUMBER of the correct pokemon. Type 'no' if no matches.\n>>> ")
                if num_response.lower() == 'no':
                    print("Okay! Let's start over...\n")
                    return inper()
                elif num_response.lower() == 'exit':
                    print("❌ Aborting!")
                    return sys.exit()
        return defending.defender(check_pokemon)


def startup():
    """

██████╗  ██████╗ ██╗  ██╗███████╗     █████╗ ███████╗███████╗██╗███████╗████████╗
██╔══██╗██╔═══██╗██║ ██╔╝██╔════╝    ██╔══██╗██╔════╝██╔════╝██║██╔════╝╚══██╔══╝
██████╔╝██║   ██║█████╔╝ █████╗      ███████║███████╗███████╗██║███████╗   ██║   
██╔═══╝ ██║   ██║██╔═██╗ ██╔══╝      ██╔══██║╚════██║╚════██║██║╚════██║   ██║   
██║     ╚██████╔╝██║  ██╗███████╗    ██║  ██║███████║███████║██║███████║   ██║   
╚═╝      ╚═════╝ ╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝╚══════╝   ╚═╝   

"""
    time.sleep(0.5)
    print(f"""{b}
PLEASE NOTE THESE SPECIAL NAMES
{b}""")
    for n in list(plz_fix_names['name']):
        print(f'    {n}')
    time.sleep(0.3)
    df = pd.DataFrame({"x": ["LongStringNumber1", "LongStringNumber2"]})
    df["x"] = df["x"].str.slice(start=5, stop=10)
    return inper()
