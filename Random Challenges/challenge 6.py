def rgb(r, g, b):
    color_value = list((r, g, b))

    for value in color_value:
        if value <= 0:
            color_value[color_value.index(value)] = 0
        elif value > 255:
            color_value[color_value.index(value)] = 255
    x = tuple(color_value)

    return f"{'%02x%02x%02x' % x}".upper()
    
print(rgb(-20,275,125))