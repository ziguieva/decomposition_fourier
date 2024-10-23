import numpy as np
import matplotlib.pyplot as plt

def compute_error(original_signal, reconstructed_signal):
    return np.mean((original_signal - reconstructed_signal) ** 2)

def analyze_approximation_error():
    T = 2 * np.pi
    x = np.linspace(0, T, 1000)
    original_signal = np.sign(np.sin(x))  # Square wave
    
    errors = []
    for n_terms in range(1, 20):
        reconstructed = np.zeros_like(original_signal)
        for n in range(1, n_terms + 1):
            reconstructed += (4 / (np.pi * n)) * np.sin((2 * n - 1) * x)
        
        error = compute_error(original_signal, reconstructed)
        errors.append(error)
    
    plt.plot(range(1, 20), errors)
    plt.title("Approximation Error vs Number of Fourier Terms")
    plt.xlabel("Number of Terms")
    plt.ylabel("Mean Squared Error")
    plt.show()
