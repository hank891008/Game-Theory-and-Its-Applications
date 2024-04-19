import numpy as np
from base_model import base_model

class matching_model(base_model):
    def __init__(self, n, connects, heuristic=True):
        super().__init__(n, connects)
        self.state = self.init_state()
        self.prefer_table = self.init_prefer_table(heuristic)
        self.G = self.add_self_loop(self.G)
        self.beta = 0.5
    
    def add_self_loop(self, G):
        for i in range(self.n):
            self.G[i].append(i)
            self.G[i] = sorted(self.G[i])
        return G
            
    def init_state(self):
        state = np.zeros(self.n, dtype=np.int_)
        for i in range(self.n):
            state[i] = np.random.choice(self.G[i])
        return state
    
    def init_prefer_table(self, heuristic):
        prefer_table = np.zeros((self.n, self.n), dtype=np.int_)
        for i in range(self.n):
            for j in range(self.n):
                if i == j:
                    prefer_table[i][j] = 0
                elif j in self.G[i]:
                    if heuristic == True:
                        prefer_table[i][j] = self.n - self.deg[j]
                    else:
                        prefer_table[i][j] = 1
        return prefer_table
    
    def utility(self, player):
        if self.state[player] == player:
            return 0
        else:
            u = 0
            chosen = self.state[player]
            prefer_rank = self.prefer_table[player][chosen]
            can_link = self.state[chosen] == player 
            can_link |= self.state[chosen] == chosen
            u = prefer_rank * can_link - self.beta
        return u
                
            
    
    def best_response(self, player):
        origin_state = self.state[player]
        return_state = self.state[player]
        max_state_utility = self.utility(player)
        others = self.G[player]
        for other in others:
            self.state[player] = other
            other_state_utility = self.utility(player)
            if other_state_utility > max_state_utility:
                return_state = other
                max_state_utility = other_state_utility
        self.state[player] = origin_state
        return return_state
    
    def make_pair(self):
        matching = []
        for i in range(self.n):
            for other in self.G[i]:
                if i < other and self.state[i] == other and self.state[other] == i:
                    matching.append((i, other))
        return len(matching)
    
    def solve(self):
        move_count = 0
        while True:
            can_improve = self.reach_NE()
            if can_improve == []:
                break
            player = np.random.choice(can_improve)
            self.state[player] = self.best_response(player)
            move_count += 1
        return move_count, self.make_pair()
