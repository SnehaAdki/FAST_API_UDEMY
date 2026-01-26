# https://www.youtube.com/watch?v=zRz1GPSH50I&list=PLJN9ydlFnJsiEgyjO3D3yBhtiENymhF8G

class Position():
    def __init__(self):
        self.start_position = 0
        self.end_position = 0

    def set_start_end_pos(self):
        print("Enter start position:")
        self.start_position = int(input())
        print("Enter end position:")
        self.end_position = int(input())
