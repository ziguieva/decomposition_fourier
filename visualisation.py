import numpy as np
import matplotlib.pyplot as plt

def visualize():
    T = 2 * np.pi
    x = np.linspace(0, T, 1000)
    
    signal = np.sign(np.sin(x))  # Square wave
    fft_result = np.fft.fft(signal)
    freqs = np.fft.fftfreq(len(signal))
    
    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    plt.plot(x, signal)
    plt.title("Original Signal")
    
    plt.subplot(1, 2, 2)
    plt.plot(freqs, np.abs(fft_result))
    plt.title("FFT Result")
    
    plt.tight_layout()
    plt.show()
