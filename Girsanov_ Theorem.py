"""
Girsanov's Theorem Implementation in Python for Finance

This script demonstrates the implementation of Girsanov's 
theorem in Python for finance. Girsanov's theorem is a fundamental 
result in stochastic calculus with applications in finance. It establishes a 
relationship between two probability measures, one under the original probability 
measure and another under a new measure obtained by changing the drift term 
of a stochastic process. In this example, we simulate the stock price process 
under two measures: the original measure (P) and the new measure (Q) obtained by applying 
Girsanov's theorem. The stock price process is modeled using geometric Brownian motion.
The script generates random stock price paths and computes the corresponding stock prices 
under both measures. It then prints the first 10 stock prices for each measure.

"""

import numpy as np
from scipy.stats import norm

def girsonov_theorem(S0, mu, sigma, T, num_paths):
    """
    Function to simulate the stock price process under the original measure (P)
    and the new measure (Q) using Girsanov's theorem.

    Parameters:
        S0 (float): Initial stock price.
        mu (float): Drift.
        sigma (float): Volatility.
        T (float): Time horizon.
        num_paths (int): Number of simulated paths.

    Returns:
        tuple: A tuple containing two arrays representing the stock prices under the original measure and the new measure.
    """

    # Calculate the time step
    dt = T / num_paths

    # Generate random Wiener increments
    dW = np.random.normal(0, np.sqrt(dt), num_paths)

    # Compute the Wiener process
    W = np.cumsum(dW)

    # Calculate the time array
    t = np.linspace(0, T, num_paths)

    # Original process under the original measure (P)
    S_original = S0 * np.exp((mu - 0.5 * sigma**2) * t + sigma * W)

    # Compute the Radon-Nikodym derivative
    drift_change = mu - 0.5 * sigma**2
    RN_derivative = np.exp(-drift_change * W - 0.5 * drift_change**2 * t)

    # New process under the new measure (Q)
    S_new = S0 * RN_derivative * np.exp(sigma * W)

    return S_original, S_new

# Parameters
S0 = 100.0  # Initial stock price
mu = 0.05   # Drift
sigma = 0.2  # Volatility
T = 1.0     # Time horizon
num_paths = 1000  # Number of simulated paths

# Generate stock price paths under original and new measures using Girsanov's theorem
S_original, S_new = girsonov_theorem(S0, mu, sigma, T, num_paths)

# Print the first 10 stock prices for both measures
print("Original measure (P):", S_original[:10])
print("New measure (Q):", S_new[:10])
