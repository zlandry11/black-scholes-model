"""
    The Black-Scholes model was first introduced by economists Fischer Black and Myron Scholes
in 1973. This partial-differential equation (PDE) gives a theoretical estimate for the fair
price of a European option. This model has become widely used by investors today and is still
one of the most popular formulas for pricing options. Several assumptions must be made in this
model to determine the price of European options:
    1. Options can only be exercised at expiration
    2. Risk-free interest rate and volatility are constant
    3. Stock price follows Geometric Brownian Motion
    4. No dividends are paid for the duration of the option
    5. No transaction or commission 
    6. No arbitrage opportunities exist
"""
import math
from scipy.stats import norm

def fair_price(S, X, T, r, sigma, option='call'):
    """Finds fair price of a European call or put option.

    Args:
        S: Initial price of the underlying asset
        X: Strike price of the option
        T: Expiration in years
        r: Annual risk-free interest rate compounded continuously
        sigma: Volatility of returns of the underlying asset
        option: Type of option
    
    Returns: 
        The fair price of a European call or put option under Black-Scholes
        assumptions. The price will be calculated in American dollars. 
    """
    d1 = (math.log(S/X) + r*T + (.5)*(sigma**2)*(T)) / (sigma*math.sqrt(T))
    d2 = d1 - sigma*math.sqrt(T)

    if option == 'call':
        price = S*norm.cdf(d1) - X*math.exp(-r*T)*norm.cdf(d2)
    if option == 'put':
        price = price = -S*norm.cdf(-d1) + X*math.exp(-r*T)*norm.cdf(-d2)
    price = round(price, 2)

    print("Fair price of European {} option: ${}".format(option, price))
    return price

