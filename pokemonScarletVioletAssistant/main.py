import sys
import time
import pandas as pd
import name_check
import type_mapping

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


counter_mm = 0
counter_timer = 0


def timer(counter_timer=counter_timer):
    tr = time.perf_counter_ns() / 1000000000
    # print(counter_timer, ': ', tr)
    counter_timer += 1


timer(counter_timer) # 0


def begin():
    print("""
 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄    ▄  ▄▄▄▄▄▄▄▄▄▄▄                         ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌  ▐░▌▐░░░░░░░░░░░▌                       ▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌ ▐░▌ ▐░█▀▀▀▀▀▀▀▀▀                        ▐░▌░▌   ▐░▐░▌▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ 
▐░▌       ▐░▌▐░▌       ▐░▌▐░▌▐░▌  ▐░▌                                 ▐░▌▐░▌ ▐░▌▐░▌▐░▌       ▐░▌     ▐░▌     ▐░▌          
▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░▌░▌   ▐░█▄▄▄▄▄▄▄▄▄       ▄▄▄▄▄▄▄▄▄▄▄      ▐░▌ ▐░▐░▌ ▐░▌▐░█▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░▌    ▐░░░░░░░░░░░▌     ▐░░░░░░░░░░░▌     ▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀▀▀ ▐░▌       ▐░▌▐░▌░▌   ▐░█▀▀▀▀▀▀▀▀▀       ▀▀▀▀▀▀▀▀▀▀▀      ▐░▌   ▀   ▐░▌▐░█▀▀▀▀▀▀▀█░▌     ▐░▌     ▐░█▀▀▀▀▀▀▀▀▀ 
▐░▌          ▐░▌       ▐░▌▐░▌▐░▌  ▐░▌                                 ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░▌          
▐░▌          ▐░█▄▄▄▄▄▄▄█░▌▐░▌ ▐░▌ ▐░█▄▄▄▄▄▄▄▄▄                        ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░█▄▄▄▄▄▄▄▄▄ 
▐░▌          ▐░░░░░░░░░░░▌▐░▌  ▐░▌▐░░░░░░░░░░░▌                       ▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░░░░░░░░░░░▌
 ▀            ▀▀▀▀▀▀▀▀▀▀▀  ▀    ▀  ▀▀▀▀▀▀▀▀▀▀▀                         ▀         ▀  ▀         ▀       ▀       ▀▀▀▀▀▀▀▀▀▀▀ """)
    timer(counter_timer) # 1
    return main_menu()


def note_type():
    print('\n\n')
    for a in types:
        egla = 0
        if len(a) < 8:
            egla = 8 - len(a)
        b = types.index(a) + 10
        if types.index(a) < 9:
            print(f"{types.index(a)}. {types_emojis[a]} {a}{' ' * egla}        {b}. {types_emojis[types[b]]} {types[b]}")
        elif types.index(a) < 10:
            print(f"{types.index(a)}. {types_emojis[a]} {a}")
        else:
            pass
    print('-' * 30)


def main_menu():
    check_pokemon = ''
    timer(counter_timer) # 2
    options_list = ['name']  # , 'type']
    """
    ^ can adjust back once 'search_input' is fixed
    """
    time.sleep(0.45)
    print(f"""
{'◓ ◑ ◒ ◐ ' * 10}
{'◐ ◒ ◑ ◓ ' * 10}""")
    time.sleep(0.225)
    print(f"""
╔═╗╔═╗╔═╗╦═╗╔═╗╦ ╦  ╔╗ ╦ ╦  ┌─┐
╚═╗║╣ ╠═╣╠╦╝║  ╠═╣  ╠╩╗╚╦╝   ┌┘
╚═╝╚═╝╩ ╩╩╚═╚═╝╩ ╩  ╚═╝ ╩    o """)
    timer(counter_timer) # 3
    print('==' * 16)

    for item in options_list:
        print(f"  {options_list.index(item) + 1}. {item.capitalize()}                   ")
    print('==' * 16)
    timer(counter_timer) # 4
    search_input = 1  # float(input("Please choose an option. [#]\n>>> "))
    """
    ^^^ issues with the 'type' search working properly, can debug later; fix 'options_list' once complete
    """

    if search_input == 'exit' or counter_mm > 2:
        print('❌ Aborting!')
        return sys.exit()
    elif float(search_input) - 1 == 0:
        return name_search()
    elif float(search_input) - 1 == 1:
        note_type()
        type1_input = input(f"What is the 1st type? [#]\n").lower()
        if types[int(type1_input)] not in types:
            print("Seriously? Aborting.")
            return exit()
        type2_input = input(f"What is the 2nd type? [#]\n").lower()
        if types[int(type2_input)] not in types:
            print("Seriously? Aborting.")
            return exit()
        return type_search(type1_input, type2_input, check_pokemon)
    else:
        print("⚠️ Something looks off. Try again.")
        return main_menu()


def name_search():
    timer(counter_timer)
    name_check.startup()
    pass


def type_search(type1_input, type2_input, check_pokemon):
    timer(counter_timer)
    type_mapping.typez(type1_input, type2_input, check_pokemon)
    pokemon_sv.query(f"(type1 == {type1_input} & type2 == {type2_input}) or (type1 == {type2_input})")
    pass


begin()

timer(counter_timer)

# long process here
