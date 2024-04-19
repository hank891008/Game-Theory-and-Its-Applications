import sys
import numpy as np
import networkx as nx
from mis import mis_based_ids_model
from sym_mds import symmetric_mds_based_ids_model
from matching import matching_model

def solve(algo, tirals=1000):
    n = 30
    states = []
    for _ in range(tirals):
        ws_model = nx.watts_strogatz_graph(n, 4, 0.0)
        connects = []
        for i in range(n):
            st = ''
            for j in range(n):
                if ws_model.has_edge(i, j):
                    st += '1'
                else:
                    st += '0'
            connects.append(st)
        solver = algo(n, connects)
        move, state = solver.solve()
        states.append(state)
    return states

def solve_matching(algo, tirals=1000):
    n = 30
    s1, s2 = [], []
    maximum = []
    for _ in range(tirals):
        ws_model = nx.watts_strogatz_graph(n, 4, 0.8)
        maximum.append(len(nx.max_weight_matching(ws_model)))
        connects = []
        for i in range(n):
            st = ''
            for j in range(n):
                if ws_model.has_edge(i, j):
                    st += '1'
                else:
                    st += '0'
            connects.append(st)
        solver = algo(n, connects, heuristic=False)
        move, state = solver.solve()
        s1.append(state)
        solver = algo(n, connects, heuristic=True)
        move, state = solver.solve()
        s2.append(state)
    return s1, s2, maximum
if __name__ == '__main__':
    print("Requirement 1-1:")
    results = solve(mis_based_ids_model)
    print(np.mean(results), np.std(results))
    
    print("Requirement 1-2:")
    results = solve(symmetric_mds_based_ids_model)
    print(np.mean(results), np.std(results))
    
    print("Requirement 2:")
    s1, s2, m = solve_matching(matching_model)
    print(np.mean(s1), np.std(s1))
    print(np.mean(s2), np.std(s2))
    print(np.mean(m), np.std(m))