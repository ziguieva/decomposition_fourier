import series_fourier
import decomposition_fourier
import reconstruction_signal
import visualisation
import filtering_fourier

def menu():
    print("Choose an operation:")
    print("1. Fourier Series")
    print("2. Fourier Decomposition (FFT/DFT)")
    print("3. Signal Reconstruction")
    print("4. Signal Filtering in Frequency Domain")
    print("5. Visualize Fourier Series")
    
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        series_fourier.compute_fourier_series()
    elif choice == '2':
        decomposition_fourier.perform_fft()
    elif choice == '3':
        reconstruction_signal.reconstruct_signal()
    elif choice == '4':
        filtering_fourier.apply_filter()
    elif choice == '5':
        visualisation.visualize()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    menu()
