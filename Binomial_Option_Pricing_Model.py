"""
Binomial Option Pricing Model

This script calculates the price of a European call option using the binomial model.
The binomial model is a discrete-time model for the dynamics of the underlying asset
price and provides a way to approximate the price of options. This script implements
the binomial model and computes the option price based on the specified input parameters.

"""


import numpy as np

def binomial_model(S, K, r, T, vol, N):
    """
    Calculates the price of a European call option using the binomial model.

    Parameters:
        S (float): initial stock price
        K (float): strike price
        r (float): risk-free interest rate
        T (float): time to maturity (in years)
        vol (float): volatility of the underlying asset
        N (int): number of time steps

    Returns:
        float: price of the option
    """

    # Step 1: Calculate delta t
    delta_t = T / N

    # Step 2: Calculate up and down factors
    u = np.exp(vol * np.sqrt(delta_t))  # Up factor
    d = 1 / u  # Down factor

    # Step 3: Calculate risk-neutral probability
    p = (np.exp(r * delta_t) - d) / (u - d)

    # Step 4: Create arrays to store stock prices and option prices
    stock_prices = np.zeros((N+1, N+1))
    option_prices = np.zeros((N+1, N+1))

    # Step 5: Initialize the stock prices at each step
    stock_prices[0, 0] = S

    for i in range(1, N+1):
        stock_prices[i, 0] = stock_prices[i-1, 0] * u
        for j in range(1, i+1):
            stock_prices[i, j] = stock_prices[i-1, j-1] * d

    # Step 6: Calculate option prices at expiration (i.e., at the last time step)
    option_prices[N, :] = np.maximum(0, stock_prices[N, :] - K)

    # Step 7: Backward iteration to calculate option prices at earlier time steps
    for i in range(N-1, -1, -1):
        for j in range(i+1):
            option_prices[i, j] = np.exp(-r * delta_t) * (p * option_prices[i+1, j] + (1 - p) * option_prices[i+1, j+1])

    # Step 8: Return the option price at time 0 (initial time step)
    return option_prices[0, 0]

# Example usage
initial_stock_price = 100
strike_price = 105
risk_free_rate = 0.05
time_to_maturity = 1
volatility = 0.2
num_steps = 100

option_price = binomial_model(initial_stock_price, strike_price, risk_free_rate, time_to_maturity, volatility, num_steps)
print("Option price:", option_price)
