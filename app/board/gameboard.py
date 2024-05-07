class Board:
  def __init__(self):
    pass

  def make_game_board(self):
    row_number = 8
    board_list = []
    for i in range(row_number + 1):
      board_component = []
      for j in range(row_number + 1):
        if i == 0:
          board_component.append(' ')
          continue
        elif j == 0:
          board_component.append(' ')
          continue
        board_component.append('-')
      board_list.append(board_component)
    return board_list
  
  def show_board(self, board_list):
    for i in board_list:
      board = ' '.join(i)
      print(board)

  def set_start(self):
    start_board = self.make_game_board()
    start_board[5][4] = '○'
    start_board[4][5] = '○'
    start_board[5][5] = '●'
    start_board[4][4] = '●'
    return start_board
