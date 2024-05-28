class Rule:
  def __init__(self):
        self.board = [['-' for _ in range(8)] for _ in range(8)]
        self.board[3][3], self.board[3][4] = '●', '◯'
        self.board[4][3], self.board[4][4] = '◯', '●'
        self.current_player = '◯'
        self.directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

  def game_board(self):
      return self.board

  def player(self):
      return '黒' if self.current_player == '◯' else '白'

  def make_move(self, row, col):
      if not self.is_valid_move(row, col):
          return False
      self.board[row][col] = self.current_player
      for d in self.directions:
          if self.check_direction(row, col, d[0], d[1]):
              self.flip_pieces(row, col, d[0], d[1])
      self.current_player = self.opponent()
      return True

  def is_valid_move(self, row, col):
      if self.board[row][col] != '-':
          return False
      for d in self.directions:
          if self.check_direction(row, col, d[0], d[1]):
              return True
      return False

  def check_direction(self, row, col, dx, dy):
      row_index, column_index = row + dx, col + dy
      if not (0 <= row_index < 8 and 0 <= column_index < 8) or self.board[row_index][column_index] != self.opponent():
          return False
      while 0 <= row_index < 8 and 0 <= column_index < 8:
          if self.board[row_index][column_index] == '-':
              return False
          if self.board[row_index][column_index] == self.current_player:
              return True
          row_index += dx
          column_index += dy
      return False

  def flip_pieces(self, row, col, dx, dy):
      row_index, column_index = row + dx, col + dy
      while self.board[row_index][column_index] == self.opponent():
          self.board[row_index][column_index] = self.current_player
          row_index += dx
          column_index += dy

  def opponent(self):
      return '◯' if self.current_player == '●' else '●'

  def count_pieces(self):
      black, white = 0, 0
      for row in self.board:
          black += row.count('◯')
          white += row.count('●')
      return black, white

  def has_valid_moves(self):
        for i in range(8):
            for j in range(8):
                if self.is_valid_move(i, j):
                    return True
        return False
