import numpy as np

def calculate_var(returns, confidence=0.95):
    returns = np.array(returns)
    return np.percentile(returns, (1 - confidence) * 100)

if __name__ == '__main__':
    print('VaR model module loaded.')

