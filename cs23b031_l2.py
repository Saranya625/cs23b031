import numpy as np
import plotext as pt

np.random.seed(31)

n = 10
p = np.arange(0.1, 1.1, 0.1)
samples = 1000

empirical_probability = []
analytical_probability = []

for pr in p:
    success = 0
    analytical = 1 - (1 - pr) ** n
    analytical_probability.append(analytical)

    for i in range(samples):
        nodes = np.random.rand(n) < pr
        if np.any(nodes):
            success += 1

    empirical = success / samples
    empirical_probability.append(empirical)


