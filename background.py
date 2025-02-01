import tkinter as tk

def create_gradient(canvas, width, height, start_color, end_color, direction="vertical"):
    """Creates a gradient background on a Tkinter Canvas.

    Args:
        canvas: The Tkinter Canvas widget.
        width: The width of the Canvas.
        height: The height of the Canvas.
        start_color: The starting color of the gradient (e.g., "#RRGGBB" or color name).
        end_color: The ending color of the gradient.
        direction: "vertical" or "horizontal" (default is "vertical").
    """

    # Convert hex colors to RGB tuples (if necessary)
    start_rgb = canvas.winfo_rgb(start_color)
    end_rgb = canvas.winfo_rgb(end_color)

    if direction == "vertical":
        for i in range(height):
            # Calculate the interpolated color for this row
            r = int(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * i / height)
            g = int(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * i / height)
            b = int(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * i / height)
            hex_color = f"#{r:04x}{g:04x}{b:04x}"  # Convert back to hex

            canvas.create_rectangle(0, i, width, i + 1, fill=hex_color, outline="") #outline="" removes the border

    elif direction == "horizontal":
        for i in range(width):
            # Calculate the interpolated color for this column
            r = int(start_rgb[0] + (end_rgb[0] - start_rgb[0]) * i / width)
            g = int(start_rgb[1] + (end_rgb[1] - start_rgb[1]) * i / width)
            b = int(start_rgb[2] + (end_rgb[2] - start_rgb[2]) * i / width)
            hex_color = f"#{r:04x}{g:04x}{b:04x}"  # Convert back to hex
            canvas.create_rectangle(i, 0, i + 1, height, fill=hex_color, outline="")

    else:
        raise ValueError("Invalid direction. Choose 'vertical' or 'horizontal'.")


#root = tk.Tk()
#canvas_width = 400
#canvas_height = 300
#canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, highlightthickness=0)  # highlightthickness=0 to remove default canvas border
#canvas.pack()

#create_gradient(canvas, canvas_width, canvas_height, "blue", "white", "vertical")  # Example: Vertical blue to white
#create_gradient(canvas, canvas_width, canvas_height, "red", "yellow", "horizontal") # Example: Horizontal red to yellow


#root.mainloop()