from unittest import TestCase, main
from integrate import (
    get_min_max_for_func,
    make_random_points,
    monte_carlo_integrate,
    num_under_curve,
)


def linear(x):
    return x


####
##
## num_under_curve
##
####

class WhenEvaluatingPointsUnderCurve(TestCase):

    def test_compare_function_1_value(self):
        assert num_under_curve(linear, [(1, 0)]) == 1

    def test_compare_function_multiple_values_all_under_curve(self):
        assert num_under_curve(linear, [(1, 0), (.5, .4), (2, 1.3)]) == 3

    def test_compare_function_multiple_values_some_under_curve(self):
        assert num_under_curve(linear, [(1, 0), (.5, .4), (2, 3)]) == 2

    def test_make_random_points_returns_correct_number_results(self):
        assert len(
            list(make_random_points((0, 0), (1, 1), num_points=10))) == 10

    def test_make_random_points_returns_all_valid_points(self):
        for x, y in make_random_points((0, -3), (10, -1), num_points=30):
            assert 0 <= x <= 10 and -3 <= y <= -1


####
##
## monte_carlo_integrate
##
####

class WhenTestingIntegrationFunction(TestCase):

    def assert_integration_correct(self, func, xmin, xmax, expected,
                                   expected_err=10, num_points=10000):
        result = monte_carlo_integrate(func, xmin, xmax, num_points=num_points)
        percent_error = abs((result - expected) / expected * 100)
        if percent_error > expected_err:
            raise AssertionError('Expected {0}; got {1}; err {2}'.format(
                expected, result, percent_error))
        return percent_error

    def test_integrate_linear_func_zero_to_one(self):
        self.assert_integration_correct(linear, 0, 1, .5)

    def test_integrate_linear_func_zero_to_two(self):
        self.assert_integration_correct(linear, 0, 2, 2)

    def test_integrate_linear_func_neg_one_to_two(self):
        self.assert_integration_correct(linear, -1, 2, 1.5)

    def test_integrate_linear_func_one_to_two(self):
        self.assert_integration_correct(linear, 1, 2, 1.5)

    def test_integrate_linear_func_neg_one_to_five(self):
        self.assert_integration_correct(linear, -1, 5, 12)


####
##
## get_min_max_for_func
##
####

class WhenTestingGetMinMaxFunction(TestCase):

    def test_getting_min_max_for_linear_func(self):
        x, y = get_min_max_for_func(linear, 0, 1)
        assert x == 0
        assert abs(1 - y) < .000001


if __name__ == '__main__':
    main()
