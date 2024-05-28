from algorhythm.rule import Rule
from controller.control import Controller
from board.gameboard import Board

def main():
  rule = Rule()
  board = Board(rule)
  controller = Controller(board, rule)
  controller.execute()

if __name__ == "__main__":
  main()
