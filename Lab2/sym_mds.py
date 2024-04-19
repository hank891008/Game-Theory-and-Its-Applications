from base_model import base_model

class symmetric_mds_based_ids_model(base_model):
    def __init__(self, n, connects):
        super().__init__(n, connects)
        self.alpha = 1.5
        self.beta = 0.5
        self.gamma = self.n * self.alpha + 1
    
    def gain(self, player):
        v = self.state[player]
        for other in self.G[player]:
            v += self.state[other]
        if v == 1:
            return self.alpha
        return 0

    # gain of dominance
    def total_gain(self, player):
        g = self.gain(player)
        for other in self.G[player]:
            g += self.gain(other)
        return g
    
    # penalty of violating independence
    def penalty(self, player):
        w = 0
        for other in self.G[player]:
            w += self.state[player] * self.state[other] * self.gamma
        return w
    
    def utility(self, player):
        if self.state[player] == 0:
            return 0
        return self.total_gain(player) - self.beta - self.penalty(player)
    
    def best_response(self, player):
        orginal_state = self.state[player]
        orginal_state_utility = self.utility(player)
        other_state = 1 - orginal_state
        self.state[player] = other_state
        other_state_utility = self.utility(player)
        self.state[player] = orginal_state
        if other_state_utility > orginal_state_utility:
            return other_state
        return orginal_state
        

    