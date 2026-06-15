import random
import statistics as st
import numpy as np
import matplotlib as plt

def estimate_pi_stratified(num_samples):
    """
    stratified sampling: divide the square into a grid, sample uniformly within each stratum
    """
    n_per_side = int(np.sqrt(num_samples))
    total_inside = 0
    total_points = 0
    variance_n = 0

    for i in range(n_per_side):
        for j in range(n_per_side):
            # x bounds
            x_left = -1 + 2*i/n_per_side
            x_right = -1 + 2*(i+1)/n_per_side

            # y bounds
            y_bottom = -1 + 2*j/n_per_side
            y_top = -1 + 2*(j+1)/n_per_side

            x = np.random.uniform(x_left, x_right)
            y = np.random.uniform(y_bottom, y_top)

            if x**2 + y**2 <= 1:
                total_inside += 1
            total_points += 1



    return 4 * total_inside/total_points

"""
can we also calculate the variance of this estimation?
We should do multiple trials, and then calculate the variance from those trials
"""
def variance_calc(num_trials, num_samples):
    pi_trials = []

    for i in range(num_trials):
        pi_trials.append(estimate_pi_stratified(num_samples))

    avg_pi = np.average(pi_trials)
    variance = np.var(pi_trials, ddof=1)
    std_dev = np.sqrt(variance)

    print("Average pi value:", avg_pi)
    print("Variance:", variance)
    print("Standard Deviation:", std_dev)

variance_calc(100,10000)
