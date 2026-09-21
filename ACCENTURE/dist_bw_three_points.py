import math

# Find the total of the three straight-line distances between three points.
# distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)


def distance_between(point_a, point_b):
    """Return the straight-line distance between two (x, y) points."""
    x_difference = point_b[0] - point_a[0]
    y_difference = point_b[1] - point_a[1]
    return math.sqrt(x_difference**2 + y_difference**2)


def total_pairwise_distance(point_1, point_2, point_3):
    """Add the distances 1-2, 2-3, and 1-3."""
    distance_1_to_2 = distance_between(point_1, point_2)
    distance_2_to_3 = distance_between(point_2, point_3)
    distance_1_to_3 = distance_between(point_1, point_3)
    return distance_1_to_2 + distance_2_to_3 + distance_1_to_3


print(total_pairwise_distance((1, 1), (2, 4), (3, 6)))
