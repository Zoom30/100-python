import math
def square_areas_difference(r: int):
    area_of_big_square = math.pow(2 * r, 2)
    area_of_small_square = math.pow(math.sqrt(math.pow(2 * r, 2) /2), 2)
    return round(area_of_big_square - area_of_small_square, 0)



print(square_areas_difference(5))