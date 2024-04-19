import sys
from mis import mis_based_ids_model
from sym_mds import symmetric_mds_based_ids_model
from matching import matching_model
        
def solve(algo, n, connects, tirals=100):
    results = []
    for _ in range(tirals):
        solver = algo(n, connects)
        move, state = solver.solve()
        results.append(state)
    return results

def main():
    lines = sys.argv
    n, connects = lines[1], lines[2:]
    
    print("Requirement 1-1:")
    results = solve(mis_based_ids_model, n, connects)
    print(f"the cardinality of MIS-based IDS Game is {min(results)}")
    
    print("Requirement 1-2:")
    results = solve(symmetric_mds_based_ids_model, n, connects)
    print(f"the cardinality of Symmetric MDS-based IDS Game is {min(results)}")
    
    
    print("Requirement 2:")
    results = solve(matching_model, n, connects)
    print(f"the cardinality of Matching Game is {max(results)}")

if __name__ == '__main__':
    main()