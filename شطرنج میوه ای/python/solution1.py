# https://quera.org/problemset/60134/

def fruits(fruit_list):
    f_name = [fruit['name'] for fruit in fruit_list if 
            fruit['shape'] == 'sphere' and
            300<=fruit['mass'] <= 600 and
            100<=fruit['volume'] <=500]
    
    return {name:f_name.count(name) for name in set(f_name)}

# GoodFrts = fruits((
#     {'name': 'apple', 'shape': 'sphere', 'mass': 350, 'volume': 120},
#     {'name': 'mango', 'shape': 'square', 'mass': 150, 'volume': 120},
#     {'name': 'lemon', 'shape': 'sphere', 'mass': 300, 'volume': 100},
#     {'name': 'apple', 'shape': 'sphere', 'mass': 500, 'volume': 250}))

# print(GoodFrts)