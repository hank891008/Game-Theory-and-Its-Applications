from base_model import base_model

class mis_based_ids_model(base_model):
    def __init__(self, n, connects):
        super().__init__(n, connects)
        self.alpha = 1.5
        
    def utility(self, player):
        if self.state[player] == 0:
            return 0
        
        u = 1
        for other in self.G[player]:
            if self.deg[player] <= self.deg[other]:
                u -= self.alpha * self.state[other]
        return u
    
    def best_response(self, player):
        for other in self.G[player]:
            if self.state[other] == 1 and self.deg[player] <= self.deg[other]:
                return 0
        return 1
    