from tkinter import Tk, BOTH, Canvas
import time
import random
class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.geometry(f"{width}x{height}")
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.running = True

        self.canvas = Canvas(self.__root, bg="black", width=width, height=height)
        self.canvas.pack(fill=BOTH, expand=True)


    def close(self):
        if self.running:
            self.running = False
            self.__root.quit()
            self.__root.destroy()

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        while self.running:
            self.redraw()
    
    def draw_line(self, line, color="white"):
        line.draw(self.canvas, color=color)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, point, point2):
        self.pointx = point.x
        self.pointy = point.y
        self.point2x = point2.x
        self.point2y = point2.y

    def draw(self, canvas, color="white"):
        canvas.create_line( self.pointx, self.pointy, self.point2x, self.point2y, fill=color, width=2)

class Cell:
    def __init__(self, window=None):
        self.__win = window
        self.has_left_wall = True
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.visited = False

    def draw(self, x, y, width, height):
        self.__x1 = x
        self.__y1 = y
        self.__x2 = x + width
        self.__y2 = y + height
        if self.has_left_wall:
            line = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
            if self.__win:
                self.__win.draw_line(line)
        elif not self.has_left_wall:
            line = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
            if self.__win:
                self.__win.draw_line(line, color="green")

        if self.has_top_wall:
            line = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
            if self.__win:
                self.__win.draw_line(line)
        elif not self.has_top_wall:
            line = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
            if self.__win:
                self.__win.draw_line(line, color="green")

        if self.has_right_wall:
            line = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
            if self.__win:
                self.__win.draw_line(line)
        elif not self.has_right_wall:
            line = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
            if self.__win:
                self.__win.draw_line(line, color="green")

        if self.has_bottom_wall:
            line = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
            if self.__win:
                self.__win.draw_line(line)
        elif not self.has_bottom_wall:
            line = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
            if self.__win:
                self.__win.draw_line(line, color="green")

    def get_center(self):
        return Point(((self.__x2 + self.__x1) / 2), ((self.__y2 + self.__y1) / 2))
    
    def draw_move(self, to_cell, undo=False):
        center_to_cell = to_cell.get_center()
        center_cell = self.get_center()
        if undo:
            line = Line(center_to_cell, center_cell)
            if self.__win:
                self.__win.draw_line(line, color="gray")
            
        else:
            line = Line(center_cell, center_to_cell)
            if self.__win:
                self.__win.draw_line(line, color="red")




class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.__seed = seed
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win
        self.__cells = []
        self.__create_cells()
        self.__break_entrance_and_exit()
        if self.__seed:
            random.seed(seed)
        self.__break_walls_r(0, 0)
    
    def __create_cells(self):
        for i in range(self.__num_cols):
            column = []
            for j in range(self.__num_rows):
                cell = Cell(self.__win)
                cell.has_left_wall = True
                cell.has_top_wall = True
                cell.has_right_wall = True
                cell.has_bottom_wall = True
                column.append(cell)
            self.__cells.append(column)
        for i in range(self.__num_cols):
            for j in range(self.__num_rows):
                self.__draw_cell(column=i, row=j)
    
    def __draw_cell(self, column, row):
        cell = self.__cells[column][row]
        cell.draw(self.__x1 + (column * self.__cell_size_x), self.__y1 + (row * self.__cell_size_y), self.__cell_size_x, self.__cell_size_y)
        self.animate()
    
    def animate(self):
        if self.__win:
            self.__win.redraw()
        time.sleep(0.0333)  # 30 FPS

    def __break_entrance_and_exit(self):
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)
        self.__cells[self.__num_cols - 1][self.__num_rows - 1].has_bottom_wall = False
        self.__draw_cell(self.__num_cols - 1, self.__num_rows - 1)
    
    def __break_walls_r(self, i, j):
        self.__cells[i][j].visited = True
        while True:
            need_to_visit = []
            if i > 0 and not self.__cells[i - 1][j].visited:
                need_to_visit.append((i - 1, j))
            if i < len(self.__cells) - 1 and not self.__cells[i + 1][j].visited:
                need_to_visit.append((i + 1, j))
            if j > 0 and not self.__cells[i][j - 1].visited:
                need_to_visit.append((i, j - 1))
            if j < len(self.__cells[0]) - 1 and not self.__cells[i][j + 1].visited:
                need_to_visit.append((i, j + 1))
            if not need_to_visit:
                self.__draw_cell(i, j)
                return
            next_cell = random.choice(need_to_visit)
            next_i, next_j = next_cell
            next_cell = self.__cells[next_i][next_j]
            current_cell = self.__cells[i][j]
            if next_i < i:
                current_cell.has_left_wall = False
                next_cell.has_right_wall = False
            elif next_i > i:
                current_cell.has_right_wall = False
                next_cell.has_left_wall = False
            elif next_j < j:
                current_cell.has_top_wall = False
                next_cell.has_bottom_wall = False
            elif next_j > j:
                current_cell.has_bottom_wall = False
                next_cell.has_top_wall = False
            next_cell.draw_move(current_cell, undo=False)
            self.__break_walls_r(next_i, next_j)    







            
win = Window(800, 600)
maze = Maze(50, 50, 10, 10, 50, 50, win)
# Keep the window open until closed
win.wait_for_close()