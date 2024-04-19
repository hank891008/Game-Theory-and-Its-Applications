import networkx as nx
from networkx.algorithms import approximation
import matplotlib.pyplot as plt
a = [0.0, 0.2, 0.4, 0.6, 0.8]
for p in a:
    n, k = 30, 4
    ws_model = nx.watts_strogatz_graph(n, k, p)
    # nx.draw(ws_model, with_labels=True)
    # plt.savefig(f"ws_model_{p}.png")
    # print("maximum_independent_set:", len(approximation.maximum_independent_set(ws_model)))
    # print(approximation.maximum_independent_set(ws_model))
    # print("min_edge_dominating_set:", len(approximation.min_edge_dominating_set(ws_model)))
    # print(approximation.min_edge_dominating_set(ws_model))
    # print("maximum_matching:", len(nx.max_weight_matching(ws_model)))
    # print(nx.max_weight_matching(ws_model))
    print(n, end=' ')
    for i in range(n):
        for j in range(n):
            if ws_model.has_edge(i, j):
                print(1, end='')
            else:
                print(0, end='')
        print(' ', end='')
    print()