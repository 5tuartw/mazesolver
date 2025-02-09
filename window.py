#from tkinter import Tk, BOTH, Canvas
import tkinter as tk
from tkinter import ttk
from maze import Maze


class Window:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._num_rows = 0
        self._num_cols = 0
        self._margin = 10
        self._cell_size = 0
        self.__root = tk.Tk()
        self.__root.title("Maze Solver")
        self.__canvas = tk.Canvas(self.__root, bg="white", height=height, width=width, highlightthickness=0)
        self.add_buttons()
        self.__canvas.pack(fill=tk.BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self._maze = None
        self._mazes = []

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self):
        self.__running = False

    def draw_line(self, line, fill_color = "black"):
        return line.draw(self.__canvas, fill_color)
    
    def add_buttons(self):
        control_frame = tk.Frame(self.__root)
        control_frame.pack(side = tk.TOP)

        size_select_lbl = tk.Label(control_frame, text="Select maze creation style:")
        size_select_lbl.pack(side=tk.LEFT)
        small_btn = ttk.Button(control_frame, text="Backtrack", command = lambda: self._create_mazes("Backtrack"))
        small_btn.pack(side=tk.LEFT)
        medium_btn = ttk.Button(control_frame, text="Prim's", command = lambda:  self._create_mazes("Prim's"))
        medium_btn.pack(side=tk.LEFT)
        large_btn = ttk.Button(control_frame, text="Kruskal's", command = lambda:  self._create_mazes("Kruskal's"))
        large_btn.pack(side=tk.LEFT)
        control_frame.pack()
    
    def _create_mazes(self, style):
        self.__canvas.delete("all")
        self._mazes = []
        if style == "Backtrack":
            self._num_cols = 8
            self._num_rows = 6
            print(f"Style: {style}")
        if style == "Prim's":
            self._num_cols = 8
            self._num_rows = 6
            print(f"Style: {style}")
        if style == "Kruskal's":
            self._num_cols = 8
            self._num_rows = 6
            print(f"Style: {style}")
        
        self._calculate_cell_size(self._width - 2 * self._margin, self._height - 2 * self._margin)

        x_position = self._margin
        y_position = self._margin

        for i in range(12):
            self._mazes.append(Maze(x_position,
                                    y_position,
                                    self._num_rows,
                                    self._num_cols,
                                    self._cell_size,
                                    self._cell_size,
                                    self.__root,
                                    self.__canvas,
                                    style=style))
            # Update x_position for the next maze
            x_position += self._num_cols * self._cell_size + 10
            # If the next maze exceeds the canvas width, move to the next row
            if x_position + self._num_cols * self._cell_size > self._width:
                x_position = self._margin
                y_position += self._num_rows * self._cell_size + 10

            # self._mazes[i].solve()
            self._mazes[i].draw_shortest_path()

        print("Mazes initialised!")
    
    def _calculate_cell_size(self, maze_width, maze_height):
        #check if basing size on width works for height as well
        cell_size = maze_width / self._num_cols
        if cell_size * self._num_rows < maze_height:
            self._cell_size = cell_size / 4
        #else base size on height
        else:
            self._cell_size = maze_height / self._num_rows / 4
    
    

        




