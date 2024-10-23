import numpy as np
import series_fourier
import decomposition_fourier

def test_fourier_series_coefficients():
    T = 2 * np.pi
    x = np.linspace(0, T, 1000)
    signal = np.sign(np.sin(x))
    
    a0, an, bn = series_fourier.fourier_coefficients(signal, T, 10)
    
    assert np.isclose(a0, 0.0, atol=1e-2), "a0 should be approximately 0"
    print("Fourier series coefficient test passed.")

def test_fft():
    signal = np.sin(50 * 2 * np.pi * np.linspace(0, 1, 1000))
    fft_result = np.fft.fft(signal)
    
    assert len(fft_result) == len(signal), "FFT output length should match input length"
    print("FFT test passed.")
    
if __name__ == "__main__":
    test_fourier_series_coefficients()
    test_fft()
