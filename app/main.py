from algorhythm.rule import Rule
from controller.control import Controller
from board.gameboard import Board

def main():
  ui = Board()
  board_list = ui.set_start()
  ui.show_board(board_list)
  rule = Rule()
  controller = Controller(rule)
  end_flag = False
  while end_flag == False:
    row_number, column_number, board_list = controller.put_white_stone(board_list)
    board_list = rule.flip_stones_white(row_number, column_number, board_list)
    end_flag = rule.is_end(board_list)
    ui.show_board(board_list)
    row_number, column_number, board_list = controller.put_black_stone(board_list)
    board_list = rule.flip_stones_black(row_number, column_number, board_list)
    end_flag = rule.is_end(board_list)
    ui.show_board(board_list)

if __name__ == "__main__":
  main()
