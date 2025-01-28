from cell import Cell
import time

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win = None,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for i in range(self.num_cols):
            column = []
            for j in range(self.num_rows):
                column.append(Cell(
                    self.win,
                    (self.x1+(self.cell_size_x*j)),
                    (self.x1+(self.cell_size_x*(j+1))),
                    (self.y1+(self.cell_size_y*i)),
                    (self.y1+(self.cell_size_y*(i+1)))
                    ))
            self._cells.append(column)
        
        #for i in self._cells:
        #    for j in i:
        #        j.draw()
        #        self._animate()
    
    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_left_wall = False
        self._cells[0][0].draw()
        self._cells[num_rows-1][num_cols-1].has_right_wall = False
        self._cells[num_rows-1][num_cols-1].draw()
        
