#from tkinter import Tk, BOTH, Canvas
import tkinter as tk
from background import create_gradient
from maze import Maze
from player import Player
from enemy import Enemy
from items import Powerup
from game import Game

class Window:
    def __init__(self, width, height):
        self._width = width
        self._height = height
        self._num_rows = 0
        self._num_cols = 0
        self._margin = 25
        self._cell_size = 0
        self.__root = tk.Tk()
        self.__root.title("Maze Solver")
        self.__canvas = tk.Canvas(self.__root, bg="white", height=height, width=width, highlightthickness=0)
        self.add_buttons()
        self.__canvas.pack(fill=tk.BOTH, expand=1)
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self._player = None
        self._enemey = None
        self._maze = None
        self._game = None

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

        size_select_lbl = tk.Label(control_frame, text="Select size:")
        size_select_lbl.pack(side=tk.LEFT)
        small_btn = tk.Button(control_frame, text="Small", command = lambda: self._initiate_game("small"))
        small_btn.pack(side=tk.LEFT)
        medium_btn = tk.Button(control_frame, text="Medium", command = lambda:  self._initiate_game("medium"))
        medium_btn.pack(side=tk.LEFT)
        large_btn = tk.Button(control_frame, text="Large", command = lambda:  self._initiate_game("large"))
        large_btn.pack(side=tk.LEFT)
        control_frame.pack()
    
    def _initiate_game(self, size):
        if size == "small":
            self._num_cols = 8
            self._num_rows = 6
            print(f"Size: {size}")
        if size == "medium":
            self._num_cols = 12
            self._num_rows = 9
            print(f"Size: {size}")
        if size == "large":
            self._num_cols = 24
            self._num_rows = 18
            print(f"Size: {size}")
        
        self._calculate_cell_size(self._width - 2 * self._margin, self._height - 2 * self._margin)
        
        self._maze = Maze(self._margin,
                          self._margin,
                          self._num_rows,
                          self._num_cols,
                          self._cell_size,
                          self._cell_size,
                          self.__root,
                          self.__canvas)
        
        print("Maze initialised!")
        self._player = Player(self.__canvas, self._cell_size, 0, 0, self._margin)
        self._enemy = Enemy(self.__canvas, self._cell_size, self._num_cols-1, self._num_rows-1, self._margin)
        self._game = Game(self.__canvas, self._maze, self._player)
        self._game.find_deadends()
        item_loc = self._game.choose_deadend()
        self._powerup = Powerup(self.__canvas, self._cell_size, item_loc[0], item_loc[1], self._margin, "invisibility")
        self._setup_controls()
        #self._maze.solve()
    
    def _calculate_cell_size(self, maze_width, maze_height):
        #check if basing size on width works for height as well
        cell_size = maze_width / self._num_cols
        if cell_size * self._num_rows < maze_height:
            self._cell_size = cell_size
        #else base size on height
        else:
            self._cell_size = maze_height / self._num_rows
    
    def _setup_controls(self):
        self.__root.bind('<Left>', self._on_left_press)
        self.__root.bind('<Up>', self._on_up_press)
        self.__root.bind('<Down>', self._on_down_press)
        self.__root.bind('<Right>', self._on_right_press)
    
    def _on_left_press(self, event):
        self._game.move_left()
    def _on_right_press(self, event):
        self._game.move_right()
    def _on_down_press(self, event):
        self._game.move_down()
    def _on_up_press(self, event):
        self._game.move_up()
    

        




