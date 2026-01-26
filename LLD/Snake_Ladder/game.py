
from configure import Board
from players import Player
from dice import Dice


class Game():
    def __init__(self):
        self.players = []
        self.number_players = 0
        self.dice = Dice(0)
        self.snake_ladder_board = Board()


    def generate_players(self):
        print("Enter number of players:")
        self.number_players = int(input())

        for i in range(0,self.number_players):
            self.players.append(Player().set_players())

    def get_players(self):
        for i in range(0,self.number_players):
            Player().get_players(self.players[i])
    
    def generate_dice(self):
        print("Enter number of Dices:")
        self.dice = Dice(int(input()))

    def board_configurations_are(self):
        print("Board Configurations are....")
        print("--------------------------------------")
        self.snake_ladder_board.show_board_details()
        print(self.dice.number)
        self.get_players()

    def configure_baord_seting(self):
        self.snake_ladder_board.configure_board()
        self.generate_players()
        self.generate_dice()
        self.board_configurations_are()


    def start_game(self):
        i = 0
        curr_player = self.players.pop(0)
        while(curr_player.curr_pos != self.snake_ladder_board.size_baord):
            # curr_pos + dice_roll 
            print(f"current Turn {curr_player.name}")
            print(f"current Turn {curr_player.curr_pos}")
            dice_number = curr_player.curr_pos + self.dice.roll()
            print(f"Dice number {dice_number}")       
            if dice_number in self.snake_ladder_board.snakes.keys():
                # snake scenariso
                curr_player.curr_pos = self.snake_ladder_board.snakes[dice_number]
            elif dice_number in self.snake_ladder_board.ladders.keys():
                # ladder scenariso
                curr_player.curr_pos = self.snake_ladder_board.ladders[dice_number]
            elif dice_number == self.snake_ladder_board.size_baord:
                #print(f"{curr_player.name} Won the game")
                break
            elif dice_number > self.snake_ladder_board.size_baord:
                # rolled is greater thean size
                # no change
                curr_player.curr_pos = curr_player.curr_pos
            else:
                # valid just inc
                curr_player.curr_pos = dice_number
            self.players.append(curr_player)
            curr_player = self.players.pop(0)
        print(f"{curr_player.name} Won the game")

g1 = Game()
g1.configure_baord_seting()
g1.start_game()