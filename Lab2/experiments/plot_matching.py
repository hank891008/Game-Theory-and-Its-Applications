import matplotlib.pyplot as plt

matching1 = [13.437, 13.234, 13.163, 13.08, 13.044]
matching1_std = [0.668, 0.718, 0.754, 0.791, 0.832]
matching2 = [13.42, 13.931, 14.085, 14.133, 14.157]
matching2_std = [0.663, 0.615, 0.562, 0.558, 0.571]
maximum = [15, 15, 15, 15, 15]
maximum_std = [0, 0, 0, 0, 0]

y = [0.0, 0.2, 0.4, 0.6, 0.8]
plt.ylim(12, 15.5)
plt.plot(y, matching1, label='non_heuristic_Matching', color='blue', linestyle='-', marker='o')
plt.plot(y, matching2, label='heuristic_Matching', color='green', linestyle='-', marker='o')
plt.plot(y, maximum, label='Optimum', color='red', linestyle='-', marker='o')
plt.xlabel('Link Rewiring Probability')
plt.ylabel('Candinality of Matching')
plt.legend()
plt.savefig("matching.png")