"""
Siegel's Paradox Simulation in Python

This script generates two random variables, computes the correlation between them at the individual level,
and then aggregates the data into higher levels to demonstrate Siegel's Paradox. It plots the individual and
aggregated data points, showing how the correlation can change from positive at the individual level to
negative at the aggregated level.

Siegel's Paradox is a statistical phenomenon where the correlation between two variables in a time series is
positive, but when the time series are aggregated into higher levels, the correlation becomes negative.

"""

import numpy as np
import matplotlib.pyplot as plt

# Set random seed for reproducibility
np.random.seed(0)

# Generate random data for two variables
n = 1000
x = np.random.randn(n)  # Generate random data for variable x
y = np.random.randn(n)  # Generate random data for variable y

# Compute correlation at the individual level
corr_individual = np.corrcoef(x, y)[0, 1]  # Compute correlation coefficient between x and y
print("Individual correlation:", corr_individual)

# Aggregate the data into higher levels
aggregated_size = 10  # Number of data points to aggregate
x_agg = x.reshape(-1, aggregated_size).mean(axis=1)  # Aggregate x by taking the mean of every aggregated_size consecutive data points
y_agg = y.reshape(-1, aggregated_size).mean(axis=1)  # Aggregate y by taking the mean of every aggregated_size consecutive data points

# Compute correlation at the aggregated level
corr_aggregated = np.corrcoef(x_agg, y_agg)[0, 1]  # Compute correlation coefficient between aggregated x and aggregated y
print("Aggregated correlation:", corr_aggregated)

# Plot the individual and aggregated data
plt.scatter(x, y, label="Individual Data")  # Scatter plot of individual data points
plt.scatter(x_agg, y_agg, label="Aggregated Data")  # Scatter plot of aggregated data points
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()
