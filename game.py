import random

class Game:
    def __init__(self, canvas, maze, player, enemy):
        self._canvas = canvas
        self._maze = maze
        self._player = player
        self._player_x = self._player._x
        self._player_y = self._player._y
        self._enemy = enemy
        self.deadends = []
        self.enemy_path_stack = []
        self._running = True
        
    
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
    
    def start_enemy_movement(self):
        self._running = True
        self.schedule_enemy_move()
    
    def stop_enemy_movement(self):
        self._running = False
    
    def schedule_enemy_move(self):
        if self._running:
            self.enemy_move(self._enemy)
            self._canvas.after(1000, self.schedule_enemy_move)

    def find_enemy_moves(self, i, j):
        #check each direction and add to list
        available_moves = []
        #check left
        if i > 0 and not self._maze._cells[i][j].has_left_wall:
            available_moves.append(("left", self._maze._cells[i-1][j].enemy_visits))
        #check right
        if i < self._maze._num_cols - 1 and not self._maze._cells[i][j].has_right_wall:
            available_moves.append(("right", self._maze._cells[i+1][j].enemy_visits))
        #check up
        if j > 0 and not self._maze._cells[i][j].has_top_wall:
            available_moves.append(("up", self._maze._cells[i][j-1].enemy_visits))
        #check down
        if j < self._maze._num_rows - 1 and not self._maze._cells[i][j].has_bottom_wall:
            available_moves.append(("down", self._maze._cells[i][j+1].enemy_visits))
        print(available_moves)
        return available_moves
    
    def find_best_enemy_move(self, available_moves):
        if not available_moves:
            return None

        lowest_value = float('inf')
        lowest_moves = []

        for item in available_moves:
            if item[1] < lowest_value:
                lowest_value = item[1]
                lowest_moves = [item]
            elif item[1] == lowest_value:
                lowest_moves.append(item)
        
        if lowest_moves:
            return random.choice(lowest_moves)
        else:
            return None
            
    def enemy_move(self, enemy):
        current_x = enemy._x
        current_y = enemy._y
        while not(current_x == 0 and current_y == 0):
            if (current_x, current_y) in self.deadends:
                self._maze._cells[current_x][current_y].enemy_visits = 10
            else:
                self._maze._cells[current_x][current_y].enemy_visits += 1
            available_moves = self.find_enemy_moves(enemy._x, enemy._y)
            if available_moves == []:
                return None
            next_move = self.find_best_enemy_move(available_moves)

            if next_move[0] == "left":
                self._canvas.move(self._enemy._shape, -self._enemy._cell_size, 0)
                self._enemy._x -= 1
            if next_move[0] == "right":
                self._canvas.move(self._enemy._shape, self._enemy._cell_size, 0)
                self._enemy._x += 1
            if next_move[0] == "up":
                self._canvas.move(self._enemy._shape, 0, -self._enemy._cell_size)
                self._enemy._y -= 1
            if next_move[0] == "down":
                self._canvas.move(self._enemy._shape, 0, self._enemy._cell_size)
                self._enemy._y += 1
            break

