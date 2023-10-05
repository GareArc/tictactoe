from tictactoe.objects.types import State

def _score_consecutive(line, goal_len: int, board_size: int, piece: str) -> float:

    """
    Score a line of the board for a given piece.
    """
    result = -500
    p_len = 0.0
    p_potential = 0.0
    empty = 0
    for i in range(board_size):
        if line[i] == piece:
            p_len += 1
            p_potential += 1
            if p_len >= goal_len:
                return goal_len * 1000
        elif line[i] == '':
            p_potential += 1
            empty += 1
        else:
            if p_potential >= goal_len:
                score = (p_len / goal_len) * 5 + p_len * 10
                if score > result:
                    result = score
            p_len = 0.0
            p_potential = 0.0
            
    if p_potential >= goal_len:
        score = (p_len / goal_len) * 5 + p_len * 10 
        if score > result:
            result = score
    
    return result

def _score_column(board: State, col: int, goal_len: int, board_size: int, piece: str) -> float:
    """
    Score a column of the board for a given piece.
    """
    column = [board[i][col] for i in range(board_size)]
    return _score_consecutive(column, goal_len, board_size, piece)

def _score_row(board: State, row: int, goal_len: int, board_size: int, piece: str) -> float:
    """
    Score a row of the board for a given piece.
    """
    return _score_consecutive(board[row], goal_len, board_size, piece)

def _score_diagonal(board: State, goal_len: int, board_size: int, piece: str) -> float:
    """
    Score a diagonal of the board for a given piece.
    """
    score = 0.0
    # top-right to bottom-left
    for row in range(board_size):
        col = 0
        line = [board[row + i][col + i] for i in range(min(board_size - row, board_size - col))]
        score = max(score, _score_consecutive(line, goal_len, min(board_size - row, board_size - col), piece))
        # print(f"line: {line}, score: {_score_consecutive(line, goal_len, min(board_size - row, board_size - col), piece)}")
    for col in range(1, board_size):
        row = 0
        line = [board[row + i][col + i] for i in range(min(board_size - row, board_size - col))]
        score = max(score, _score_consecutive(line, goal_len, min(board_size - row, board_size - col), piece))
        # print(f"line: {line}, score: {_score_consecutive(line, goal_len, min(board_size - row, board_size - col), piece)}")
    # top-left to bottom-right
    for col in range(board_size):
        row = 0
        line = [board[row + i][col - i] for i in range(col+1)]
        score = max(score, _score_consecutive(line, goal_len, col+1, piece))
        # print(f"line: {line}, score: {_score_consecutive(line, goal_len, col+1, piece)}")
    for row in range(1, board_size):
        col = board_size - 1
        line = [board[row + i][col - i] for i in range(board_size - row)]
        score = max(score, _score_consecutive(line, goal_len, board_size - row, piece))
        # print(f"line: {line}, score: {_score_consecutive(line, goal_len, board_size - row, piece)}")
    return score
            

def advanced_heuristic(board: State, goal_len: int, board_size: int, **kwargs) -> float:
    """
    Advanced heuristic function for tic-tac-toe(x).
    """
    score_x = 0.0
    score_o = 0.0
    for row in range(board_size):
        score_x = max(score_x, _score_row(board, row, goal_len, board_size, 'x'))
        score_o = max(score_o, _score_row(board, row, goal_len, board_size, 'o'))
    # print(f"After row: score_x: {score_x}")
    for col in range(board_size):
        score_x = max(score_x, _score_column(board, col, goal_len, board_size, 'x'))
        score_o = max(score_o, _score_column(board, col, goal_len, board_size, 'o'))
    # print(f"After col: score_x: {score_x}")
    score_x = max(score_x, _score_diagonal(board, goal_len, board_size, 'x'))
    score_o = max(score_o, _score_diagonal(board, goal_len, board_size, 'o'))
    # print(f"After diag: score_x: {score_x}")
    
    return score_x - 2 * score_o
    
    
if __name__ == '__main__':
    state = [['x', 'x', 'o', ''],
             ['', '', 'x', ''],
             ['', '', 'o', ''],
             ['', '', '', '']]
    print(advanced_heuristic(state, 3, 4))