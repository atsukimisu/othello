class Rule:
  def __init__(self):
    pass

  def is_placeable_black(self, row_number, column_number, board_list):
    white = "●"
    if board_list[row_number - 1][column_number - 1] != white and board_list[row_number - 1][column_number] != white and board_list[row_number - 1][column_number + 1] != white and board_list[row_number][column_number - 1] != white and board_list[row_number][column_number + 1] != white and board_list[row_number + 1][column_number - 1] != white and board_list[row_number + 1][column_number] != white and board_list[row_number + 1][column_number + 1] != white:
      return False
    while 1 <= row_number <= 8 and 1 <= column_number <= 8:
      for i in range(2, 8):
        if board_list[row_number - i][column_number - i] == "-":
          break
        elif  board_list[row_number - i][column_number - i] == "●":
          continue
        return True
    while 1 <= row_number <= 8 and 1 <= column_number <= 8:
      for i in range(2, 8):
        if board_list[row_number - i][column_number] == "-":
          break
        elif  board_list[row_number - i][column_number] == "●":
          continue
        return True
    while 1 <= row_number <= 8 and 1 <= column_number <= 8:
      for i in range(2, 8):
        if board_list[row_number][column_number - i] == "-":
          break
        elif  board_list[row_number][column_number - i] == "●":
          continue
        return True
    while 1 <= row_number <= 8 and 1 <= column_number <= 8:
      for i in range(2, 8):
        if board_list[row_number + i][column_number + i] == "-":
          break
        elif  board_list[row_number + i][column_number + i] == "●":
          continue
        return True
    while 1 <= row_number <= 8 and 1 <= column_number <= 8:
      for i in range(2, 8):
        if board_list[row_number + i][column_number] == "-":
          break
        elif  board_list[row_number + i][column_number] == "●":
          continue
        return True
    while 1 <= row_number <= 8 and 1 <= column_number <= 8:
      for i in range(2, 8):
        if board_list[row_number][column_number + i] == "-":
          break
        elif  board_list[row_number][column_number + i] == "●":
          continue
        return True
    while 1 <= row_number <= 8 and 1 <= column_number <= 8:
      for i in range(2, 8):
        if board_list[row_number - i][column_number + i] == "-":
          break
        elif  board_list[row_number - i][column_number + i] == "●":
          continue
        return True
    while 1 <= row_number <= 8 and 1 <= column_number <= 8:
      for i in range(2, 8):
        if board_list[row_number + i][column_number - i] == "-":
          break
        elif  board_list[row_number + i][column_number - i] == "●":
          continue
        return True
    return False

  def is_placeable_white(self, row_number, column_number, board_list):
      black = "⚪︎"
      if board_list[row_number - 1][column_number - 1] != black and board_list[row_number - 1][column_number] != black and board_list[row_number - 1][column_number + 1] != black and board_list[row_number][column_number - 1] != black and board_list[row_number][column_number + 1] != black and board_list[row_number + 1][column_number - 1] != black and board_list[row_number + 1][column_number] != black and board_list[row_number + 1][column_number + 1] != black:
        return False
      while 1 <= row_number <= 8 and 1 <= column_number <= 8:
        for i in range(2, 8):
          if board_list[row_number - i][column_number - i] == "-":
            break
          elif  board_list[row_number - i][column_number - i] == black:
            continue
          return True
      while 1 <= row_number <= 8 and 1 <= column_number <= 8:
        for i in range(2, 8):
          if board_list[row_number - i][column_number] == "-":
            break
          elif  board_list[row_number - i][column_number] == black:
            continue
          return True
      while 1 <= row_number <= 8 and 1 <= column_number <= 8:
        for i in range(2, 8):
          if board_list[row_number][column_number - i] == "-":
            break
          elif  board_list[row_number][column_number - i] == black:
            continue
          return True
      while 1 <= row_number <= 8 and 1 <= column_number <= 8:
        for i in range(2, 8):
          if board_list[row_number + i][column_number + i] == "-":
            break
          elif  board_list[row_number + i][column_number + i] == black:
            continue
          return True
      while 1 <= row_number <= 8 and 1 <= column_number <= 8:
        for i in range(2, 8):
          if board_list[row_number + i][column_number] == "-":
            break
          elif  board_list[row_number + i][column_number] == black:
            continue
          return True
      while 1 <= row_number <= 8 and 1 <= column_number <= 8:
        for i in range(2, 8):
          if board_list[row_number][column_number + i] == "-":
            break
          elif  board_list[row_number][column_number + i] == black:
            continue
          return True
      while 1 <= row_number <= 8 and 1 <= column_number <= 8:
        for i in range(2, 8):
          if board_list[row_number - i][column_number + i] == "-":
            break
          elif  board_list[row_number - i][column_number + i] == black:
            continue
          return True
      while 1 <= row_number <= 8 and 1 <= column_number <= 8:
        for i in range(2, 8):
          if board_list[row_number + i][column_number - i] == "-":
            break
          elif  board_list[row_number + i][column_number - i] == black:
            continue
          return True
      return False

  def flip_stones_white(self, row_number, column_number, board_list):
      directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
      opponent = "⚪︎"
      player = "●"
      for dx, dy in directions:
          ny, nx = column_number + dx, row_number + dy
          stones_to_flip = []     
          while 0 <= nx < 8 and 0 <= ny < 8:
              if board_list[nx][ny] == opponent:
                  stones_to_flip.append((nx, ny))
              elif board_list[nx][ny] == player:
                  for fx, fy in stones_to_flip:
                      board_list[fx][fy] = player
                  break
              else:
                  break
              nx, ny = nx + dx, ny + dy
      return board_list

  def flip_stones_black(self, row_number, column_number, board_list):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    opponent = "●"
    player = "⚪︎"
    for dx, dy in directions:
        ny, nx = column_number + dx, row_number + dy
        stones_to_flip = []
        while 0 <= nx < 8 and 0 <= ny < 8:
            if board_list[nx][ny] == opponent:
                stones_to_flip.append((nx, ny))
            elif board_list[nx][ny] == player:
                for fx, fy in stones_to_flip:
                    board_list[fx][fy] = player
                break
            else:
                break
            nx, ny = nx + dx, ny + dy
    return board_list

  def is_end(self, board_list):
    for list_component in board_list:
      if '-' in list_component:
        return False
    return True