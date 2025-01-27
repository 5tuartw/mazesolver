from graphics import Window, Point, Line
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)
    
    line1 = Line(Point(100,200),Point(200,400))
    line2 = Line(Point(555,800),Point(4,29))
    win.draw_line(line1,"red")
    win.draw_line(line2,"blue")
    cell1 = Cell(win, 120, 140, 120, 140)    
    cell1.draw()
    cell2 = Cell(win, 220, 240, 120, 140)
    cell2.has_bottom_wall = False
    cell2.draw()
    cell1.draw_move(cell2, False)

    maze = Maze(10,10,5,5,20,20,win)
    

    win.wait_for_close()



if __name__ == "__main__":
    main()