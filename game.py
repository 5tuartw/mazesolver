class Game:
    def __init__(self, canvas, maze, player):
        self._canvas = canvas
        self._maze = maze
        self._player = player
        self._player_x = self._player._x
        self._player_y = self._player._y
    
    def move_left(self):
        if self._player_x > 0 and not self._maze._cells[self._player_x][self._player_y].has_left_wall:
            self._canvas.move(self._player._shape, -self._player._cell_size, 0)
            self._player_x -= 1

    def move_right(self):
        if self._player_x < self._maze._num_cols and not self._maze._cells[self._player_x][self._player_y].has_right_wall:
            self._canvas.move(self._player._shape, self._player._cell_size, 0)
            self._player_x += 1

    def move_up(self):
        if self._player_y > 0 and not self._maze._cells[self._player_x][self._player_y].has_top_wall:
            self._canvas.move(self._player._shape, 0, -self._player._cell_size)
            self._player_y -= 1

    def move_down(self):
        if self._player_y < self._maze._num_rows and not self._maze._cells[self._player_x][self._player_y].has_bottom_wall:
            self._canvas.move(self._player._shape, 0, self._player._cell_size)
            self._player_y += 1

