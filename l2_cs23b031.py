import random
import plotext as plt
n = 10
trials = 100000
p_values = [i / 10 for i in range(1, 11)]   

empirical_probs = []
analytical_probs = []

for p in p_values:
    success = 0
    for _ in range(trials):
        nodes = [random.random() < p for _ in range(n)]
        if any(nodes):
            success += 1

    empirical = success / trials
    analytical = 1 - (1 - p) ** n
    empirical_probs.append(empirical)
    analytical_probs.append(analytical)
