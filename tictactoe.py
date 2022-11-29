import random

class TicTacToe:
    def __init__(self) -> None:
        self.board = []
        self.human_player = ''
        self.comp_player = ''
        self.current_player = ''
        self.won = False

    def create_board(self) -> None:
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)


    def print_board(self) -> None:
        print()
        for row in self.board:
            for space in row:
                print(space, end = ' ')
            print()

    def introduce_game(self) -> None:
        print()
        print('Welcome to Tic Tac Toe!')
        print()
        self.print_board()
        print()
        self.choose_player()
        print('You are player', self.human_player)
        print('The computer is player', self.comp_player)
        print()
        if self.human_player == 'X':
            print('The human player goes first...')
        else: 
            print('The computer player goes first...')
        print()

    def choose_player(self) -> None:
        player = random.randint(0,1)
        if player == 0:
            self.human_player = 'X'
            self.comp_player = 'O'
            self.current_player = 'human'
        else:
            self.human_player = 'O'
            self.comp_player = 'X'
            self.current_player = 'computer'

    def validate_choice(self, x, y) -> bool:
        # is x and y is not within bounds, return false
        if x < 0 or x > 2 or y < 0 or y > 2:
            return False
        # if the spot is already taken, return false
        if self.board[x][y] != '-':
            return False
        return True
  

    def generate_comp_choice(self) -> int:
        output = []
        x = random.randint(1,3)
        y = random.randint(1,3)
        output.append(x)
        output.append(y)
        return output

    def end_game(self) -> None:
        if self.won == True:
            print('Player ', self.current_player, ' has won!')  
        else:
            print('Nobody won this round!')
        answer = input('Want to play again? (Y or N) ')
        if answer == 'Y' or answer == 'y':
            self.board = []
            self.human_player = ''
            self.comp_player = ''
            self.current_player = ''
            self.won = False
            self.play_game()
        else:
            return

    def check_row(self, symbol):
        for i in range(3):
            if (self.board[i][0]  == symbol 
                  and self.board[i][1] == symbol 
                  and self.board[i][2] == symbol):
                return True
        return False
          

    def check_column(self, symbol):
        for i in range(3):
          if (self.board[0][i]  == symbol 
                  and self.board[1][i] == symbol 
                  and self.board[2][i] == symbol):
                return True
        return False


    def check_diagonal(self, symbol):
        if ((self.board[0][0] == symbol 
                and self.board[1][1] == symbol
                and self.board[2][2] == symbol) or 
              (self.board[2][0] == symbol 
                and self.board[1][1] == symbol
                and self.board[0][2] == symbol)):
            return True
        return False

    def player_has_won(self) -> bool:
        current_player = self.current_player
        if current_player == 'human':
            symbol = self.human_player
        else:
            symbol = self.comp_player

        b = self.board 

        # if first row is the symbol
        if self.check_row(symbol) or self.check_column(symbol) or self.check_diagonal(symbol):
            self.won = True
            return True
        return False

    def is_full(self) -> bool:
        for row in self.board:
            for space in row:
                if space == '-':
                    return False
        return True 


    def switch_players(self) -> None:
        if self.current_player == 'computer':
            self.current_player = 'human'
        elif self.current_player == 'human':
            self.current_player = 'computer'

    def take_turn(self):
        print('It is the', self.current_player, 'player\'s turn!\n')
        if self.current_player == 'computer':
            found = False
            while not found:
              [x, y] = self.generate_comp_choice()
              if self.validate_choice(x-1, y-1):
                  self.board[x-1][y-1] = self.comp_player
                  found = True
        if self.current_player == 'human':
            found = False
            while not found:
                x = int(input('Which row do you choose? '))
                y = int(input('Which column do you choose? '))
                if not self.validate_choice(x-1, y-1):
                    print()
                    print('Sorry this is not a valid spot. Choose a space on the board that isn\'t taken yet.')
                    print()
                else:
                    self.board[x-1][y-1] = self.human_player
                    found = True
        self.print_board()
        print()     
        

    def play_game(self):
        self.create_board()

        self.introduce_game()

        while True:
          self.take_turn()

          if self.player_has_won() or self.is_full():
              self.end_game()
              return False
        
          self.switch_players()


game = TicTacToe()

game.play_game()


          