def knapsack(actions, max_budget):
    n = len(actions)
    # Créer un tableau pour stocker les résultats des sous-problèmes
    dp = [[0 for x in range(max_budget + 1)] for y in range(n + 1)]

    # Remplir le tableau dp de bas en haut
    for i in range(1, n + 1):
        for w in range(1, max_budget + 1):
            cost = actions[i-1][1]
            profit = actions[i-1][1] * (actions[i-1][2] / 100.0)
            if cost <= w:
                dp[i][w] = max(profit + dp[i-1][w-cost], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][max_budget]

# Données des actions: (Nom, Coût, Profit en %)
actions = [
    ("Action-1", 20, 5), ("Action-2", 30, 10), ("Action-3", 50, 15),
    ("Action-4", 70, 20), ("Action-5", 60, 17), ("Action-6", 80, 25),
    ("Action-7", 22, 7), ("Action-8", 26, 11), ("Action-9", 48, 13),
    ("Action-10", 34, 27), ("Action-11", 42, 17), ("Action-12", 110, 9),
    ("Action-13", 38, 23), ("Action-14", 14, 1), ("Action-15", 18, 3),
    ("Action-16", 8, 8), ("Action-17", 4, 12), ("Action-18", 10, 14),
    ("Action-19", 24, 21), ("Action-20", 114, 18)
]

max_budget = 500
max_profit = knapsack(actions, max_budget)
print(f"Le profit maximum possible est de {max_profit} euros")
