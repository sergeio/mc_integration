from itertools import imap
from random import uniform


def monte_carlo_integrate(func, min_x, max_x, num_points=100):
    points = make_random_points((min_x, 0), (max_x, 1), num_points=num_points)
    return num_under_curve(func, points) / float(num_points)


def num_under_curve(func, coordinates):
    """# points in :param coordinates: falling under the curve :param func:."""
    def is_under_curve(xy):
        x, y = xy
        return y < func(x)
    return sum(imap(is_under_curve, coordinates))


def make_random_points(min_corner, max_corner, num_points=100):
    """Returns random coordinate pairs in the rectangle defined."""
    min_x, min_y = min_corner
    max_x, max_y = max_corner
    return ((uniform(min_x, max_x), uniform(min_y, max_y)) \
        for i in xrange(num_points))
