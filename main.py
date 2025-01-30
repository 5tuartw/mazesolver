from graphics import Window, Point, Line
from cell import Cell
from maze import Maze

def main():
    screen_x = 800
    screen_y = 600
    win = Window(screen_x, screen_y)
    
    num_rows = 8
    num_cols = 12
    margin = 25
    
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    
    
    win.wait_for_close()

main()
