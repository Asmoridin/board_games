from itertools import combinations

PLAYER_THRESHOLDS = [17,18,21,25,28]

#Make sure to check for 2nd Vagabond
items = Factions

for player_count in range(2,6):
    combos = list(combinations(items, player_count))
