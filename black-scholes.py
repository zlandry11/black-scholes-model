import math
from scipy.stats import norm

class EuropeanOption:

    def __init__(self, asset_price, strike_price, expiration, rate, sigma, option):
        """Constructor for EuropeanOption class. 

        Parameters:
            asset_price (int or float): Initial price of the underlying asset
            strike_price (int or float): Strike price of the option
            expiration (int or float): Expiration in years
            rate (float): Annual risk-free interest rate compounded continuously
            sigma (float): Volatility of returns of the underlying asset
            option (str): Type of option
        """
        self.S = asset_price
        self.X = strike_price
        self.T = expiration
        self.r = rate
        self.sigma = sigma
        self.option = option

    def d1(self):
        """Calculates the d1 value."""
        return (math.log(self.S/self.X) + self.r*self.T + (.5)*(self.sigma**2)*(self.T)) / (self.sigma*math.sqrt(self.T))
    
    def d2(self):
        """Calculates the d2 value."""
        return self.d1() - self.sigma*math.sqrt(self.T)
    
    def fair_price(self):
        """Finds fair price of a European call or put option.
        
        Returns: 
            The fair price (in American dollars) of a European call 
            or put option under Black-Scholes assumptions.
        """
        if self.option == 'call':
            price = self.S*norm.cdf(self.d1()) - self.X*math.exp(-self.r*self.T)*norm.cdf(self.d2())
        if self.option == 'put':
            price  = -self.S*norm.cdf(-self.d1()) + self.X*math.exp(-self.r*self.T)*norm.cdf(-self.d2())
        price = round(price, 2)

        print("Fair price of European {} option: ${}".format(self.option, price))
        return price

    def delta(self):
        """Finds the delta hedging value for an option.

        Returns:
            The delta hedging value for a call or put option.
        """
        if self.option == 'call':
            delta = norm.cdf(self.d1())
        elif self.option == 'put':
            delta = norm.cdf(self.d1()) - 1
        print("Delta hedging value: {}".format(delta))
        return delta
    
    
put = EuropeanOption(250, 250, 4/12, .03, .2, 'put')
call = EuropeanOption(350, 365, 5/12, .04, .22, 'call')
call.fair_price()
put.delta()
call.delta()


            
    

