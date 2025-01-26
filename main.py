from graphics import Window, Point, Line

def main():
    win = Window(800, 600)
    
    line1 = Line(Point(100,200),Point(200,400))
    line2 = Line(Point(555,800),Point(4,29))
    win.draw_line(line1,"red")
    win.draw_line(line2,"blue")    
    win.wait_for_close()



if __name__ == "__main__":
    main()