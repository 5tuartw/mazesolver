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


main()
