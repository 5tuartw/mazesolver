from graphics import Window, Point, Line
from cell import Cell

def main():
    
    cell1 = Cell(win)
    cell1.has_left_wall = False
    cell1.draw(20,20,40,40)

    cell2 = Cell(win)
    cell2.has_right_wall = False
    cell2.draw(400,400,600,600)

    cell3 = Cell(win)
    cell3.has_top_wall = False
    cell3.draw(134,67,234,167)

    cell4 = Cell(win)
    cell4.has_bottom_wall = False
    cell4.draw(700,500,750,550)

    num_rows = 8
    num_cols = 12
    margin = 25
    screen_x = 800
    screen_y = 600
    
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    
    
    win.wait_for_close()

main()
