import numpy as np
import matplotlib.pyplot as plt

def fourier_coefficients(f, T, n_terms):
    a0 = (2 / T) * np.trapz(f, dx=T/len(f))
    an = []
    bn = []
    
    for n in range(1, n_terms+1):
        an_n = (2 / T) * np.trapz(f * np.cos(2 * np.pi * n * np.linspace(0, T, len(f)) / T), dx=T/len(f))
        bn_n = (2 / T) * np.trapz(f * np.sin(2 * np.pi * n * np.linspace(0, T, len(f)) / T), dx=T/len(f))
        an.append(an_n)
        bn.append(bn_n)
    
    return a0, an, bn

def compute_fourier_series():
    T = 2 * np.pi  # Period
    x = np.linspace(0, T, 1000)
    
    # Example: Square wave
    f = np.sign(np.sin(x))
    
    n_terms = 10
    a0, an, bn = fourier_coefficients(f, T, n_terms)
    
    reconstructed = np.full_like(f, a0 / 2)
    for n in range(1, n_terms + 1):
        reconstructed += an[n-1] * np.cos(2 * np.pi * n * x / T) + bn[n-1] * np.sin(2 * np.pi * n * x / T)
    
    plt.plot(x, f, label="Original Signal")
    plt.plot(x, reconstructed, label="Fourier Series Approximation")
    plt.legend()
    plt.show()
