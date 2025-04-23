ebruary_shopping_list = {
    1: ['meat', 'chicken', 'chicken', 'chicken', 'bread', 'chocolate', 'meat'],
    2: ['bread', 'milks', 'butter', 'butter', 'chocolate'],
    3: ['butter', 'meat', 'milks'],
    4: ['butter', 'bread', 'nuts'],
    5: ['butter', 'bread', 'chocolate', 'chocolate'],
    6: ['nuts', 'butter', 'butter', 'butter', 'chocolate', 'butter'],
    7: ['cheese', 'milks', 'butter', 'nuts'],
    8: ['cheese', 'meat', 'nuts', 'yoghurt', 'cheese'],
    9: ['chocolate', 'milks', 'milks', 'chocolate', 'milks', 'eggs', 'meat'],
    10: ['yoghurt', 'butter', 'chocolate', 'cheese', 'butter'],
    11: ['cheese', 'meat', 'yoghurt'],
    12: ['eggs', 'chocolate', 'meat', 'eggs', 'butter'],
    13: ['bread', 'eggs', 'yoghurt', 'yoghurt', 'chicken', 'chocolate'],
    14: ['milks', 'meat', 'meat'],
    15: ['meat', 'chicken', 'butter', 'nuts', 'nuts'],
    16: ['meat', 'meat', 'chicken']
}

items_prices = {
    'meat': 250,
    'chicken': 140,
    'bread': 10,
    'chocolate': 20,
    'milks': 42,
    'butter': 75,
    'nuts': 90,
    'cheese': 65,
    'yoghurt': 25,
    'eggs': 120
}

# Step 1: Count the items
items_count = {}
for items in february_shopping_list.values():
    for item in items:
        items_count.setdefault(item, 0)
        items_count[item] += 1

# Optional: Print item counts
print("=== Item Count ===")
for item, count in items_count.items():
    print(f"{item}: {count} times")

# Step 2: Calculate total cost per item
items_cost = {}
for item, count in items_count.items():
    price = items_prices.get(item, 0)
    items_cost[item] = price * count

# Step 3: Print individual total costs
print("\n=== Total Cost per Item ===")
for item, cost in items_cost.items():
    print(f"{item.title()} total cost: {cost} EGP")

# Step 4: Grand total
grand_total = sum(items_cost.values())
print(f"\n🧾 Total shopping cost for February: {grand_total} EGP")
