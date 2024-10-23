import numpy as np
import matplotlib.pyplot as plt

def perform_dft(signal):
    N = len(signal)
    n = np.arange(N)
    k = n.reshape((N, 1))
    exp_matrix = np.exp(-2j * np.pi * k * n / N)
    return np.dot(exp_matrix, signal)

def perform_fft():
    T = 1.0  # Sampling period
    x = np.linspace(0.0, 1.0, 1000)
    
    # Example: Signal is a sum of sinusoids
    signal = np.sin(50.0 * 2.0 * np.pi * x) + 0.5 * np.sin(80.0 * 2.0 * np.pi * x)
    
    fft_result = np.fft.fft(signal)
    freqs = np.fft.fftfreq(len(signal), d=T)
    
    # Plot original signal
    plt.subplot(2, 1, 1)
    plt.plot(x, signal)
    plt.title("Original Signal")
    
    # Plot FFT result
    plt.subplot(2, 1, 2)
    plt.plot(freqs, np.abs(fft_result))
    plt.title("FFT of the Signal")
    plt.xlim(0, 100)
    
    plt.show()

def perform_fft_on_large_signal():
    x = np.linspace(0, 2 * np.pi, 10000)
    signal = np.sin(50 * x) + 0.5 * np.sin(120 * x)
    
    # Perform FFT on large signal
    fft_result = np.fft.fft(signal)
    freqs = np.fft.fftfreq(len(signal))
    
    plt.plot(freqs, np.abs(fft_result))
    plt.xlim(0, 0.1)
    plt.show()
