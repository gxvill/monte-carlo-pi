import numpy as np

def estimate_pi(num_samples):
    # generate random points
    x = np.random.uniform(-1,1, num_samples)
    y = np.random.uniform(-1,1, num_samples)

    # count how many fall inside the circle
    inside = np.sum(x**2 + y**2 <= 1)

    # estimate pi
    pi_estimate = 4 * inside/num_samples
    return pi_estimate


samples = [100,1000,10000,100000,1000000,10000000,100000000,1000000000]

for n in samples:
    pi_est = estimate_pi(n)
    print(f"n = {n:>10}, pi = {pi_est:.6f}, error = {abs(pi_est - np.pi):.6f}")
