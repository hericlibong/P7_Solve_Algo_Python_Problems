import csv
from itertools import combinations

# Fonction pour lire les données des actions depuis un fichier CSV
def read_actions(filename):
    actions = []
    with open(filename, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            action = {
                'name': row['Action'],
                'cost': float(row['Cost']),
                'profit': float(row['Profit'])
            }
            actions.append(action)
    return actions

# Fonction pour calculer le profit total d'une combinaison d'actions
def calculate_total_profit(combination):
    return sum(action['cost'] * action['profit'] / 100 for action in combination)

# Fonction pour calculer le coût total d'une combinaison d'actions
def calculate_total_cost(combination):
    return sum(action['cost'] for action in combination)

# Fonction pour trouver la meilleure combinaison d'actions
def find_best_combination(actions, budget):
    best_combination = []
    best_profit = 0

    for r in range(1, len(actions) + 1):
        for combination in combinations(actions, r):
            total_cost = calculate_total_cost(combination)
            if total_cost <= budget:
                total_profit = calculate_total_profit(combination)
                if total_profit > best_profit:
                    best_profit = total_profit
                    best_combination = combination

    return best_combination, best_profit

# Lecture des données des actions
actions = read_actions('Action.csv')

# Définition du budget maximum
budget = 500

# Recherche de la meilleure combinaison d'actions
best_combination, best_profit = find_best_combination(actions, budget)

# Affichage du résultat
print("Meilleure combinaison d'actions:")
for action in best_combination:
    print(f"{action['name']} (Coût: {action['cost']}€, Profit: {action['profit']}%)")
print(f"Profit total: {best_profit}€")
