class TicTacToe:

  def __init__(self):
    self.grid = [["-" for i in range(3)] for j in range(3)]
    self.plays = 0
    self.player_turn = 0

  def reset_game(self):
    self.grid = [["-" for i in range(3)] for j in range(3)]
    self.plays = 0
    self.player_turn = 0

  def get_grid(self):
    return self.grid

  def play(self, x, y):
    if(self.grid_is_empty(x, y)):
      self.grid[x][y] = self.player_turn
      self.plays += 1

      if(self.player_won(self.player_turn)):
        print("Você ganhou!")
      elif(self.plays == 9):
        print("O jogo empatou!")
      self.player_turn = int(not(self.player_turn))
    else:
      print("Jogada inválida!")

  def player_won(self, player):
    for i in range(3):
      if(self.grid[i][0] == self.grid[i][1] == self.grid[i][2] != "-"):
        return True
      if(self.grid[0][i] == self.grid[1][i] == self.grid[2][i] != "-"):
        return True
    if(self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != "-"):
      return True
    if(self.grid[0][2] == self.grid[1][1] == self.grid[2][0] != "-"):
      return True
    return False
  
  def grid_is_empty(self, x, y):
    return (self.grid[x][y] == "-")

  def print_grid(self):
    for i in range(3):
      print("{0} {1} {2}".format(self.grid[i][0], self.grid[i][1], self.grid[i][2]))
    print()