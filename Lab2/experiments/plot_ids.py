import matplotlib.pyplot as plt

mis = [8.207, 8.5, 8.85, 8.996, 9.075]
mis_std = [0.6230176562506075, 0.8831760866327847, 1.0753604047016052, 1.1045288588352953, 1.1319783566835542]
sym_mds = [8.191, 9.491, 10.254, 10.688, 10.785]
sym_mds_std = [0.6360180815039774, 0.9591240795642657, 1.0906346776074929, 1.1647557683909533, 1.210278893478689]

y = [0.0, 0.2, 0.4, 0.6, 0.8]
plt.ylim(7, 12)
plt.plot(y, mis, label='MIS-based IDS Game', color='blue', linestyle='-', marker='o')
plt.plot(y, sym_mds, label='Symmetric MDS-based IDS Game', color='red', linestyle='-', marker='o')
plt.xlabel('Link Rewiring Probability')
plt.ylabel('Candinality of IDS')
plt.legend()
plt.savefig("result.png")