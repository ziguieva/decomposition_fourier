import numpy as np
import matplotlib.pyplot as plt

def apply_filter():
    T = 1.0  # Sampling period
    x = np.linspace(0.0, 1.0, 1000)
    
    # Example: Signal with multiple frequencies
    signal = np.sin(50.0 * 2.0 * np.pi * x) + 0.5 * np.sin(120.0 * 2.0 * np.pi * x)
    
    fft_result = np.fft.fft(signal)
    freqs = np.fft.fftfreq(len(signal), d=T)
    
    # Apply low-pass filter by zeroing out high frequencies
    cutoff = 100  # Hz
    fft_result[np.abs(freqs) > cutoff] = 0
    
    filtered_signal = np.fft.ifft(fft_result)
    
    # Plot original and filtered signals
    plt.subplot(2, 1, 1)
    plt.plot(x, signal)
    plt.title("Original Signal")
    
    plt.subplot(2, 1, 2)
    plt.plot(x, filtered_signal)
    plt.title("Filtered Signal (Low-Pass)")
    
    plt.show()
