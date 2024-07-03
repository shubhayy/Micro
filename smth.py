import matplotlib.pyplot as plt
import pandas as pd
import os
from astropy.io import ascii
from scipy.ndimage import gaussian_filter1d

paths = [
    'Exodata/LightCurves/KMT/2016/blg-0212/KMTC02_I.pysis',
    'Exodata/LightCurves/KMT/2016/blg-1105/KMTA18_I.pysis',
    'Exodata/LightCurves/KMT/2016/blg-1107/KMTA18_I.pysis',
    'Exodata/LightCurves/KMT/2016/blg-1397/KMTA31_I.pysis',
]

def plot_pysis_file(file_path):
    # Read the data from the file
    table = ascii.read(file_path)
    # Convert the data to a Pandas DataFrame
    df = table.to_pandas()
    # Plot the data with error bars
    plt.figure(figsize=(10, 6))
    plt.errorbar(df['HJD'], df['mag'], yerr=df['mag_err'], fmt='o', linestyle='-', color='b', ecolor='b', capsize=2)
    plt.xlabel('HJD')
    plt.ylabel('MGD')
    plt.title(f'MGD over Time for {os.path.basename(file_path)}')
    plt.grid(True)
    plt.show()

# Loop through paths using their elements directly
for file_path in paths:
    plot_pysis_file(file_path)
