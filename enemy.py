class Enemy:
    def __init__(self, canvas, cell_size, start_x, start_y, margin):
        self._canvas = canvas
        self._cell_size = cell_size
        self._x = start_x
        self._y = start_y
        self._margin = margin
        self._player_size = cell_size // 1.5
        self._shape = None
        self._create_shape()
    
    def _create_shape(self):
        # calculate centre of the cell
        centre_x = self._margin + (self._x * self._cell_size) + (self._cell_size // 2)
        centre_y = self._margin + (self._y * self._cell_size) + (self._cell_size // 2)

        # calculate player bounds from centre
        radius = self._player_size // 2
        x1 = centre_x - radius
        y1 = centre_y - radius
        x2 = centre_x + radius
        y2 = centre_y + radius

        edge_width = self._cell_size / 8


        self._shape = self._canvas.create_rectangle(x1, y1, x2, y2, outline = '#769aad', width = edge_width, fill = "white")