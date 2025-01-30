from graphics import Window, Point, Line

def main():
    win = Window(800, 600)
    
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
    
    
    win.wait_for_close()

if __name__ == "__main__":
    main()
