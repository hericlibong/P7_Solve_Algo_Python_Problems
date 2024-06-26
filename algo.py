import csv
from itertools import combinations


import csv

def read_actions(filename):
    """
    Lit les données des actions à partir d'un fichier CSV et les stocke dans une liste de dictionnaires.

    Args:
        filename (str): Le chemin du fichier CSV contenant les données des actions.

    Returns:
        list: Une liste de dictionnaires, où chaque dictionnaire contient les informations d'une action,
              incluant le nom, le coût et le profit en pourcentage.

    Raises:
        FileNotFoundError: Si le fichier spécifié n'est pas trouvé.
        Exception: Pour les erreurs liées à la lecture du fichier ou au parsing des données.
    """
    actions = []
    try:
        with open(filename, mode='r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                action = {
                    'name': row['Action'],
                    'cost': float(row['Cost']),
                    'profit': float(row['Profit'])
                }
                actions.append(action)
    except FileNotFoundError:
        raise FileNotFoundError("Le fichier spécifié n'a pas été trouvé.")
    except Exception as e:
        raise Exception(f"Erreur lors de la lecture du fichier: {e}")
    return actions

def calculate_profit(cost, percentage):
    """
    Calcule le profit en euros basé sur le coût initial de l'action et le pourcentage de profit.

    Args:
        cost (float): Le coût initial de l'action.
        percentage (float): Le pourcentage de profit attendu après deux ans.

    Returns:
        float: Le profit en euros calculé.
    """
    return cost * (percentage / 100)

# Chargement des actions à partir du fichier CSV
actions = read_actions("Action.csv")

# Initialisation des variables pour garder la trace de la meilleure combinaison et du profit maximum
best_combination = None
max_profit = 0

# Création et évaluation de toutes les combinaisons possibles d'actions respectant le budget de 500 euros
for i in range(1, len(actions)+1):
    for combination in combinations(actions, i):
        total_cost = sum(action['cost'] for action in combination)
        if total_cost <= 500:
            total_profit = sum(calculate_profit(action['cost'], action['profit']) for action in combination)
            if total_profit > max_profit:
                max_profit = total_profit
                best_combination = combination

# Affichage des résultats
if best_combination:
    print("Best combination to buy:")
    for action in best_combination:
        print(f"{action['name']}: Cost = {action['cost']}, Profit = {calculate_profit(action['cost'], action['profit'])} euros")
    print(f"Total profit: {max_profit} euros")
else:
    print("No valid combination found within the budget.")
