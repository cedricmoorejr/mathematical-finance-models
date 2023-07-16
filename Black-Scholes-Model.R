#######################################################################
# Script: Black-Scholes Model Implementation in R                     #
#                                                                     #
# Description: This script demonstrates the implementation of the     #
#              Black-Scholes model, a mathematical model for pricing  #
#              options. The script defines a function to calculate    #
#              option prices based on the Black-Scholes formula and   #
#              provides an example usage.                             #
#                                                                     #
#######################################################################

# Black-Scholes Model Implementation

# Function to calculate option price using Black-Scholes formula
# Arguments:
#   S: Current stock price
#   K: Strike price
#   r: Risk-free interest rate
#   t: Time to expiration (in years)
#   sigma: Volatility of the underlying stock
#   type: Option type, either "call" or "put"

black_scholes <- function(S, K, r, t, sigma, type) {
  # Calculate d1 and d2 terms
  d1 <- (log(S / K) + (r + (sigma^2) / 2) * t) / (sigma * sqrt(t))
  d2 <- d1 - sigma * sqrt(t)
  
  # Calculate option price based on option type
  if (type == "call") {
    # Calculate call option price
    price <- S * pnorm(d1) - K * exp(-r * t) * pnorm(d2)
  } else if (type == "put") {
    # Calculate put option price
    price <- K * exp(-r * t) * pnorm(-d2) - S * pnorm(-d1)
  } else {
    # Handle invalid option type
    stop("Invalid option type. Must be 'call' or 'put'.")
  }
  
  # Return the calculated option price
  return(price)
}

# Example usage
S <- 100    # Current stock price
K <- 105    # Strike price
r <- 0.05   # Risk-free interest rate
t <- 0.5    # Time to expiration (6 months)
sigma <- 0.2   # Volatility of the underlying stock
type <- "call"  # Option type (call or put)

# Calculate the option price using the black_scholes function
option_price <- black_scholes(S, K, r, t, sigma, type)

# Print the calculated option price
print(paste("Option price:", option_price))
