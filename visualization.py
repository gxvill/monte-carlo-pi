import matplotlib.pyplot as plt
import numpy as np
from variance_reduction.py import estimate_pi_stratified


def estimate_pi_visual(num_samples):
    # generate random points
    x = np.random.uniform(-1, 1, num_samples)
    y = np.random.uniform(-1, 1, num_samples)

    inside = x**2 + y**2 <= 1

    # count how many fall inside the circle

    # estimate pi
    pi_estimate = 4 * np.sum(inside)/num_samples

    # plot
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.scatter(x[inside], y[inside], color='blue', s=1, label='Inside')
    ax.scatter(x[~inside], y[~inside], color='red', s=1, label='Outside')

    # draw the cicle boundary
    theta = np.linspace(0, 2 * np.pi, 300)
    ax.plot(np.cos(theta), np.sin(theta), color='black', linewidth=1.5)

    ax.set_aspect('equal')
    ax.set_title(f'pi ={pi_estimate:.4f} (n = {num_samples})')
    ax.legend()
    plt.savefig(f'plots/monte_carlo_{num_samples}.png')
    plt.show()


def convergence_plot(max_samples=100000, step=100):
    x = np.random.uniform(-1, 1, max_samples)
    y = np.random.uniform(-1, 1, max_samples)
    inside_flags = x**2 + y**2 <= 1

    estimates = []
    sample_sizes = range(step, max_samples + 1, step)

    for n in sample_sizes:
        pi_est = 4 * np.sum(inside_flags[:n]) / n
        estimates.append(pi_est)

    sample_sizes = np.array(list(sample_sizes))

    p = np.pi/4
    var_per_sample = p*(1-p)
    se = 4 * np.sqrt(var_per_sample / sample_sizes)

    ci_95 = 1.96 * se

    plt.figure(figsize=(10, 5))
    plt.plot(sample_sizes, estimates, label='Monte Carlo estimate')
    plt.axhline(y=np.pi, color='r', linestyle='--', label='True pi')

    plt.fill_between(sample_sizes,estimates - ci_95, estimates + ci_95, color='blue',
                     alpha=0.2, label='95% confidence interval')

    plt.xlabel('Number of samples')
    plt.ylabel('Esimate of pi')
    plt.title('Convergence of Monte Carlo pi Estimation')
    plt.legend()
    plt.savefig(f'plots/convergence_{max_samples}.png')
    plt.show()


estimate_pi_visual(100000)
convergence_plot()
