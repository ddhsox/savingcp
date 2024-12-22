import colorsys


# Функции для преобразования между HEX, RGB и HSL
def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    length = len(hex_color)
    if length == 3:
        hex_color = ''.join([c * 2 for c in hex_color])  # #fff -> #ffffff
    return tuple(int(hex_color[i:i + 2], 16) for i in (0, 2, 4))


def rgb_to_hex(r, g, b):
    return f"#{r:02x}{g:02x}{b:02x}"


def rgb_to_hsl(r, g, b):
    r, g, b = r / 255.0, g / 255.0, b / 255.0
    return colorsys.rgb_to_hls(r, g, b)


def hsl_to_rgb(h, s, l):
    r, g, b = colorsys.hls_to_rgb(h, l, s)
    return int(r * 255), int(g * 255), int(b * 255)


# Функция для преобразования строки цвета в различные форматы
def convert_color(color):
    # Если цвет в формате HEX
    if color.startswith("#"):
        hex_color = color
        rgb_color = hex_to_rgb(hex_color)
        hsl_color = rgb_to_hsl(*rgb_color)
    # Если цвет в формате RGB
    elif color.startswith("RGB"):
        rgb_color = tuple(map(int, color[4:-1].split(',')))
        hex_color = rgb_to_hex(*rgb_color)
        hsl_color = rgb_to_hsl(*rgb_color)
    # Если цвет в формате RGBA
    elif color.startswith("rgba"):
        rgb_color = tuple(map(int, color[5:-1].split(',')[:3]))
        hex_color = rgb_to_hex(*rgb_color)
        hsl_color = rgb_to_hsl(*rgb_color)
    else:
        raise ValueError("Unknown color format")

    return hex_color, rgb_color, hsl_color