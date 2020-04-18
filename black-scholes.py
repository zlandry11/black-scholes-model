import math
from scipy.stats import norm

def fair_price(S, X, T, r, sigma, option='call'):
    """Finds fair price of a European call or put option.

    User can select from different types of options and also 
    whether or not the underlying stock pays dividends. 
    
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

