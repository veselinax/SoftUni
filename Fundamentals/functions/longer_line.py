import math


def distance(x1, y1, x2, y2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def closest_to_origin(x1, y1, x2, y2):
    """Return the point closer to the origin (0, 0)."""
    dist1 = math.sqrt(x1 ** 2 + y1 ** 2)
    dist2 = math.sqrt(x2 ** 2 + y2 ** 2)

    # Return the closer point first
    if dist1 <= dist2:
        return (x1, y1), (x2, y2)
    else:
        return (x2, y2), (x1, y1)


def print_line(x1, y1, x2, y2):
    """Print the line in the required format, starting with the point closer to the origin."""
    start, end = closest_to_origin(x1, y1, x2, y2)
    print(f"({math.floor(start[0])}, {math.floor(start[1])})({math.floor(end[0])}, {math.floor(end[1])})")


def longer_line(x1, y1, x2, y2, x3, y3, x4, y4):
    """Compare the lengths of two lines and print the longer one."""
    distance1 = distance(x1, y1, x2, y2)
    distance2 = distance(x3, y3, x4, y4)

    if distance1 >= distance2:
        print_line(x1, y1, x2, y2)
    else:
        print_line(x3, y3, x4, y4)


x1 = float(input())
x2 = float(input())
y1 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())


# Find and print the longer line
longer_line(x1, y1, x2, y2, x3, y3, x4, y4)
