import numpy as np
import matplotlib.pyplot as plt

def successive_poisson(tau1, tau2, size=1):
    """Compute time for arrival of 2 successive Poisson processes."""
    # Draw samples out of first exponential distribution: t1
    t1 = np.random.exponential(tau1, size)

    # Draw samples out of second exponential distribution: t2
    t2 = np.random.exponential(tau2, size)

    return t1 + t2

# Draw samples of waiting times: waiting_times
waiting_times = successive_poisson(764,715,100000)

# Make the histogram
plt.hist(waiting_times, histtype='step', bins=100, normed=True)


# Label axes
_ = plt.xlabel('Waiting Time')
_ = plt.ylabel('Quantity')


# Show the plot
plt.show()