mc-integration
==============

A (hopefully) readable implementation of Monte Carlo Integration.

Monte Carlo Integration is a fun algorithm for its conceptual simplicity; it is
useful for multi-dimentional / multi-variate integration.

Sample Use
----------

```python
from integrate import monte_carlo_integrate

def a_quadratic_function(x)
    return x ** 2 + 42 * x

# perform the integration with 10,000,000 random points
area = monte_carlo_integrate(a_quadratic_function, -1, 1, num_points=10000000)

print 'The area under the curve is', area
```
yields
```
The area under the curve is 0.70327423229187835
```
5.5% error
