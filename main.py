#import tkinter as tk
from window import Window
#from maze import Maze
#from cell import Cell
import sys

def main():
    screen_x = 800
    screen_y = 600
    sys.setrecursionlimit(10000)
    win = Window(screen_x, screen_y)
    
    win.wait_for_close()

'''def calculate_cell_size(maze_width, maze_height, num_rows, num_cols):
    #check if basing size on width works for height as well
    cell_width = maze_width / num_cols
    if cell_width * num_rows < maze_height:
        return cell_width
    #else base size on height
    return maze_height / num_rows'''




main()
