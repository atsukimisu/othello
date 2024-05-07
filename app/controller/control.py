class Controller:
  def __init__(self, rule) -> None:
    self.rule = rule

  def put_white_stone(self, board_list):
    row_number = 0
    column_number = 0
    put = False
    while put == False:
      row_number = int(input("行は?"))
      column_number = int(input("列は?"))
      if self.rule.is_placeable_white(row_number, column_number, board_list):
        print("おけません。")
      else:
        board_list[row_number][column_number] = "●"
        put = True
    return row_number, column_number, board_list

  def put_black_stone(self, board_list):
    row_number = 0
    column_number = 0
    put = False
    while put == False:
      row_number = int(input("行は?"))
      column_number = int(input("列は?"))
      if self.rule.is_placeable_black(row_number, column_number):
        print("おけません。")
      else:
        board_list[row_number][column_number] = "⚪︎"
        put = True
    return row_number, column_number, board_list
