from PIL import Image
import numpy as np

def bilinear_interpolation(x, y, img):
    x1, y1 = int(x), int(y)
    x2, y2 = min(x1 + 1, img.shape[1] - 1), min(y1 + 1, img.shape[0] - 1)

    r1 = ((x2 - x) / (x2 - x1) * img[y1, x1] + (x - x1) / (x2 - x1) * img[y1, x2])
    r2 = ((x2 - x) / (x2 - x1) * img[y2, x1] + (x - x1) / (x2 - x1) * img[y2, x2])

    return ((y2 - y) / (y2 - y1) * r1 + (y - y1) / (y2 - y1) * r2)

def rotate_image(image, angle):
    angle = -angle 
    angle = np.radians(angle)
    cos_val = np.cos(angle)
    sin_val = np.sin(angle)
    width, height = image.shape[1], image.shape[0]
    new_height = int(round(abs(width*cos_val) + abs(height*sin_val)))
    new_width = int(round(abs(height*cos_val) + abs(width*sin_val)))
    new_image = np.zeros((new_height, new_width, image.shape[2]))

    for i in range(new_height):
        for j in range(new_width):
            y = (i - new_height/2)*cos_val - (j - new_width/2)*sin_val + height/2
            x = (i - new_height/2)*sin_val + (j - new_width/2)*cos_val + width/2

            if x >= 0 and y >= 0 and x < width and y < height:
                new_image[i, j] = bilinear_interpolation(x, y, image)

    return new_image

image_path = "example.bmp"
image = Image.open(image_path)
image = np.array(image)

rotated_image_90 = rotate_image(image, 90)
rotated_image_90_pil = Image.fromarray(rotated_image_90.astype('uint8'))
rotated_image_90_pil.show()

rotated_image_45 = rotate_image(image, 45)
rotated_image_45_pil = Image.fromarray(rotated_image_45.astype('uint8'))
rotated_image_45_pil.show()