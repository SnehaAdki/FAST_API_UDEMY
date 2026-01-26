from position import Position 

class Board():
    def __init__(self):
        self.num_of_ladders = 0
        self.num_of_snakes = 0
        self.snakes = {}
        self.ladders = {}
        self.size_baord = 0

    def configure_board(self):
        print("Configuring the board")
        print("Enter board size")
        self.size_baord = int(input())
        print("Enter number of snakes")
        self.num_of_snakes = int(input())
        print("Enter number of ladders")
        self.num_of_ladders = int(input())
        self.create_snakes()
        self.create_ladders()
        self.show_board_details()

    def show_board_details(self):
        print("Board Configuration")
        print(f"Board Size {self.size_baord}")
        print(f"Number of Snakes  {self.num_of_snakes}")
        print(f"Number of Ladders  {self.num_of_ladders}")
        print(f"Snakes Details are {self.snakes}")
        print(f"Ladder Details are {self.ladders}")


    def create_snakes(self):
        print("Create the snake Board ")
        for i in range(1,self.num_of_snakes+1):
            p1 = Position()
            print(f"{i} snake" )
            p1.set_start_end_pos()
            self.snakes[p1.start_position] = p1.end_position
        
        
    def create_ladders(self):
        print("Create the Ladder Board ")
        for i in range(1,self.num_of_ladders+1):
            p1 = Position()
            print(f"{i} ladder" )
            p1.set_start_end_pos()
            self.ladders[p1.start_position] = p1.end_position



