from graphics import Line, Point

class Cell():
  def __init__(self, win):
    self.has_left_wall = True
    self.has_right_wall = True
    self.has_top_wall = True
    self.has_bottom_wall = True
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
      line = Line(Point(x1,y1), Point(x1,y2))
      self._win.draw_line(line)
    else:
      line = Line(Point(x1,y1), Point(x1,y2))
      self._win.draw_line(line, "white")      
    if self.has_right_wall:
      line = Line(Point(x2,y1), Point(x2,y2))
      self._win.draw_line(line)
    else:
      line = Line(Point(x2,y1), Point(x2,y2))
      self._win.draw_line(line, "white")
    if self.has_top_wall:
      line = Line(Point(x1,y1), Point(x2,y1))
      self._win.draw_line(line)
    else:
      line = Line(Point(x1,y1), Point(x2,y1))
      self._win.draw_line(line, "white")
    if self.has_bottom_wall:
      line = Line(Point(x1,y2), Point(x2,y2))
      self._win.draw_line(line)
    else:
      line = Line(Point(x1,y2), Point(x2,y2))
      self._win.draw_line(line, "white")

  def find_centre(self):
    return Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)
    
  def draw_move(self, to_cell, undo=False):
    move_line = Line(self.find_centre(), to_cell.find_centre())
    color = "gray" if undo else "red"
    self._win.draw_line(move_line, color)
