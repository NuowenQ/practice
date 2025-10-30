class Tournament:
    competition_history = [] # Ordered competition history
    player_information = {} # Key: username, value: user

    def register_player(self, username, real_name): 
        if username in self.player_information: 
            print("you have already registered")

        else: 
            self.player_information[username] = User(username, real_name, 1000)
            print("registered successfully")
    
    def record_match(self, player1_username, player2_username, winner_username): 
        if player1_username in self.player_information and player2_username in self.player_information: 
            self.competition_history.append((player1_username, player2_username, winner_username))

            if (winner_username == player1_username): 
                self.player_information[player1_username].won(25, player2_username)
                self.player_information[player2_username].loss(25, player1_username)
            else: 
                self.player_information[player2_username].won(25, player1_username)
                self.player_information[player1_username].loss(25, player2_username)
            
        elif player1_username not in self.player_information: 
            print("INVALID INPUT: player1 doesn't exist")

        elif player2_username not in self.player_information: 
            print("INVALID INPUT: player1 doesn't exist")
    
    def get_head_to_head(self, player1_username, player2_username): 
        return (
            self.player_information[player1_username].won_record(player2_username),
            self.player_information[player2_username].won_record(player1_username) 
            )

class User: 
    # Key: username, value: number of wining / lossing
    history = {} # (win, loss)

    def __init__(self, username, real_name, rating_points): 
        self.username = username
        self.real_name = real_name 
        self.rating_points = rating_points
    
    def won(self, points, player): 
        self.rating_points += points

        if player in self.history: 
            self.history[player][0] += 1
        else: 
            self.history[player] = (1, 0)
        
    def loss(self, points, player): 
        self.rating_points -= points

        if player in self.history: 
            self.history[player][1] += 1
        else: 
            self.history[player] = (0, 1)
    
    def won_record(self, player): 
        if player not in self.history: 
            return 0
        else: 
            return self.history[player][0]
    
    def loss_record(self, player): 
        if player not in self.history: 
            return 0
        else: 
            return self.history[player][1]

if __name__ == "__main__": 
    t = Tournament()
    t.register_player("u1", "chenxiao")
    t.register_player("u2", "keming")
    t.record_match("u1", "u2", "u1")
    print(t.get_head_to_head("u1", "u2"))
