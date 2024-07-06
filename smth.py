import matplotlib.pyplot as plt
import pandas as pd
import os
from astropy.io import ascii
from scipy.ndimage import gaussian_filter1d

paths = [
    'Exodata/LightCurves/KMT/2023/blg-0416',
    'Exodata/LightCurves/KMT/2023/blg-0469'

]

def plot_pysis_file(file_path, tag, err):
    # Read the data from the file
    table = ascii.read(file_path)
    # Convert the data to a Pandas DataFrame
    df = table.to_pandas()
    # Plot the data with error bars
    plt.figure(figsize=(10, 6))

    # Check if tag and error column exist
    if tag in df.columns and err in df.columns:
        plt.errorbar(df['HJD'], df[tag], yerr=df[err], fmt='o', linestyle='-', color='b', ecolor='b', capsize=2)
    else:
        print(f"Warning: Columns '{tag}' or '{err}' not found in {file_path}")

    plt.xlabel('HJD')
    plt.ylabel(tag)
    plt.title(f'MGD over Time for {os.path.basename(file_path)}')
    plt.grid(True)
    plt.show()

plot_pysis_file('Exodata/LightCurves/KMT/2021/blg-1547/KMTA03_I.pysis', 'mag', 'mag_err')
plot_pysis_file('Exodata/LightCurves/KMT/2021/blg-1547/KMTA03_I.pysis', '\Delta_flux', 'flux_err')


# # Loop through each path in the list
# for dir in paths:
#     print(f"Processing directory: {dir}")
#     for filename in os.listdir(dir):
#         filepath = os.path.join(dir, filename)

#         # Check if file ends with '_V.pysis' (modify extension if needed)
#         if filepath.endswith('_V.pysis'):
#             plot_pysis_file(filepath, '\Delta_flux', 'flux_err')
#         else:
#             plot_pysis_file(filepath, 'mag', 'mag_err')



# Read data from the FITS file

# from scipy.signal import savgol_filter
# smoothed_flux = savgol_filter(df['mag'], window_length=11, polyorder=2)

# # plt.plot(df['HJD'], df['mag'], label='Original')
# plt.plot(df['HJD'], smoothed_flux, label='Smoothed', color='red')
# plt.xlabel('Time')
# plt.ylabel('Flux')
# plt.title('Savitzky-Golay Filter')
# plt.legend()
# plt.show()

# import pywt
# import numpy as np
# import matplotlib.pyplot as plt
# from astropy.io import ascii

# # Read data
# table = ascii.read('Exodata/LightCurves/KMT/2023/blg-0469/KMTA42_I.pysis')
# df = table.to_pandas()

# # Perform wavelet decomposition
# coeffs = pywt.wavedec(df['mag'], 'db4', level=5)

# # Calculate threshold for noise reduction
# sigma = np.median(np.abs(coeffs[-1] - np.median(coeffs[-1])))
# uthresh = sigma * np.sqrt(2 * np.log(len(df['mag'])))

# # Apply soft thresholding
# denoised_coeffs = coeffs
# denoised_coeffs[1:] = [pywt.threshold(i, value=uthresh, mode="soft") for i in denoised_coeffs[1:]]

# # Perform wavelet reconstruction
# denoised_flux = pywt.waverec(denoised_coeffs, 'db4')

# # Trim denoised_flux to match the length of original data
# if len(denoised_flux) > len(df['mag']):
#     denoised_flux = denoised_flux[:len(df['mag'])]
# else:
#     denoised_flux = np.pad(denoised_flux, (0, len(df['mag']) - len(denoised_flux)), 'constant', constant_values=(0, 0))

# # Plot the results
# plt.plot(df['HJD'], df['mag'], label='Original')
# plt.plot(df['HJD'], denoised_flux, label='Denoised', color='red')
# plt.xlabel('Time')
# plt.ylabel('Magnitude')
# plt.title('Wavelet Transform Denoising')
# plt.legend()
# plt.show()
