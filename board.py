class Board:
    def __init__(self, width, height) -> None:
        self.board = []
        self.width = width
        self.height = height

    def create_board(self) -> None:
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append('-')
            self.board.append(row)

    def print_board(self) -> None:
        print()
        for row in self.board:
            for space in row:
                print(space, end = ' ')
            print()
        print()

    def is_full(self) -> bool:
        for row in self.board:
            for space in row:
                if space == '-':
                    return False
        return True 


    
