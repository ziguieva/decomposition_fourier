import numpy as np
import matplotlib.pyplot as plt

def reconstruct_signal():
    T = 2 * np.pi
    n_terms = 10
    x = np.linspace(0, T, 1000)
    original_signal = np.sign(np.sin(x))  # Example: Square wave
    
    # Reconstruct from Fourier coefficients
    reconstructed_signal = np.zeros_like(original_signal)
    for n in range(1, n_terms + 1):
        reconstructed_signal += (4 / (np.pi * n)) * np.sin((2 * n - 1) * x)
    
    plt.plot(x, original_signal, label="Original Signal")
    plt.plot(x, reconstructed_signal, label="Reconstructed Signal")
    plt.legend()
    plt.show()
