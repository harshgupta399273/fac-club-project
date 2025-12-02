import numpy as np

def monte_carlo_simulation(returns, num_simulations=10000, days=252):
    simulations = []
    mean_return = np.mean(returns)
    std_return = np.std(returns)

    for _ in range(num_simulations):
        simulated = np.random.normal(mean_return, std_return, days)
        simulations.append(simulated)

    return np.array(simulations)

if __name__ == '__main__':
    print('Monte Carlo simulation module loaded.')

