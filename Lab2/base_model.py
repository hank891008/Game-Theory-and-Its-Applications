import numpy as np
from abc import ABC, abstractmethod

class base_model(ABC):
    def __init__(self, n, connects):
        self.n = int(n)
        self.G = self.init_connection(connects)
        self.state = self.init_state()
        self.deg = self.init_deg()
    
    def init_connection(self, connects):
        G = [[] for _ in range(self.n)]
        for i in range(self.n):
            for j in range(len(connects[i])):
                if connects[i][j] == '1':
                    G[i].append(j)
        return G
    
    def init_deg(self):
        deg = np.zeros(self.n, dtype=np.int_)
        for i in range(self.n):
            deg[i] = len(self.G[i])
        return deg
    
    def init_state(self):
        state = np.zeros(self.n, dtype=np.bool_)
        for i in range(self.n):
            state[i] = np.random.randint(0, 2)
        return state
    
    @abstractmethod
    def utility(self, player):
        pass
    
    @abstractmethod
    def best_response(self, player):
        pass
    
    def reach_NE(self):
        can_improve = []
        for i in range(self.n):
            if self.state[i] != self.best_response(i):
                can_improve.append(i)
        return can_improve

    def solve(self):
        move_count = 0
        while True:
            can_improve = self.reach_NE()
            if can_improve == []:
                break
            player = np.random.choice(can_improve)
            self.state[player] = self.best_response(player)
            move_count += 1
        return move_count, np.sum(self.state)