from cell import Cell
import time
import random

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
            seed = None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._create_cells()
        self.seed = seed
        if self.seed != None:
            random.seed(seed)
        self.cells_visited = 0

    def _create_cells(self):
        self._cells = []
        for i in range(self.num_rows):
            row = []
            for j in range(self.num_cols):
                row.append(Cell(
                    self.win,
                    (self.x1+(self.cell_size_x*j)),
                    (self.x1+(self.cell_size_x*(j+1))),
                    (self.y1+(self.cell_size_y*i)),
                    (self.y1+(self.cell_size_y*(i+1)))
                    ))
            self._cells.append(row)
        
        for i in self._cells:
            for j in i:
                j.draw()
                self._animate()
        
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
    
    def _animate(self):
        self.win.redraw()
        time.sleep(0.005)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[0][0].draw()
        self._cells[self.num_rows-1][self.num_cols-1].has_bottom_wall = False
        self._cells[self.num_rows-1][self.num_cols-1].draw()
        
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            to_visit = []
            #try left
            if j > 0 and not self._cells[i][j-1].visited:
                to_visit.append((i, j-1, "left"))
            #try right
            if j < (self.num_rows - 1) and not self._cells[i][j+1].visited:
                to_visit.append((i, j+1, "right"))
            #try up
            if i > 0 and not self._cells[i-1][j].visited:
                to_visit.append((i-1, j, "up"))
            #try down
            if i < (self.num_cols -1) and not self._cells[i+1][j].visited:
                to_visit.append((i+1, j, "down"))
            
            #if no cells left to try, draw and return to break loop
            if to_visit == []:
                self._cells[i][j].draw()
                #print("No more paths here")
                return
            #print(to_visit)
            pick_random = to_visit[random.randrange(0, len(to_visit))]
            #print(f"Selecting cell: {pick_random}")

            direction = pick_random[2]
            #print(f"At cell ({i},{j}) Going {direction}")
            if direction == "up":
                #print(f"Breaking wall between ({i},{j}) and ({pick_random[0]},{pick_random[1]})")
                #print(f"Before: top={self._cells[i][j].has_top_wall}, bottom={self._cells[pick_random[0]][pick_random[1]].has_bottom_wall}")
                self._cells[i][j].has_top_wall = False
                self._cells[pick_random[0]][pick_random[1]].has_bottom_wall = False
                #print(f"After: top={self._cells[i][j].has_top_wall}, bottom={self._cells[pick_random[0]][pick_random[1]].has_bottom_wall}")

            elif direction == "down":
                #print(f"Breaking wall between ({i},{j}) and ({pick_random[0]},{pick_random[1]})")
                #print(f"Before: bottom={self._cells[i][j].has_bottom_wall}, top={self._cells[pick_random[0]][pick_random[1]].has_top_wall}")
                self._cells[i][j].has_bottom_wall = False
                self._cells[pick_random[0]][pick_random[1]].has_top_wall = False
                #print(f"After: bottom={self._cells[i][j].has_bottom_wall}, top={self._cells[pick_random[0]][pick_random[1]].has_top_wall}")

            elif direction == "left":
                #print(f"Breaking wall between ({i},{j}) and ({pick_random[0]},{pick_random[1]})")
                #print(f"Before: left={self._cells[i][j].has_left_wall}, right={self._cells[pick_random[0]][pick_random[1]].has_right_wall}")
                self._cells[i][j].has_left_wall = False
                self._cells[pick_random[0]][pick_random[1]].has_right_wall = False
                #print(f"After: left={self._cells[i][j].has_left_wall}, right={self._cells[pick_random[0]][pick_random[1]].has_right_wall}")

            elif direction == "right":
                #print(f"Breaking wall between ({i},{j}) and ({pick_random[0]},{pick_random[1]})")
                #print(f"Before: right={self._cells[i][j].has_right_wall}, left={self._cells[pick_random[0]][pick_random[1]].has_left_wall}")
                self._cells[i][j].has_right_wall = False
                self._cells[pick_random[0]][pick_random[1]].has_left_wall = False
                #print(f"After: right={self._cells[i][j].has_right_wall}, left={self._cells[pick_random[0]][pick_random[1]].has_left_wall}")
            
            self._cells[i][j].draw()
            self._cells[i][j].draw_move(self._cells[pick_random[0]][pick_random[1]])
            #self._cells[pick_random[0]][pick_random[1]].draw()

            self._break_walls_r(pick_random[0], pick_random[1])
            
                

