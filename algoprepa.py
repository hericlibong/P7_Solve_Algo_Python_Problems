from itertools import combinations

# Données des actions
actions = [
    ("Action-1", 20, 5), ("Action-2", 30, 10), ("Action-3", 50, 15),
    ("Action-4", 70, 20), ("Action-5", 60, 17), ("Action-6", 80, 25),
    ("Action-7", 22, 7), ("Action-8", 26, 11), ("Action-9", 48, 13),
    ("Action-10", 34, 27), ("Action-11", 42, 17), ("Action-12", 110, 9),
    ("Action-13", 38, 23), ("Action-14", 14, 1), ("Action-15", 18, 3),
    ("Action-16", 8, 8), ("Action-17", 4, 12), ("Action-18", 10, 14),
    ("Action-19", 24, 21), ("Action-20", 114, 18)
]

def calculate_profit(cost, percentage):
    return cost * (percentage / 100)

# Création de toutes les combinaisons possibles respectant le budget de 500 euros
best_combination = None
max_profit = 0

for i in range(1, len(actions)+1):
    for combination in combinations(actions, i):
        total_cost = sum(action[1] for action in combination)
        if total_cost <= 500:
            total_profit = sum(calculate_profit(action[1], action[2]) for action in combination)
            if total_profit > max_profit:
                max_profit = total_profit
                best_combination = combination

# Affichage de la meilleure combinaison d'actions à acheter et du profit total
if best_combination:
    print("Best combination to buy:")
    for action in best_combination:
        print(f"{action[0]}: Cost = {action[1]}, Profit = {calculate_profit(action[1], action[2])} euros")
    print(f"Total profit: {max_profit} euros")
else:
    print("No valid combination found within the budget.")
