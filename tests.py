import unittest
from window import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._Maze__cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._Maze__cells[0]),
            num_rows,
        )
    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._Maze__break_entrance_and_exit()
        self.assertFalse(m1._Maze__cells[0][0].has_top_wall)
        self.assertFalse(m1._Maze__cells[num_cols - 1][num_rows - 1].has_bottom_wall)
    
    def test_maze_break_walls_r(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._Maze__reset_cells_visited()
        m1._Maze__break_walls_r(0, 0)
        # Check that the first cell is visited
        self.assertTrue(m1._Maze__cells[0][0].visited)
        # Check that the last cell is visited
        self.assertTrue(m1._Maze__cells[num_cols - 1][num_rows - 1].visited)
    
    def test_maze_reset_cells_visited(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        m1._Maze__reset_cells_visited()
        # Check that all cells are not visited
        for column in m1._Maze__cells:
            for cell in column:
                self.assertFalse(cell.visited)


if __name__ == "__main__":
    unittest.main()