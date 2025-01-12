import colorsys

def rgb_to_cmyk(r, g, b):
    c = 1 - r / 255
    m = 1 - g / 255
    y = 1 - b / 255
    k = min(c, m, y)
    if k == 1:
        return 0, 0, 0, 1
    return (c - k) / (1 - k), (m - k) / (1 - k), (y - k) / (1 - k), k

def cmyk_to_rgb(c, m, y, k):
    r = (1 - c) * (1 - k) * 255
    g = (1 - m) * (1 - k) * 255
    b = (1 - y) * (1 - k) * 255
    return int(r), int(g), int(b)

def lab_to_hsb(l, a, b):
    
    l = l / 100
    a = (a + 128) / 255
    b = (b + 128) / 255

    # Конвертируем Lab в RGB
    x = (l + 16) / 116
    y = a / 500 + x
    z = x - b / 200
    y = y ** 3 if y ** 3 <= 0.008856 else y
    x = x ** 3 if x ** 3 <= 0.008856 else x
    z = z ** 3 if z ** 3 <= 0.008856 else z
    x = x * 0.95047 if x * 0.95047 <= 0.008856 else x
    y = y * 1.00000 if y * 1.00000 <= 0.008856 else y
    z = z * 1.08883 if z * 1.08883 <= 0.008856 else z

    r = x * 3.2406 - y * 1.5372 - z * 0.4986
    g = -x * 0.9689 + y * 1.8758 + z * 0.0415
    b = x * 0.0557 - y * 0.2040 + z * 1.0570

    # Конвертируем RGB в HSB
    r = max(0, min(1, r))
    g = max(0, min(1, g))
    b = max(0, min(1, b))
    h, s, v = colorsys.rgb_to_hsv(r, g, b)

    return h * 360, s * 100, v * 100

def hsb_to_lab(h, s, v):
    # Конвертируем HSB в RGB
    r, g, b = colorsys.hsv_to_rgb(h / 360, s / 100, v / 100)

    # Конвертируем RGB в Lab
    x = r * 0.4124564 + g * 0.3575761 + b * 0.1804375
    y = r * 0.2126729 + g * 0.7151522 + b * 0.0721750
    z = r * 0.0193339 + g * 0.1191920 + b * 0.9503041

    x = x / 0.95047 if x > 0.008856 else (x / 903.3 + 16) / 116
    y = y / 1.00000 if y > 0.008856 else (y / 903.3 + 16) / 116
    z = z / 1.08883 if z > 0.008856 else (z / 903.3 + 16) / 116

    l = max(0, min(100, 116 * y - 16))
    a = max(-128, min(127, 500 * (x - y)))
    b = max(-128, min(127, 200 * (y - z)))

    return l, a, b

# Пример использования
h, s, v = 0, 100, 100
l, a, b = hsb_to_lab(h, s, v)
print(f"HSB: ({h}, {s}, {v}) -> Lab: ({l}, {a}, {b})")

l, a, b = 50, 0, 0
h, s, v = lab_to_hsb(l, a, b)
print(f"Lab: ({l}, {a}, {b}) -> HSB: ({h}, {s}, {v})")

r, g, b = 255, 255, 0
c, m, y, k = rgb_to_cmyk(r, g, b)
print(f"RGB: ({r}, {g}, {b}) -> CMYK: ({c}, {m}, {y}, {k})")

c = 0
m = 1
y = 1
k = 0
r, g, b = cmyk_to_rgb(c, m, y, k)
print(f"CMYK: ({c}, {m}, {y}, {k}) -> RGB: ({r}, {g}, {b})")
