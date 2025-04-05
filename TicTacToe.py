class TicTacToe:
    def __init__(self) -> None:
        self.board = [" " for _ in range(9)]
        self.human = "O"
        self.ai = "X"

    def print_board(self) -> None:
        for i in range(0, 9, 3):
            print(f"{self.board[i]} | {self.board[i +1]} | {self.board[i + 2]}")
            if i < 6:
                print("----------")

    def available_moves(self):
       return [i for i, spot in enumerate(self.board) if spot == " "]

    def make_move(self, position, player):
        """Make a move on the board"""
        if self.board[position] == " ":
            self.board[position] = player
            return True
        return False
    
    def is_board_full(self):
        """Check if the board is full"""
        return " " not in self.board
    
    def check_winner(self):
        """Check if there's a winner. Returns winner symbol or None"""
        #Check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i + 1] == self.board[i + 2] != " ":
                return self.board[i]
        
        #Check columns
        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] != " ":
                return self.board[i]
        
        #Check diagonals
        if self.board[0] == self.board[4] == self.board[8] != " ":
            return self.board[0]
        if self.board[2] == self.board[4] == self.board[6] != " ":
            return self.board[2]
        
        return None
    
    def game_over(self):
        """Check if the game is over"""
        return self.check_winner() or self.is_board_full()
        return False

# if __name__ == "__main__":
#     game = TicTacToe()
#     game.make_move(0, "X")
#     game.make_move(1, "X")
#     game.make_move(2, "X")
#     game.print_board()
#     print(game.check_winner())
#     print(game.available_moves())