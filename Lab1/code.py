"""
Command Usage:
python main.py --Q <game_number>

Replace <game_number> with the number of the game you want to simulate (1-9).

Example:
python main.py --Q 5

Output:
The output will be stored in Q<game_number>.txt
"""
import numpy as np
from tqdm import tqdm
from argparse import ArgumentParser

def get_game_matrix(args):
    Q = args.Q
    if Q == 1:
        return np.array([[[-1, -1], [1, 0]],
                        [[0, 1], [3, 3]]])
    elif Q == 2:
        return np.array([[[2, 2], [1, 0]],
                        [[0, 1], [3, 3]]])
    elif Q == 3:
        return np.array([[[1, 1], [0, 0]],
                        [[0, 0], [0, 0]]])
    elif Q == 4:
        return np.array([[[0, 1], [2, 0]],
                        [[2, 0], [0, 4]]])
    elif Q == 5:
        return np.array([[[0, 1], [1, 0]],
                        [[1, 0], [0, 1]]])
    elif Q == 6:
        return np.array([[[10, 10], [0, 0]],
                        [[0, 0], [10, 10]]])
    elif Q == 7:
        return np.array([[[0, 0], [1, 1]],
                        [[1, 1], [0, 0]]])
    elif Q == 8:
        return np.array([[[3, 2], [0, 0]],
                        [[0, 0], [2, 3]]])
    elif Q == 9:
        return np.array([[[3, 3], [0, 2]],
                        [[2, 0], [1, 1]]])
    else:
        raise ValueError("Q should be 1~9")

def run(game_matrix):
    n, m = game_matrix.shape[0], game_matrix.shape[1]
    belif1, belif2, _p, _q = [], [], [], []
    
    # 5000 trials
    progress = tqdm(range(5000))
    for _ in progress:
        # sample p, q from uniform distribution(0, 100)
        p, q = np.random.random(2) * 100
        # store the init p and q
        _p.append(p)
        _q.append(q)
        
        # p2's belief of p1's action
        cnt1 = np.array([p, 100 - p])
        # p1's belief of p2's action
        cnt2 = np.array([q, 100 - q])
        
        # 1000 rounds
        for i in range(1000):
            # calculate  payoff
            payoff1, payoff2 = np.zeros((2, n))
            for action_1 in range(n):
                for action_2 in range(m):
                    payoff1[action_1] += cnt2[action_2] * game_matrix[action_1][action_2][0] 
                    payoff2[action_2] += cnt1[action_1] * game_matrix[action_1][action_2][1]
            # choose the idx of max expected payoff
            # if there are multiple max, choose one randomly
            # update the belief
            idx_1 = np.argwhere(payoff1 == np.max(payoff1)).flatten()
            idx_1 = np.random.choice(idx_1, 1)
            idx_2 = np.argwhere(payoff2 == np.max(payoff2)).flatten()
            idx_2 = np.random.choice(idx_2, 1)
            cnt1[idx_1] += 1
            cnt2[idx_2] += 1
        
        # store the belief of p1 and p2
        belif1.append(cnt2 - np.array([q, 100 - q]))
        belif2.append(cnt1 - np.array([p, 100 - p]))
        
    belif1 = np.array(belif1)
    belif2 = np.array(belif2)
    with open(f'Q{args.Q}.txt', 'w') as f:
        for (p, q, i, j) in zip(_p, _q, belif1, belif2):
            f.write(f"init p: {p:.3f}, q:{q:.3f}, {i / np.sum(i)}, {j / np.sum(j)}\n")
        f.write(f"p1\'s belief mean: {belif1.mean(axis=0)}, p2 belief mean\'s: {belif2.mean(axis=0)}\n")
        f.write(f"p1\'s belief std: {belif1.std(axis=0)}, p2 belief std\'s: {belif2.std(axis=0)}\n")

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--Q", type=int, default=1, help="Q1~Q9, default: Q1")
    args = parser.parse_args()
    np.set_printoptions(suppress=True, precision=3)
    
    # get game matrix
    game_matrix = get_game_matrix(args)
    # run the game
    run(game_matrix)