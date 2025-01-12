import turtle

class FractalTree:
    def __init__(self):
        self.t = turtle.Turtle()
    
    def draw_tree(self, size, angle, level):
        if level == 0:
            return
        
        self.t.forward(size)
        self.t.left(angle)
        
        self.draw_tree(0.8 * size, angle, level-1)
        
        self.t.right(2 * angle)
        
        self.draw_tree(0.8 * size, angle, level-1)
        
        self.t.left(angle)
        
        self.t.backward(size)
    
    def draw_fractal(self, size, angle, level):
        turtle.speed(0)
        turtle.penup()
        turtle.goto(0, -turtle.window_height() / 2 + 50)
        turtle.pendown()
        self.t.setheading(90)
        
        self.draw_tree(size, angle, level)
        
        turtle.done()


































fractal_tree = FractalTree()
fractal_tree.draw_fractal(100, 30, 5)





