import numpy as np
def determinant(matrix):
    if len(matrix) == 1:
        return matrix[0]
    elif len(matrix) == 2:
        return ((matrix[0][0] * matrix[1][1]) - (matrix [0][1] * matrix[1][0]))
    # m2 = [ 
    #     [2,5,3], 
    #     [1,-2,-1], 
    #     [1, 3, 4]
    #     ]
    # matrix = m2

    else:
        return (round(np.linalg.det(np.array(matrix))))

print(determinant([[2,5,3], [1,-2,-1], [1, 3, 4]]))