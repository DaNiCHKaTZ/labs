import tkinter as tk
from tkinter import colorchooser
import random
import math
import matplotlib.pyplot as plt
import numpy as np
class MosaicApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mosaic Generator")
        
        self.width = tk.Entry(root)
        self.height = tk.Entry(root)
        self.colors = []
        self.block_size = tk.IntVar()
        self.canvas = None
        self.mosaic = None
        
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
        
        tk.Button(self.root, text="To Negative", command=self.to_negative).grid(row=5, column=0, columnspan=4)
        tk.Button(self.root, text="To Grayscale", command=self.to_grayscale).grid(row=6, column=0, columnspan=4)
        tk.Button(self.root, text="To Binary", command=self.to_binary).grid(row=7, column=0, columnspan=4)
        tk.Button(self.root, text="Brightness change", command=self.bright_change).grid(row=8, column=0, columnspan=4)
        tk.Button(self.root, text="Brightness Histogram", command=self.calculate_brightness_histogram).grid(row=9, column=0, columnspan=4)
        tk.Button(self.root, text="Log Compression", command=self.log_compression).grid(row=14, column=0, columnspan=4)
        tk.Button(self.root, text="Linear Stretch", command=self.linear_stretch).grid(row=15, column=0, columnspan=4)


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
        
        if self.canvas:
            self.canvas.destroy()
        
        self.canvas = tk.Canvas(self.root, width=width*block_size, height=height*block_size)
        self.canvas.grid(row=10, column=0, columnspan=4)
        
        self.mosaic = []
        for y in range(0, height*block_size, block_size):
            row = []
            for x in range(0, width*block_size, block_size):
                color = random.choice(self.colors)
                row.append(self.canvas.create_rectangle(x, y, x+block_size, y+block_size, fill=color))
            self.mosaic.append(row)
    
    def apply_filter(self, filter_func):
        if self.mosaic:
            for row in self.mosaic:
                for rect_id in row:
                    color = self.canvas.itemcget(rect_id, "fill")
                    new_color = filter_func(color)
                    self.canvas.itemconfig(rect_id, fill=new_color)
    
    def to_negative(self):
        self.apply_filter(self.to_negative_color)
    
    def to_grayscale(self):
        self.apply_filter(self.to_grayscale_color)
    
    def to_binary(self):
        self.apply_filter(self.to_binary_color)
    
    def bright_change(self):
        self.apply_filter(self.bright_change_color)
    
    def log_compression(self):
        self.apply_filter(self.log_compression_color)

    def log_compression_color(self, color):
        color = color.lstrip('#')
        rgb = [int(color[i:i+2], 16) for i in range(0, 6, 2)]
        c = 255 / np.log(1 + np.max(rgb))
        new_rgb = [c * np.log(1 + x) for x in rgb]
        return '#' + ''.join('{:02x}'.format(int(x)) for x in new_rgb)


    def to_negative_color(self, color):
        color = color.lstrip('#')
        rgb = [int(color[i:i+2], 16) for i in range(0, 6, 2)]
        negative = [255 - x for x in rgb]
        return '#' + ''.join('{:02x}'.format(x) for x in negative)

    def to_grayscale_color(self, color):
        color = color.lstrip('#')
        rgb = [int(color[i:i+2], 16) for i in range(0, 6, 2)]
        gray = int(0.3 * rgb[0] + 0.59 * rgb[1] + 0.11 * rgb[2])
        return '#' + '{:02x}'.format(gray) * 3

    def to_binary_color(self, color, threshold=128):
        color = color.lstrip('#')
        rgb = [int(color[i:i+2], 16) for i in range(0, 6, 2)]
        gray = int(sum(rgb) / 3)
        binary = 0 if gray < threshold else 255
        return '#' + '{:02x}'.format(binary) * 3

    def bright_change_color(self, color):
        color = color.lstrip('#')
        rgb = [int(color[i:i+2], 16) for i in range(0, 6, 2)]
        c = 40
        rgb_new = [c * math.log(1 + i) for i in rgb]
        return '#' + ''.join('{:02x}'.format(int(x)) for x in rgb_new)


    def calculate_brightness_histogram(self):
        if self.mosaic:
            brightness_values = []
            for row in self.mosaic:
                for rect_id in row:
                    color = self.canvas.itemcget(rect_id, "fill")
                  
                    gray_value = int(self.to_grayscale_color(color)[1:3], 16) 
                    brightness_values.append(gray_value)

            plt.figure()
            plt.hist(brightness_values, bins=range(256), color='gray', edgecolor='black', alpha=0.7)
            plt.title('Brightness Histogram')
            plt.xlabel('Brightness')
            plt.ylabel('Frequency')
            plt.grid(axis='y', alpha=0.75)
            plt.show()
    def linear_stretch(self):
        self.apply_filter(self.linear_stretch_color)

    def linear_stretch_color(self, color):
        color = color.lstrip('#')
        rgb = [int(color[i:i+2], 16) for i in range(0, 6, 2)]
        min_val = min(rgb)
        max_val = max(rgb)
        new_rgb = [(x - min_val) * 255 // (max_val - min_val) for x in rgb]
        return '#' + ''.join('{:02x}'.format(int(x)) for x in new_rgb)




if __name__ == "__main__":
    root = tk.Tk()
    app = MosaicApp(root)
    root.mainloop()