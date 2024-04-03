class Board:
  def __init__(self):
    pass

  def make_game_board(self):
    row_number = int(input('何×何マスでプレイする？'))
    board_list = []
    for i in range(row_number):
      board_component = []
      for j in range(row_number):
        board_component.append('-')
      board_list.append(board_component)
    return board_list
  
  def show_board(self, board_list):
    for i in board_list:
      board = ' '.join(i)
      print(board)

b = Board()
board = b.make_game_board()
b.show_board(board)
