from graphics import Line, Point


class Cell:
    def __init__(self, win, x1, x2, y1, y2):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win
        self.centre = Point((x1+x2)/2, (y1+y2)/2)
        self.visited = False
    
    def draw(self):
        top_left = Point(self._x1, self._y1)
        top_right = Point(self._x2, self._y1)
        bottom_left = Point(self._x1, self._y2)
        bottom_right = Point(self._x2, self._y2)
        left_line = Line(top_left, bottom_left)
        right_line = Line(top_right, bottom_right)
        top_line = Line(top_left, top_right)
        bottom_line = Line(bottom_left, bottom_right)

        
        color = "black" if self.has_left_wall else "white"
        self._win.draw_line(left_line, color)
        color = "black" if self.has_right_wall else "white"
        self._win.draw_line(right_line, color)
        color = "black" if self.has_top_wall else "white"
        self._win.draw_line(top_line, color)
        color = "black" if self.has_bottom_wall else "white"
        self._win.draw_line(bottom_line, color)
        
        #if self.has_left_wall:
        #    self._win.draw_line(left_line, "black")
        #if self.has_right_wall:
        #    self._win.draw_line(right_line, "black")
        #if self.has_top_wall:
        #    self._win.draw_line(top_line, "black")
        #if self.has_bottom_wall:
        #    self._win.draw_line(bottom_line, "black")

    def draw_move(self, to_cell, undo=False):
        color = "gray" if undo else "red"
        move_line = Line(self.centre, to_cell.centre)
        self._win.draw_line(move_line, color)
