import math
from datetime import datetime
from scipy.stats import norm

def black_scholes(S, K, T, r, sigma, option_type='call'):
    d1 = (math.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    if option_type == 'call':
        return S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
    elif option_type == 'put':
        return K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("Invalid option_type. Use 'call' or 'put'.")

# Parameters
S = 661  # stock price
K = 760  # strike price
expiry = datetime(2026, 12, 18) # year/month/day
today = datetime(2025, 9, 16)  #year/month/day
T = (expiry - today).days / 365 # time to expiry in years
r = 0.0429   # risk-free rate 
sigma = 0.13 # implied volatility


call_price = black_scholes(S, K, T, r, sigma, 'call')
print(f"Expected Premium Value: ${call_price:.2f}")
