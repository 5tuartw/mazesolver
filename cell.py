from tkinter import Tk

class Cell():
  def __init__(self, win):
    self.has_left_wall = True
    self.has_right_wall = True
    self.has_top_wall = True
    self.has_bottom_wall = True
    self.num_walls = 4
    self.visited = False
    self._x1 = None
    self._x2 = None
    self._y1 = None
    self._y2 = None
    self._win = win

  def draw(self, x1, y1, x2, y2):
    if self._win is None:
      return
    self._x1 = x1
    self._x2 = x2
    self._y1 = y1
    self._y2 = y2

    if self.has_left_wall:
      self._win.create_line(x1,y1,x1,y2, fill="black")
    else:
      self._win.create_line(x1,y1,x1,y2, fill="white")
    if self.has_right_wall:
      self._win.create_line(x2,y1,x2,y2, fill="black")
    else:
      self._win.create_line(x2,y1,x2,y2, fill="white")
    if self.has_top_wall:
      self._win.create_line(x1,y1,x2,y1, fill="black")
    else:
      self._win.create_line(x1,y1,x2,y1, fill="white")
    if self.has_bottom_wall:
      self._win.create_line(x1,y2,x2,y2, fill="black")
    else:
      self._win.create_line(x1,y2,x2,y2, fill="white")

  def find_centre(self):
    return Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)
    
  def draw_move(self, to_cell, undo=False):
    #move_line = Line(self.find_centre(), to_cell.find_centre())
    start_point = self.find_centre()
    end_point = to_cell.find_centre()
    color = "gray" if undo else "red"
    self._win.create_line(start_point.x, start_point.y, end_point.x, end_point.y, fill=color)
  
  def count_walls(self):
    self.num_walls = sum([self.has_left_wall, self.has_right_wall, self.has_top_wall, self.has_bottom_wall])
    return self.num_walls

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
