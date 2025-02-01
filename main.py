#import tkinter as tk
from graphics import *
#from maze import Maze
#from cell import Cell
import sys

def main():
    screen_x = 800
    screen_y = 600
    sys.setrecursionlimit(10000)
    win = Window(screen_x, screen_y)
    
    #title = win.Label(text="Maze Craze!")

    num_rows = 12
    num_cols = 12
    margin = 25
    maze_width = screen_x - (2 * margin)
    maze_height = screen_y - (2 * margin)
    #cell_size = calculate_cell_size(maze_width, maze_height, num_rows, num_cols)


    #maze = Maze(margin, margin, num_rows, num_cols, cell_size, cell_size, win)
    #maze.solve()
    
    win.wait_for_close()

'''def calculate_cell_size(maze_width, maze_height, num_rows, num_cols):
    #check if basing size on width works for height as well
    cell_width = maze_width / num_cols
    if cell_width * num_rows < maze_height:
        return cell_width
    #else base size on height
    return maze_height / num_rows'''




main()
