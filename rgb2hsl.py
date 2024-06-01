import numpy as np

def rgb2hsl(r, g, b):
    r /= 255.0
    g /= 255.0
    b /= 255.0
    
    c_max = np.max([r, g, b])
    c_min = np.min([r, g, b])
    delta = c_max - c_min
    
    # Renk tonu hesaplama
    if delta == 0:
        h = 0
    elif c_max == r:
        h = ((g - b) / delta) % 6
    elif c_max == g:
        h = (b - r) / delta + 2
    else:
        h = (r - g) / delta + 4
    
    h *= 60
    
    # Parlaklık hesaplama
    l = (c_max + c_min) / 2
    
    # Doygunluk hesaplama
    if delta == 0:
        s = 0
    else:
        s = delta / (1 - abs(2 * l - 1))
    
    return h, s * 100, l * 100

# Örnek kullanım:
r, g, b = 255, 0, 0  # Kırmızı renk
h, s, l = rgb2hsl(r, g, b)
print(f"Renk Tonu: {h}, Doygunluk: {s}%, Parlaklık: {l}%")
