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
        line.draw(self.canvas, fill=color)

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

            
win = Window(800, 600)
line1 = Line(Point(100, 100), Point(200, 200))
line2 = Line(Point(200, 100), Point(100, 200))
win.draw_line(line1, "red")
win.draw_line(line2, "blue")
win.redraw()
# Keep the window open until closed
win.wait_for_close()