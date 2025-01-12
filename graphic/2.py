import tkinter as tk 
from tkinter import filedialog
import struct
from PIL import Image

def read_file_as_bytearray(file_path):
    with open(file_path, 'rb') as file:
        byte_array = []
        byte = file.read(1)
        while byte:
            byte_array.append(byte[0])
            byte = file.read(1)
    
    return byte_array

def read_bmp(file_path):
    with open(file_path, 'rb') as file:
        header = file.read(54)
        width = struct.unpack('<i', header[18:22])[0]
        height = struct.unpack('<i', header[22:26])[0]
        
        file.seek(54)
        pixels = file.read()

        print(f"Изображение шириной {width} пикселей и высотой {height} пикселей успешно открыто.")

        red_pixels = green_pixels = blue_pixels = 0
        img_pixels = bytearray()
        for i in range(0, len(pixels), 3):
            blue = pixels[i]
            green = pixels[i+1]
            red = pixels[i+2]
            img_pixels.extend([red, green, blue])  
            if red > green and red > blue:
                red_pixels += 1
            elif green > red and green > blue:
                green_pixels += 1
            elif blue > red and blue > green:
                blue_pixels += 1

        print(f"Количество красных пикселей: {red_pixels}")
        print(f"Количество зеленых пикселей: {green_pixels}")
        print(f"Количество синих пикселей: {blue_pixels}")

        img = Image.frombytes("RGB", (width, height), bytes(img_pixels))
        img = img.transpose(Image.FLIP_TOP_BOTTOM)  
        img.show()

def save_bmp(file_path, width, height, pixels):
    with open(file_path, 'wb') as file:
        header = bytearray(b'BM')
        header += struct.pack('<i', 54 + len(pixels))
        header += b'\x00\x00\x00\x00'
        header += b'\x36\x00\x00\x00'
        header += b'\x28\x00\x00\x00'
        header += struct.pack('<i', width)
        header += struct.pack('<i', height)
        header += b'\x01\x00'
        header += b'\x18\x00'
        header += b'\x00\x00\x00\x00'
        header += struct.pack('<i', len(pixels))
        header += b'\x13\x0B\x00\x00'
        header += b'\x13\x0B\x00\x00'
        header += b'\x00\x00\x00\x00'
        header += b'\x00\x00\x00\x00'
        
        file.write(header)
        file.write(pixels)

def open_file_dialog():
    file_path = filedialog.askopenfilename(filetypes=[("Bitmap files", "*.bmp")])
    if file_path:
        read_bmp(file_path)

def save_file_dialog():
    file_path = filedialog.asksaveasfilename(defaultextension=".bmp", filetypes=[("Bitmap files", "*.bmp")])
    if file_path:
        pixels = bytearray(b'\xFF\x00\x00' * 100)  
        save_bmp(file_path, 100, 1, pixels)  

root = tk.Tk()
root.title("BMP Editor")

open_button = tk.Button(root, text="Open BMP", command=open_file_dialog)
open_button.pack()

save_button = tk.Button(root, text="Save BMP", command=save_file_dialog)
save_button.pack()

root.mainloop()