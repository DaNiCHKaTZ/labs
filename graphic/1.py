import tkinter as tk
from tkinter import colorchooser
import random
import matplotlib.pyplot as plt

class MosaicApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mosaic Generator")
        
        self.width = tk.Entry(root)
        self.height = tk.Entry(root)
        self.colors = []
        self.block_size = tk.IntVar()
        
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
        
        tk.Button(self.root, text="To Negative", command=lambda: self.to_transform(self.to_negative)).grid(row=5, column=0, columnspan=4)
        tk.Button(self.root, text="To Grayscale", command=lambda: self.to_transform(self.to_grayscale)).grid(row=6, column=0, columnspan=4)
        tk.Button(self.root, text="To Binary", command=lambda: self.to_transform(self.to_binary)).grid(row=7, column=0, columnspan=4)
    
    def select_colors(self):
        self.colors = []
        for _ in range(4):
            color = colorchooser.askcolor()[1]
            self.colors.append(color)
    
    def generate_mosaic(self):
        if not self.colors:
            return
        width = int(self.width.get())
        height = int(self.height.get())
        block_size = self.block_size.get()
        
        canvas = tk.Canvas(self.root, width=width*block_size, height=height*block_size)
        canvas.grid(row=8, column=0, columnspan=4)
        
        for y in range(0, height*block_size, block_size):
            for x in range(0, width*block_size, block_size):
                color = random.choice(self.colors)
                for transform in [self.to_negative, self.to_grayscale, self.to_binary]:
                    color = transform(color)
                canvas.create_rectangle(x, y, x+block_size, y+block_size, fill=color)
    
    def to_transform(self, transform_func):
        for i in range(len(self.colors)):
            self.colors[i] = transform_func(self.colors[i])
    
def to_negative(self, color):
color = color.lstrip('#')
rgb = [int(color[i:i+2], 16) for i in range(0, 6, 2)]
negative = [255 - x for x in rgb]
return '#' + ''.join('{:02x}'.format(x) for x in negative)

def to_grayscale(self, color):
color = color.lstrip('#')
rgb = [int(color[i:i+2], 16) for i in range(0, 6, 2)]
gray = int(0.2126 * rgb[0] + 0.7152 * rgb[1] + 0.0722 * rgb[2])
return '#' + '{:02x}'.format(gray) * 3

def to_binary(self, color, threshold=128):
color = color.lstrip('#')
rgb = [int(color[i:i+2], 16) for i in range(0, 6, 2)]
gray = int(sum(rgb) / 3)
binary = 0 if gray < threshold else 255
return '#' + '{:02x}'.format(binary) * 3

if __name__ == "__main__":
    root = tk.Tk()
    app = MosaicApp(root)
    root.mainloop()