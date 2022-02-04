PLAYER = 'O' # the piece that moves through the maze
GOAL = 'X' # the target that the player is trying to reach
QUICKSAND = "*" # quicksand pits that have a higher cost to travel out of

class Maze:

  def __init__(self, maze, width): # MAZE = ONE IN VIDEO, WIDTH =  14
    self.maze = maze
    self.width = width

  def print_maze(self, x = None, y = None):
    if x == None and y == None:
      print(self.maze)
    else:
      row_num = 2*x + 1
      col_num = 4*y+2

      prev_rows = self.maze[:self.width*row_num]
      curr_row = self.maze[self.width*row_num:self.width*row_num+self.width]
      post_rows = self.maze[self.width*row_num + self.width:]

      updated_row = curr_row[:col_num] + PLAYER + curr_row[col_num+1:]
      new_maze = prev_rows + updated_row + post_rows
      print(new_maze)

  def print_path(self,path):
    print("Traversing Path...")
    for cell in path:
      self.print_maze(int(cell[1]), int(cell[3]))
    print("Path Length: " + str(len(path) - 1))
