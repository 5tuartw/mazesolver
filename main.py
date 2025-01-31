from graphics import Window
from maze import Maze
from cell import Cell
import sys

def main():
    screen_x = 800
    screen_y = 600
    sys.setrecursionlimit(10000)
    win = Window(screen_x, screen_y)
    
    num_rows = 8
    num_cols = 12
    margin = 25
    
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    maze.solve()

    '''cell1 = Cell(win)
    cell1.draw(50,50,100,100)
    cell2 = Cell(win)
    cell2.draw(100,50,150,100)

    cell1.draw_move(cell2, True)'''
    
    win.wait_for_close()

main()
