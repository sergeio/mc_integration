from itertools import imap
from random import uniform


def monte_carlo_integrate(func, xmin, xmax, num_points=100):
    ymin, ymax = get_min_max_for_func(func, xmin, xmax)
    rectangle_area = (ymax - ymin) * (xmax - xmin)
    points = make_random_points(
        (xmin, ymin), (xmax, ymax), num_points=num_points)
    ratio_under_curve = num_under_curve(func, points) / float(num_points)
    return rectangle_area * ratio_under_curve


def num_under_curve(func, coordinates):
    """# points in :param coordinates: falling under the curve :param func:."""
    def is_under_curve(xy):
        x, y = xy
        true_y = func(x)
        if true_y > 0 and y >= 0 and y < true_y: return 1
        if true_y < 0 and y <= 0 and y > true_y: return -1
        return 0
    return sum(imap(is_under_curve, coordinates))


def get_min_max_for_func(func, xmin, xmax, num_points=100000):
    """Get the minimum and maximum values for the given function and range.

    ..note: This is an approximation.

    """
    def frange(start, stop, step):
        """Like xrange, but works with floats."""
        while start < stop:
            yield start
            start += step

    step = (xmax - xmin) / float(num_points)
    min_val, max_val = xmin, xmin

    for y in imap(func, frange(xmin, xmax, step)):
        if y < min_val: min_val = y
        elif y > max_val: max_val = y

    return min_val, max_val


def make_random_points(min_corner, max_corner, num_points=100):
    """Returns random coordinate pairs in the rectangle defined."""
    xmin, ymin = min_corner
    xmax, ymax = max_corner
    return ((uniform(xmin, xmax), uniform(ymin, ymax)) \
        for i in xrange(num_points))
