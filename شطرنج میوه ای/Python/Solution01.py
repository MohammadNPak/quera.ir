GoodFruits = {}
GoodFruitsList = []


def fruits(FruitsSpecifications):
    for fruit in FruitsSpecifications:
        FruitName = fruit['name']
        if (fruit['shape'] == 'sphere') and (300 <= fruit['mass'] <= 600) and (100 <= fruit['volume'] <= 500):
            GoodFruitsList.append(FruitName)
    for item in GoodFruitsList:
        FrtCnt = GoodFruitsList.count(item)
        GoodFruits[item] = FrtCnt
    return GoodFruits


GoodFrts = fruits((
    {'name': 'apple', 'shape': 'sphere', 'mass': 350, 'volume': 120},
    {'name': 'mango', 'shape': 'square', 'mass': 150, 'volume': 120},
    {'name': 'lemon', 'shape': 'sphere', 'mass': 300, 'volume': 100},
    {'name': 'apple', 'shape': 'sphere', 'mass': 500, 'volume': 250}))

print(GoodFrts)
