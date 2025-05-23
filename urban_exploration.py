import os
import scipy.io
import numpy as np
import matplotlib.pyplot as plt

# Set the path to your .mat file
file_path = 'C:/Users/HP/Desktop/SEMESTER_6/EE405_Undergraduate Project I/Urban_6.mat'  # Make sure this path is correct

if os.path.exists(file_path):
    # Load the .mat file
    mat = scipy.io.loadmat(file_path)

    # Print the structure of the loaded .mat file
    print(mat.keys())

    # Extract data
    Y = mat['Y']     # (bands, num_pixels)
    M = mat['M']     # Endmembers: (bands, num_endmembers)
    A = mat['A']     # Abundances: (num_endmembers, num_pixels)
    HW = mat['HW']   # (height, width)

    bands, num_pixels = Y.shape
    _, num_endmembers = M.shape
    height, width = HW[0][0], HW[0][1]

    print("Number of spectral channels (bands):", bands)
    print("Number of pixels:", num_pixels)
    print("Image dimensions (HxW):", height, "x", width)
    print("Number of endmembers:", num_endmembers)

    # Plot abundance maps
    abundance_maps = A.reshape((num_endmembers, height, width))
    plt.figure(figsize=(15, 3))
    for i in range(num_endmembers):
        plt.subplot(1, num_endmembers, i+1)
        plt.imshow(abundance_maps[i], cmap='viridis')
        plt.title(f'Endmember {i+1}')
        plt.axis('off')
    plt.tight_layout()
    plt.show(block=False)

    # Plot endmember signatures


    plt.figure(figsize=(12, 3 * num_endmembers))
    for i in range(num_endmembers):
        plt.subplot(3, 2, i + 1)
        plt.plot(M[:, i], color='blue')
        plt.title(f'Endmember {i+1} Signature')
        plt.xlabel('Spectral Band')
        plt.ylabel('Reflectance')
        plt.grid(True)
    plt.subplots_adjust(hspace=1)   
    
    plt.show(block=False)

    # Plot original vs reconstructed spectra
    np.random.seed(42)
    pixel_indices = np.random.choice(Y.shape[1], size=10, replace=False)

    plt.figure(figsize=(15, 20))
    for i, idx in enumerate(pixel_indices):
        original = Y[:, idx]
        abundance = A[:, idx]
        reconstructed = M @ abundance

        plt.subplot(5, 2, i+1)
        plt.plot(original, label='Original', color='black')
        plt.plot(reconstructed, label='Reconstructed (LMM)', linestyle='--', color='red')
        plt.title(f'Pixel #{idx} Spectrum')
        plt.xlabel('Spectral Band')
        plt.ylabel('Reflectance')
        if i==0:
            plt.legend()
        plt.grid(True)

    plt.subplots_adjust(hspace=1)
    plt.show()

else:
    print("File not found. Please check the file path.")
