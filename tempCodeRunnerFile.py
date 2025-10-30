     self.win_history[player] += 1
        else: 
            self.win_history[player] = 1 
        
    def loss(self, points, player): 
        self.rating_points -= points
        if player in self.loss_history: 
            self.loss_history[player] += 1
        else: 
            self.loss_history[player] = 1 
    
    def won_record(self, player): 
        if player not in win_history: 
            return 0
        else: 
            return self.win_history[player]
    
    def loss_record(self, player): 
        if player not in loss_history: 
            return 0
        else: 
            return self.loss_history[player]
