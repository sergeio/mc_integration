from integrate import (
    num_under_curve,
    make_random_points,
    monte_carlo_integrate,
)


def test_compare_function_1_value():
    linear = lambda x: x
    assert num_under_curve(linear, [(1, 0)]) == 1


def test_compare_function_multiple_values_all_under_curve():
    linear = lambda x: x
    assert num_under_curve(linear, [(1, 0), (.5, .4), (2, 1.3)]) == 3


def test_compare_function_multiple_values_some_under_curve():
    linear = lambda x: x
    assert num_under_curve(linear, [(1, 0), (.5, .4), (2, 3)]) == 2


def test_make_random_points_returns_correct_number_results():
    assert len(list(make_random_points((0, 0), (1, 1), num_points=10))) == 10


def test_make_random_points_returns_all_valid_points():
    for x, y in make_random_points((0, -3), (10, -1), num_points=30):
        assert 0 <= x <= 10 and -3 <= y <= -1


def test_integrate_linear_func():
    linear = lambda x: x
    assert abs(
        monte_carlo_integrate(linear, 0, 1, num_points=10000) - .5) < .02


def run_tests():
    print '\nRunning tests:'
    passed = 0
    total = 0
    for key, value in globals().items():
        if key.startswith('test_'):
            total += 1
            try:
                value()
                print '.',
                passed += 1
            except AssertionError as e:
                print 'F', key

    print '\nPassed {0} / {1} tests.'.format(passed, total)


if __name__ == '__main__':
    run_tests()
