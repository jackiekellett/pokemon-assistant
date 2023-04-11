import pandas as pd

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
type_chart = type_chart

transpose_type_chart = type_chart.transpose()

pokedex = pokemon_sv['name']
pokedex_list = list(pokedex)


def typez(t1i, t2i, tcp):
    dashes = '–' * 30
    starz = '*' * 30
    poke_type1 = t1i
    poke_type2 = t2i
    weak_to_moves_zero = []
    weak_to_moves_double = []
    weak_to_moves = []
    resistant_to_moves = []
    resistant_to_moves_double = []
    stab1_strong_against = []
    stab1_weak_against = []
    stab1_no_effect = []
    stab2_strong_against = []
    stab2_weak_against = []
    stab2_no_effect = []
    poke_type1_array = type_chart[poke_type1]
    poke_type2_array = type_chart[poke_type2]
    double_type = poke_type1_array * poke_type2_array
    transpose_type1_array = transpose_type_chart[poke_type1]
    transpose_type2_array = transpose_type_chart[poke_type2]
    for t in types:
        if double_type[t] == 0.25:
            weak_to_moves_double.append(t)
        elif double_type[t] == 0:
            weak_to_moves_zero.append(t)
        elif double_type[t] == 0.5:
            weak_to_moves.append(t)
        elif double_type[t] == 2:
            resistant_to_moves.append(t)
        elif double_type[t] == 4:
            resistant_to_moves_double.append(t)
        elif transpose_type1_array[t] == 0:
            stab1_no_effect.append(t)
        elif transpose_type1_array[t] == 0.5:
            stab1_weak_against.append(t)
        elif transpose_type1_array[t] == 2:
            stab1_strong_against.append(t)
        elif transpose_type2_array[t] == 0:
            stab2_no_effect.append(t)
        elif transpose_type2_array[t] == 0.5:
            stab2_weak_against.append(t)
        elif transpose_type2_array[t] == 2:
            stab2_strong_against.append(t)
    print(f"""\n{starz}
{starz}""")
    if tcp == '':
        print("POKEMON TYPES:")
    else:
        print(tcp.upper())

    print(f"""{dashes}
    {types_emojis[poke_type1]} {poke_type1}
    {types_emojis[poke_type2]} {poke_type2}
{starz}""")
    print(f'WEAK TO THESE MOVE TYPES:\n{dashes}')
    for s in resistant_to_moves:
        print(f'     {types_emojis[s]} {s}')
    for s in resistant_to_moves_double:
        print(f'2x   {types_emojis[s]} {s}')
    print(f'{starz}\nRESISTANT TO THESE MOVE TYPES:\n{dashes}')
    for i in weak_to_moves:
        print(f'     {types_emojis[i]} {i}')
    for i in weak_to_moves_double:
        print(f'2x   {types_emojis[i]} {i}')
    for i in weak_to_moves_zero:
        print(f'100% {types_emojis[i]} {i}')
    print(starz)
    print(f"{types_emojis[poke_type1]} STAB MOVE {poke_type1.upper()}:\n{dashes}")
    for a in stab1_strong_against:
        print(f"2x   {types_emojis[a]} {a}")
    for a in stab1_weak_against:
        print(f"2x   {types_emojis[a]} {a}")
    for a in stab1_no_effect:
        print(f"0x   {types_emojis[a]} {a}")
    print(f"{starz}\n{types_emojis[poke_type2]} STAB MOVE {poke_type2.upper()}:\n{dashes}")
    ''
    for z in stab2_strong_against:
        print(f"2x   {types_emojis[z]} {z}")
    for x in stab2_weak_against:
        print(f"0.5x {types_emojis[x]} {x}")
    for y in stab2_no_effect:
        print(f"0x   {types_emojis[y]} {y}")
    return print('Thanks!')
