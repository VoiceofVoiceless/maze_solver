from tkinter import Tk, BOTH, Canvas

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
    def __init__(self, window):
        self.__win = window
        self.has_left_wall = True
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1

    def draw(self, x, y, width, height):
        self.__x1 = x
        self.__y1 = y
        self.__x2 = x + width
        self.__y2 = y + height
        if self.has_left_wall:
            line = Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
            self.__win.draw_line(line)
        if self.has_top_wall:
            line = Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
            self.__win.draw_line(line)
        if self.has_right_wall:
            line = Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
            self.__win.draw_line(line)
        if self.has_bottom_wall:
            line = Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
            self.__win.draw_line(line)

            
win = Window(800, 600)
line1 = Line(Point(100, 100), Point(200, 200))
line2 = Line(Point(200, 100), Point(100, 200))
win.draw_line(line1, "red")
win.draw_line(line2, "blue")
win.redraw()
cell = Cell(win)
cell.has_left_wall = True
cell.has_top_wall = True
cell.has_right_wall = True
cell.has_bottom_wall = True
cell.draw(100, 100, 50, 50)
cell2 = Cell(win)
cell2.has_left_wall = True
cell2.has_top_wall = True
cell2.has_right_wall = True
cell2.has_bottom_wall = True
cell2.draw(200, 100, 50, 50)
cell3 = Cell(win)
cell3.has_left_wall = True
cell3.has_top_wall = True
cell3.has_right_wall = True
cell3.has_bottom_wall = True
cell3.draw(100, 200, 50, 50)
win.redraw()
# Keep the window open until closed
win.wait_for_close()