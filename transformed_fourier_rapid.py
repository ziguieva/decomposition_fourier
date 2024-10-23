import numpy as np
import matplotlib.pyplot as plt
import time

def perform_fft():
    x = np.linspace(0, 2 * np.pi, 10000)
    signal = np.sin(50 * x) + 0.5 * np.sin(120 * x)
    
    start_time = time.time()
    fft_result = np.fft.fft(signal)
    end_time = time.time()
    
    print(f"FFT computation took: {end_time - start_time} seconds")
    
    freqs = np.fft.fftfreq(len(signal))
    
    plt.plot(freqs, np.abs(fft_result))
    plt.xlim(0, 0.1)
    plt.show()
