import random
import plotext as plt
random.seed(47)
n = 10
trials = 100000
p_values = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]   

empirical_probs = []
analytical_probs = []
for p in p_values:
    success = 0
    for _ in range(trials):
        nodes = [random.random() <  p for _ in range(n)]
        if sum(nodes)==1:
            success += 1

    empirical = success / trials
    analytical = n*p*((1 - p) ** (n-1))

    empirical_probs.append(empirical)
    analytical_probs.append(analytical)
with open("l2_cs23b031.txt", "w") as f:
    f.write("p\tEmpirical\tAnalytical\n")
    for i in range(len(p_values)):
        f.write(f"{p_values[i]:.1f}\t{empirical_probs[i]:.6f}\t{analytical_probs[i]:.6f}\n")

print("\nData saved to l2_fullrollnumber.txt")
plt.clf()

plt.title("Bernoulli Network Success Probability")
plt.xlabel("Participation probability p")
plt.ylabel("System success probability")
	
plt.plot(p_values, analytical_probs, label="Analytical",marker="dot")
plt.plot(p_values, empirical_probs, label="Empirical")
plt.show()
plt.save_fig("cs23b031.txt")
