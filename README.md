## Computational Finance
The purpose of this repository is to get hands on with the details of implementing a Pricing framework and hoopefully eventually a risk management tool suite (a platform would be a pipe dream.)

The goals are 
- Gather market data from free sources
    - Option (other derivatives if necessary) Market data from [OKX](https://www.okx.com/docs-v5/en/#public-data)
    - Interest Rate data (https://www.bankofengland.co.uk/statistics/yield-curves)

- Write some routines to calculate Implied volatility using above market data
    - Experiment with numerical methods for root finding
        - Experiment with parallel implementations for rapid performance
    
- Generate volatility surface vols ... consult [this resource](https://tsimagine.com/insights/thinking-about-building-a-volatility-surface-think-again/) when the time comes.
    
- Calibrate different models to the above market data

- Price dervative based on calibrated models
    - OKX have derivative market prices available so could be a nice baseline. 