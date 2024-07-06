import os
import matplotlib.pyplot as plt
from astropy.io import ascii
import pandas as pd

# Define the base directory
base_dir = 'Exodata/LightCurves/KMT/2017'



# Function to plot data from a .pysis file
def plot_pysis_file(file_path):
    # Read the data from the file
    table = ascii.read(file_path)
    # Convert the data to a Pandas DataFrame
    df = table.to_pandas()
    # Plot the data with error bars
    plt.figure(figsize=(10, 6))
    plt.errorbar(df['HJD'], df['\Delta_flux'], yerr=df['flux_err'], fmt='o', linestyle='-', color='b', ecolor='b', capsize=2)
    plt.xlabel('HJD')
    plt.ylabel('Flux')
    plt.title(f'Flux over Time for {os.path.basename(file_path)}')
    plt.grid(True)
    plt.show()


plot_pysis_file('Exodata/LightCurves/KMT/2017/blg-0165/KMTC42_I.pysis')