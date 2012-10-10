mc-integration
==============

A (hopefully) readable implementation of Monte Carlo Integration.

Monte Carlo Integration is a fun algorithm for its conceptual simplicity, and
is useful for multi-dimentional / multi-variate integration.

Sample Use
----------

```python
from integrate import monte_carlo_integrate

def some_quadratic_function(x)
    return x ** 2 + 42 * x

# perform the integration with 1000 random points
area = monte_carlo_integrate(some_quadratic_function, -10, 10, num_points=1000)

print 'The area under the curve is', area
```
