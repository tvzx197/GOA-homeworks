import math

def find_next_square(sq):
    root = math.isqrt(sq)
    if root * root == sq:
        next_square = (root + 1) ** 2
        return next_square
    else:
        return -1