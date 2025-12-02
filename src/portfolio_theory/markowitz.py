import numpy as np

def portfolio_variance(weights, cov_matrix):
    return np.dot(weights.T, np.dot(cov_matrix, weights))

if __name__ == '__main__':
    print('Markowitz portfolio module loaded.')

