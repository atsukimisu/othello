class Controller:
  def __init__(self, board, rule) -> None:
    self.board = board
    self.rule = rule

  def show_board(self):
    self.board.show_board()

  def current_player(self):
    return self.rule.player()

  def count_pieces(self):
    return self.rule.count_pieces()

  def make_move(self, row, col):
    return self.rule.make_move(row, col)

  def execute(self):
    while self.rule.has_valid_moves():
      self.show_board()
      print(f"{self.current_player()}の番です")
      row, col = map(int, input("行と列を入力してください: ").split())
      if not self.make_move(row,col):
        print("もう一度入力してください")
    self.show_board()
    black, white = self.count_pieces()
    print(f"ゲーム終了。◯: {black}, ●: {white}")
    if black > white:
        print("黒の勝ち!")
    elif white > black:
        print("白の勝ち!")
    else:
        print("引き分け!")
