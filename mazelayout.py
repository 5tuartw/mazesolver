def calculate_maze_layout(canvas_width, canvas_height, num_mazes, num_cells_per_maze):
    # Determine the number of mazes per row and column
    num_mazes_per_row = int(num_mazes ** 0.5)
    num_mazes_per_col = (num_mazes + num_mazes_per_row - 1) // num_mazes_per_row

    # Calculate the maximum cell size that fits within the canvas dimensions
    max_cell_size_x = canvas_width // (num_mazes_per_row * num_cells_per_maze)
    max_cell_size_y = canvas_height // (num_mazes_per_col * num_cells_per_maze)
    cell_size = min(max_cell_size_x, max_cell_size_y)

    # Calculate the maze dimensions
    maze_width = num_cells_per_maze * cell_size
    maze_height = num_cells_per_maze * cell_size

    # Calculate the total width and height of the mazes
    total_width = num_mazes_per_row * maze_width
    total_height = num_mazes_per_col * maze_height

    # Calculate the offset to center the mazes within the canvas
    offset_x = (canvas_width - total_width) // 2
    offset_y = (canvas_height - total_height) // 2

    return {
        "num_mazes_per_row": num_mazes_per_row,
        "num_mazes_per_col": num_mazes_per_col,
        "cell_size": cell_size,
        "maze_width": maze_width,
        "maze_height": maze_height,
        "offset_x": offset_x,
        "offset_y": offset_y
    }

def main():
    screen_x = 800
    screen_y = 600
    num_mazes = 4
    num_cells_per_maze = 10

    layout = calculate_maze_layout(screen_x, screen_y, num_mazes, num_cells_per_maze)
    print(layout)

    # Example usage with the Window class
    win = Window(screen_x, screen_y)
    for row in range(layout["num_mazes_per_col"]):
        for col in range(layout["num_mazes_per_row"]):
            x = layout["offset_x"] + col * layout["maze_width"]
            y = layout["offset_y"] + row * layout["maze_height"]
            # Create and draw the maze at (x, y) with the specified cell size
            maze = Maze(num_cells_per_maze, num_cells_per_maze, cell_size=layout["cell_size"])
            maze.draw(win, x, y)

    win.wait_for_close()

main()