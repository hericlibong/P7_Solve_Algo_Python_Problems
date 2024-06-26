import pandas as pd

def load_actions(filename):
    return pd.read_csv(filename)

def greedy_investment(actions, max_budget):
    # Trier les actions par ratio profit/coût décroissant
    actions['ratio'] = actions['Profit'] / actions['Cost']
    actions_sorted = actions.sort_values(by='ratio', ascending=False)

    total_profit = 0
    current_budget = 0
    selected_actions = []

    for _, action in actions_sorted.iterrows():
        if current_budget + action['Cost'] <= max_budget:
            current_budget += action['Cost']
            total_profit += action['Cost'] * (action['Profit'] / 100)
            selected_actions.append(action['Action'])

    return selected_actions, total_profit

# Exemple d'utilisation
actions = load_actions("Action.csv")
# print(actions)
selected_actions, profit = greedy_investment(actions, 500)
print(f"Selected actions: {selected_actions}")
print(f"Total Profit: {profit}")
