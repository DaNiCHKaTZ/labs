import tkinter as tk
from tkinter import colorchooser
import random
import math

class MosaicApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mosaic Generator")
        
        self.width = tk.Entry(root)
        self.height = tk.Entry(root)
        self.colors = []
        self.block_size = tk.IntVar()
        self.angle = 0  
        
        self.create_widgets()
    
    def create_widgets(self):
        tk.Label(self.root, text="Width:").grid(row=0, column=0)
        self.width.grid(row=0, column=1)
        
        tk.Label(self.root, text="Height:").grid(row=1, column=0)
        self.height.grid(row=1, column=1)
        
        tk.Button(self.root, text="Select Colors", command=self.select_colors).grid(row=2, column=0, columnspan=2)
        
        tk.Label(self.root, text="Block Size:").grid(row=3, column=0)
        tk.Radiobutton(self.root, text="2x2", variable=self.block_size, value=2).grid(row=3, column=1)
        tk.Radiobutton(self.root, text="4x4", variable=self.block_size, value=4).grid(row=3, column=2)
        tk.Radiobutton(self.root, text="8x8", variable=self.block_size, value=8).grid(row=3, column=3)
        
        tk.Button(self.root, text="Generate Mosaic", command=self.generate_mosaic).grid(row=4, column=0, columnspan=4)
        
        tk.Button(self.root, text="Rotate 90", command=self.rotate_90).grid(row=5, column=0, columnspan=2)
        tk.Button(self.root, text="Rotate 45", command=self.rotate_45).grid(row=5, column=2, columnspan=2)
    
    def select_colors(self):
        self.colors = []
        for _ in range(4):
            color = colorchooser.askcolor()[1]
            self.colors.append(color)
    
    def generate_mosaic(self):
        try:
            width = int(self.width.get())
            height = int(self.height.get())
            block_size = self.block_size.get()
            
            self.canvas = tk.Canvas(self.root, width=width*block_size, height=height*block_size)
            self.canvas.grid(row=6, column=0, columnspan=4)
            
            for y in range(0, height*block_size, block_size):
                for x in range(0, width*block_size, block_size):
                    color = random.choice(self.colors)
                    self.canvas.create_rectangle(x, y, x+block_size, y+block_size, fill=color)
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter valid width and height.")
    
    def rotate_90(self):
        self.angle += 90  
        self.rotate()
    
    def rotate_45(self):
        self.angle += 45  
        self.rotate()
    
    def rotate(self):
        angle = math.radians(self.angle)
        cos_val = math.cos(angle)
        sin_val = math.sin(angle)
        

        width = int(self.width.get())
        height = int(self.height.get())
        block_size = self.block_size.get()
        

        canvas = tk.Canvas(self.root, width=width*block_size, height=height*block_size)
        canvas.grid(row=6, column=0, columnspan=4)
        

        cx = width * block_size // 2
        cy = height * block_size // 2
        
        for y in range(0, height*block_size, block_size):
            for x in range(0, width*block_size, block_size):
             
                tx = x - cx
                ty = y - cy
                
              
                rx = tx * cos_val - ty * sin_val
                ry = tx * sin_val + ty * cos_val
                
             
                nx = rx + cx
                ny = ry + cy
                
         
                color = random.choice(self.colors)
                canvas.create_rectangle(nx, ny, nx+block_size, ny+block_size, fill=color)

if __name__ == "__main__":
    root = tk.Tk()
    app = MosaicApp(root)
    root.mainloop()
