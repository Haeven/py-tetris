from shape import Shape

class Tetris:
  shape = None
  grid = []
  state = "play"
  score = 0
  zoom = 20
  level = 2
  x = 100
  y = 60
  height = 0
  width = 0
  
  def __init__(self, height, width):
    self.level = 2
    self.score = 0
    self.state = "play"
    self.grid = []
    self.height = 0
    self.width = 0
    self.x = 100
    self.y = 60
    self.zoom = 20
    self.shape = None

    self.height = height
    self.width = width
    self.grid = []
    self.score = 0
    self.state = "play"
    # Initialize a grid corresponding to the width and height variables
    for i in range(height):
      row = []
      for j in range(width):
        row.append(0)
      self.grid.append(row)

  def new_shape(self):
    self.shape = Shape(3, 0)
  
  def block_intersects(self):
    intersection = False
    # Iterate over all cells in the 4x4 matrix to check if cell is out of height/width bounds 
    # or if cell intersects with another block grid
    for i in range(4):
      for j in range(4):
        if i * 4 + j in self.shape.block():
          if i + self.shape.y > self.height - 1 or \
              j + self.shape.x > self.width - 1 or \
              j + self.shape.x < 0 or \
              self.grid[i + self.shape.y][j + self.shape.x] > 0:
                # Check grid area surrounding our block is not allocated to another block
                intersection = True
    return intersection
  def break_rows(self):
      rows = 0
      for i in range(1, self.height):
          zeros = 0
          for j in range(self.width):
              if self.grid[i][j] == 0:
                  zeros += 1
          if zeros == 0:
              rows += 1
              for i1 in range(i, 1, -1):
                  for j in range(self.width):
                      self.grid[i1][j] = self.grid[i1 - 1][j]
      self.score += rows ** 2

  def go_space(self):
      while not self.block_intersects():
          self.shape.y += 1
      self.shape.y -= 1
      self.place_block()

  def go_down(self):
      self.shape.y += 1
      if self.block_intersects():
          self.shape.y -= 1
          self.place_block()

  def place_block(self):
      for i in range(4):
          for j in range(4):
              if i * 4 + j in self.shape.block():
                  self.grid[i + self.shape.y][j + self.shape.x] = self.shape.color
      self.break_rows()
      self.new_shape()
      if self.block_intersects():
          self.state = "escape"

  def go_side(self, dx):
      prev_x = self.shape.x
      self.shape.x += dx
      if self.block_intersects():
          self.shape.x = prev_x

  def rotate(self):
      prev_r = self.shape.rotation
      self.shape.rotate()
      if self.block_intersects():
          self.shape.rotation = prev_r