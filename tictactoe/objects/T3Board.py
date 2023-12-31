
from copy import deepcopy
from typing import Optional, Tuple
from tictactoe.objects.types import EndingType, State
from tictactoe.strategies.common import check_end_state, move2str


class T3Board:
    """Tic Tac Toe Board Object
    This object represents a tic tac toe board, 
    and contains all the methods relating to the board.
    """
    board: State
    goal_len: int
    board_size: int

    def __init__(self, board_size, goal_len) -> None:
        self.board_size = board_size
        self.goal_len = goal_len

        self.board = [['' for _ in range(board_size)]
                      for _ in range(board_size)]  # n by n board

    def deep_copy(self):
        return deepcopy(self.board)

    def add_piece(self, piece: str, row, col):
        """Add a piece to the board
        This method adds a piece to the board at the specified row and column.
        """
        if self.board[row][col] != '':
            raise ValueError(
                f"Cannot place piece {piece} at {row}, {col} because there is already a piece there.")
        self.board[row][col] = piece

    def check_end(self) -> Tuple[bool, Optional[EndingType]]:
        """Check if the game is finished and return the ending type if yes
        """
        return check_end_state(self.board, self.board_size, self.goal_len)

    def print_board(self):
        print(" ", end=" ")
        for col in range(self.board_size):
            print(chr(ord('a') + col), end=" ")
        print()  # Newline
        for row in range(self.board_size):
            # Print row identifier (number)
            print(row+1, end=" ")

            for col in range(self.board_size):
                cell = self.board[row][col]
                if cell == '':
                    cell = '-'
                print(cell, end=" ")
            print()  # Newline
            
    def test(self):
        for row in range(self.board_size-1, -1, -1):
            col = 0
            for i in range(min(self.board_size - row, self.board_size - col)):
                print(row + i, col + i)
                
        for col in range(1, self.board_size):
            row = 0
            for i in range(min(self.board_size - row, self.board_size - col)):
                print(row + i, col + i)

        ## (top-right to bottom-left)
        for col in range(self.board_size):
            row = 0
            for i in range(col+1):
                print(row + i, col - i)
                
        for row in range(1, self.board_size):
            col = self.board_size - 1
            for i in range(self.board_size - row):
                print(row + i, col - i)
