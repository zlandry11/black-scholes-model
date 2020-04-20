from option import EuropeanOption

class Portfolio():
    """Creating a portfolio consisting of stocks and options. 
    
    Stocks consist of long and short positions while options 
    are classified as either a call or a put. A delta-neutral
    hedging strategy is used to minimize the total delta of 
    the portfolio. 
    """
    
# Logic
# A portfolio can have four scenarios with associated hedging strategies:
#   1. Buying a call option => short sell underlying asset
#   2. Buying a put option => buy (long) underlying asset
#   3. Selling call option => buy (long) underlying asset
#   4. Selling put option => short sell underlying asset






    def __init__()