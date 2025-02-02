import random

class Game:
    def __init__(self, canvas, maze, player):
        self._canvas = canvas
        self._maze = maze
        self._player = player
        self._player_x = self._player._x
        self._player_y = self._player._y
        self.deadends = []
        self.enemy_path_stack = []
    
    def move_left(self):
        if self._player_x > 0 and not self._maze._cells[self._player_x][self._player_y].has_left_wall:
            self._canvas.move(self._player._shape, -self._player._cell_size, 0)
            self._player_x -= 1

    def move_right(self):
        if self._player_x < self._maze._num_cols - 1 and not self._maze._cells[self._player_x][self._player_y].has_right_wall:
            self._canvas.move(self._player._shape, self._player._cell_size, 0)
            self._player_x += 1

    def move_up(self):
        if self._player_y > 0 and not self._maze._cells[self._player_x][self._player_y].has_top_wall:
            self._canvas.move(self._player._shape, 0, -self._player._cell_size)
            self._player_y -= 1

    def move_down(self):
        if self._player_y < self._maze._num_rows - 1 and not self._maze._cells[self._player_x][self._player_y].has_bottom_wall:
            self._canvas.move(self._player._shape, 0, self._player._cell_size)
            self._player_y += 1

    def find_deadends(self):
        for i in range(self._maze._num_cols):
            for j in range(self._maze._num_rows):
                if self._maze._cells[i][j].count_walls() == 3:
                    self.deadends.append((i,j))
    
    def choose_deadend(self):
        return self.deadends[random.randrange(len(self.deadends))]
    
    def initialise_enemy(self, x, y):
        self.enemy_path_stack = [[x, y]]
        self.after(100, self.enemy_move)

    def find_enemy_moves(self, i, j):
        pass

    def enemy_move(self, enemy):
        if not self.enemy_path_stack:
            return
        
        i, j = self.enemy_path_stack[-1]
        self._canvas.update()
        self._maze._cells[i][j].enemy_visits += 1
        if i == j == 0:
            return
        #if i > 0 and 