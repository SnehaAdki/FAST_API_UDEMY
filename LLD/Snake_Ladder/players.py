class Player:
    def __init__(self):
        self.id = 0
        self.name = None
        self.curr_pos = 0

    def set_players(self):
        print("Player ID:")
        self.id = int(input())
        print("Player name:")
        self.name = input()
        return self

    def get_players(self , player):
        print(f"{player.id} {player.name} {player.curr_pos}")
