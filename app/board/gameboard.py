class Board:
  def __init__(self, rule):
    self.rule = rule

  def show_board(self):
    print("  " + " ".join([str(i) for i in range(8)]))
    for i in range(8):
      print(str(i) + " " + " ".join(self.rule.game_board()[i]))
