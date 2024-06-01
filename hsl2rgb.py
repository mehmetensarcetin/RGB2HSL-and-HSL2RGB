import numpy as np

def hsl2rgb(h, s, l):
    s /= 100
    l /= 100
    c = (1 - abs(2 * l - 1)) * s
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = l - c / 2

    if 0 <= h < 60:
        rp, gp, bp = c, x, 0
    elif 60 <= h < 120:
        rp, gp, bp = x, c, 0
    elif 120 <= h < 180:
        rp, gp, bp = 0, c, x
    elif 180 <= h < 240:
        rp, gp, bp = 0, x, c
    elif 240 <= h < 300:
        rp, gp, bp = x, 0, c
    else:
        rp, gp, bp = c, 0, x

    r = (rp + m) * 255
    g = (gp + m) * 255
    b = (bp + m) * 255

    return int(r), int(g), int(b)

# Örnek kullanım:
h, s, l = 0, 100, 50  # Kırmızı renk
r, g, b = hsl2rgb(h, s, l)
print(f"Kırmızı: {r}, Yeşil: {g}, Mavi: {b}")
