from PIL import Image
import numpy as np

def bilinear_interpolation(x, y, img):
    x1, y1 = int(x), int(y)
    x2, y2 = min(x1 + 1, img.shape[1] - 1), min(y1 + 1, img.shape[0] - 1)

    if x2 - x1 != 0:
        r1 = ((x2 - x) / (x2 - x1) * img[y1, x1] + (x - x1) / (x2 - x1) * img[y1, x2])
        r2 = ((x2 - x) / (x2 - x1) * img[y2, x1] + (x - x1) / (x2 - x1) * img[y2, x2])
    else:
        r1 = img[y1, x1]
        r2 = img[y2, x1]

    if y2 - y1 != 0:
        return ((y2 - y) / (y2 - y1) * r1 + (y - y1) / (y2 - y1) * r2)
    else:
        return r1


def nearest_neighbor_rescale(image, scale):
    old_height, old_width = image.shape[0], image.shape[1]
    new_height, new_width = int(old_height * scale), int(old_width * scale)

    new_image = np.zeros((new_height, new_width, image.shape[2]))

    for i in range(new_height):
        for j in range(new_width):
            y, x = min(int(old_height * i / new_height), old_height - 1), min(int(old_width * j / new_width), old_width - 1)
            new_image[i, j] = image[y, x]

    return new_image


def bilinear_rescale(image, scale):
    old_height, old_width = image.shape[:2]
    new_height, new_width = int(old_height * scale), int(old_width * scale)

    new_image = np.zeros((new_height, new_width, image.shape[2]))

    for i in range(new_height):
        for j in range(new_width):
            y, x = i / scale, j / scale
            new_image[i, j] = bilinear_interpolation(x, y, image)

    return new_image

image_path = "example.bmp"
image = Image.open(image_path)
image = np.array(image)

# nrighbor_img = nearest_neighbor_rescale(image, 0.5)
# nrighbor_img_pil = Image.fromarray(nrighbor_img.astype('uint8'))
# nrighbor_img_pil.show()

# nrighbor_img1 = nearest_neighbor_rescale(image, 2)
# nrighbor_img_pil1 = Image.fromarray(nrighbor_img1.astype('uint8'))
# nrighbor_img_pil1.show()

b_img = bilinear_rescale(image, 0.5)
b_img_pil = Image.fromarray(b_img.astype('uint8'))
b_img_pil.show()

b_img = bilinear_rescale(image, 2)
b_img_pil = Image.fromarray(b_img.astype('uint8'))
b_img_pil.show()

#
