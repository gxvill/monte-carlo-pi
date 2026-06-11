# Monte Carlo Pi Estimation

The value of pi is infinitely precise. We know its value, but how can we figure it out for ourselves?

We can use a Monte Carlo Simulation to find an estimation of its particular value.

## Dart Board Simulation

Taking a square of side length 2, we can inscribe a circle of radius one at its center. This is our geometric dart
board that we will be throwing at. After throwing $$n$$ darts at the board, we know that the ratio of darts in the
circle to $$n$$ should be $$\frac{\pi}{4}$$, or something close to it.

The law of large numbers dictates that as our $$n \rightarrow \infty$$, our estimation will converge to the
actual value of $$\pi$$.
