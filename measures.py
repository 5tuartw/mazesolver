class Maze():
    # ...existing code...

    def measure_metrics(self):
        shortest_path_length = len(self.find_shortest_path((0, 0), (self._num_cols - 1, self._num_rows - 1)))
        dead_end_count = self.count_dead_ends()
        branching_factor = self.calculate_branching_factor()
        corridor_length = self.calculate_corridor_length()
        solution_path_length = self.calculate_solution_path_length()
        maze_density = self.calculate_maze_density()

        return {
            "shortest_path_length": shortest_path_length,
            "dead_end_count": dead_end_count,
            "branching_factor": branching_factor,
            "corridor_length": corridor_length,
            "solution_path_length": solution_path_length,
            "maze_density": maze_density
        }

    def count_dead_ends(self):
        dead_end_count = 0
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                open_paths = 0
                if i > 0 and not self._cells[i][j].has_left_wall:
                    open_paths += 1
                if i < self._num_cols - 1 and not self._cells[i][j].has_right_wall:
                    open_paths += 1
                if j > 0 and not self._cells[i][j].has_top_wall:
                    open_paths += 1
                if j < self._num_rows - 1 and not self._cells[i][j].has_bottom_wall:
                    open_paths += 1
                if open_paths == 1:
                    dead_end_count += 1
        return dead_end_count

    def calculate_branching_factor(self):
        total_branches = 0
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                open_paths = 0
                if i > 0 and not self._cells[i][j].has_left_wall:
                    open_paths += 1
                if i < self._num_cols - 1 and not self._cells[i][j].has_right_wall:
                    open_paths += 1
                if j > 0 and not self._cells[i][j].has_top_wall:
                    open_paths += 1
                if j < self._num_rows - 1 and not self._cells[i][j].has_bottom_wall:
                    open_paths += 1
                total_branches += open_paths
        return total_branches / (self._num_cols * self._num_rows)

    def calculate_corridor_length(self):
        total_corridor_length = 0
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                if self.is_corridor(i, j):
                    total_corridor_length += 1
        return total_corridor_length / (self._num_cols * self._num_rows)

    def is_corridor(self, i, j):
        open_paths = 0
        if i > 0 and not self._cells[i][j].has_left_wall:
            open_paths += 1
        if i < self._num_cols - 1 and not self._cells[i][j].has_right_wall:
            open_paths += 1
        if j > 0 and not self._cells[i][j].has_top_wall:
            open_paths += 1
        if j < self._num_rows - 1 and not self._cells[i][j].has_bottom_wall:
            open_paths += 1
        return open_paths == 2

    def calculate_solution_path_length(self):
        solution_path = self.find_shortest_path((0, 0), (self._num_cols - 1, self._num_rows - 1))
        return len(solution_path)

    def calculate_maze_density(self):
        total_walls = 0
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                if self._cells[i][j].has_left_wall:
                    total_walls += 1
                if self._cells[i][j].has_right_wall:
                    total_walls += 1
                if self._cells[i][j].has_top_wall:
                    total_walls += 1
                if self._cells[i][j].has_bottom_wall:
                    total_walls += 1
        return total_walls / (self._num_cols * self._num_rows * 4)

    # ...existing code...