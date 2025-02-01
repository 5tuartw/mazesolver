# mazesolver


## List of changes
* Addition of buttons to select maze size before drawing. This moved the maze drawing function calls into the Window Class, which then led to me updatign the Cell drawing methods to use the tkinter create_line() method instead of the draw_line method. Note: may look at separating this from the window class, as it's not the most appropriate logic for drawing the maze
* Addition of a player