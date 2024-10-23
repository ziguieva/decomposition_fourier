import numpy as np
import matplotlib.pyplot as plt

def approximate_non_periodic_signal():
    T = 2 * np.pi
    x = np.linspace(0, T, 1000)
    non_periodic_signal = np.exp(-x)  # Example of non-periodic signal
    
    # Truncate Fourier series
    n_terms = 10
    reconstructed = np.zeros_like(non_periodic_signal)
    for n in range(1, n_terms + 1):
        reconstructed += (2 / T) * np.sin(n * x)
    
    plt.plot(x, non_periodic_signal, label="Original Non-Periodic Signal")
    plt.plot(x, reconstructed, label="Truncated Fourier Series Approximation")
    plt.legend()
    plt.show()
