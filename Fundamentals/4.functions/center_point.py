x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

import math


def closest_point(x1, y1, x2, y2):
    # Calculate the distance of both points from the origin (0, 0)
    distance1 = math.sqrt(x1 ** 2 + y1 ** 2)  # distance is sqrt(x^2 + y^2) разстояние
    distance2 = math.sqrt(x2 ** 2 + y2 ** 2)

    # Compare the distances and return the closest point
    if distance1 <= distance2:
        print(f"({math.floor(x1)}, {math.floor(y1)})")
    else:
        print(f"({math.floor(x2)}, {math.floor(y2)})")


closest_point(x1, y1, x2, y2)
