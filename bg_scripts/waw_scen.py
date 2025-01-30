#!/usr/bin/python3

"""
Scenario searcher/information for World at War 85 by LNL
"""

import os

from steve_utils.output_utils import double_print

valid_countries = ['Soviet Union', 'West Germany', 'United Kingdom', 'United States']

if os.getcwd().endswith('board_games'):
    file_h = open('DB/WorldAtWar85Scens.txt', 'r', encoding="UTF-8")
else:
    file_h = open('board_games/DB/WorldAtWar85Scens.txt', 'r', encoding="UTF-8")

scenarios = []
map_dict = {}
for line in file_h.readlines():
    if line.startswith('#'):
        continue
    line = line.strip()
    scenario_name, in_sov_country, in_allied_country, scen_location, in_maps, turns, product \
        = line.split(';')
    sov_countries = []
    allied_countries = []
    for country in in_sov_country.split(','):
        if country.strip() not in valid_countries:
            print("Invalid Soviet country: " + country.strip())
        else:
            sov_countries.append(country.strip())
    for country in in_allied_country.split(','):
        if country.strip() not in valid_countries:
            print("Invalid allied country: " + country.strip())
        else:
            allied_countries.append(country.strip())
    maps = []
    for in_map in in_maps.split(','):
        maps.append(int(in_map.strip()))
    for used_map in maps:
        if used_map not in map_dict:
            map_dict[used_map] = 0
        map_dict[used_map] += 1
    if turns != 'Variable':
        turns = int(turns)
    if product not in ['Operation Red Gauntlet']:
        print("Invalid product: " + product)
    scenarios.append((scenario_name, sov_countries, allied_countries, scen_location, \
        maps, turns, product))

if __name__ == "__main__":
    if os.getcwd().endswith('board_games'):
        out_file_h = open("output/WAWScenarios.txt", 'w', encoding="UTF-8")
    else:
        out_file_h = open("board_games/output/WAWScenarios.txt", 'w', encoding="UTF-8")

    double_print(f"There are {len(scenarios)} total scenarios.", out_file_h)

    map_sorted = sorted(map_dict.items(), key=lambda x:x[1], reverse=True)
    map_str = f"Out of {len(map_dict)} maps, map {map_sorted[0][0]} is the most used - " + \
        f"{map_sorted[0][1]} times."
    double_print(map_str, out_file_h)
    map_str = f"Least used map is {map_sorted[-1][0]} - only used {map_sorted[-1][1]} time(s)."
    double_print(map_str, out_file_h)

    turn_scenarios = filter(lambda x: x[5] != 'Variable', scenarios)
    scen_sorter = sorted(turn_scenarios, key = lambda x: (x[5], x[0]))
    shortest_scenario = scen_sorter[0]
    longest_scenario = scen_sorter[-1]
    length_str = f"Shortest scenario is {shortest_scenario[0]} ({shortest_scenario[5]} turns)" + \
        f"; longest is {longest_scenario[0]} ({longest_scenario[5]} turns)"
    double_print(length_str, out_file_h)
