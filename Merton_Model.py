"""
Merton Model Equity Valuation

This script calculates the equity value of a company using the Merton model. The Merton model is a financial model
that estimates the probability of a company defaulting on its debt obligations.

Inputs:
- assets: Total value of the company's assets.
- debt: Value of the company's debt.
- equity_volatility: Volatility of the company's equity.
- risk_free_rate: Risk-free interest rate.
- maturity: Time to maturity in years.

Output:
- equity_value: Estimated equity value of the company.

Usage:
Specify the input values for a specific company and run the script. The calculated equity value will be printed as output.
"""

import numpy as np
from scipy.stats import norm

def merton_model_equity_value(assets, debt, equity_volatility, risk_free_rate, maturity):
    # Calculate d1 and d2 using the Merton model formula
    d1 = (np.log(assets / debt) + (risk_free_rate + 0.5 * equity_volatility ** 2) * maturity) / (equity_volatility * np.sqrt(maturity))
    d2 = d1 - equity_volatility * np.sqrt(maturity)

    # Calculate the equity value using the Merton model formula
    equity_value = assets * norm.cdf(d1) - debt * np.exp(-risk_free_rate * maturity) * norm.cdf(d2)
    return equity_value

# Example usage with realistic inputs
assets = 1000000  # Total value of the company's assets
debt = 800000  # Value of the company's debt
equity_volatility = 0.25  # Volatility of the company's equity
risk_free_rate = 0.03  # Risk-free interest rate
maturity = 2  # Time to maturity in years

# Calculate the equity value using the Merton model
equity_value = merton_model_equity_value(assets, debt, equity_volatility, risk_free_rate, maturity)

# Print the calculated equity value
print("Equity value:", equity_value)
