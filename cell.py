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
    
    def draw(self):
        top_left = Point(self._x1, self._y1)
        top_right = Point(self._x2, self._y1)
        bottom_left = Point(self._x1, self._y2)
        bottom_right = Point(self._x2, self._y2)

        if self.has_left_wall:
            left_line = Line(top_left, bottom_left)
            self._win.draw_line(left_line, "black")
        
        if self.has_right_wall:
            right_line = Line(top_right, bottom_right)
            self._win.draw_line(right_line, "black")

        if self.has_top_wall:
            top_line = Line(top_left, top_right)
            self._win.draw_line(top_line, "black")

        if self.has_bottom_wall:
            bottom_line = Line(bottom_left, bottom_right)
            self._win.draw_line(bottom_line, "black")
    
    def draw_move(self, to_cell, undo=False):
        color = "gray" if undo else "red"
        move_line = Line(self.centre, to_cell.centre)
        self._win.draw_line(move_line, color)