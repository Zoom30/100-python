# The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

# Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

# The following are examples of expected output values:

# rgb(255, 255, 255) # returns FFFFFF
# rgb(255, 255, 300) # returns FFFFFF
# rgb(0,0,0) # returns 000000
# rgb(148, 0, 211) # returns 9400D3

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