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
    plt.errorbar(df['HJD'], df['mag'], yerr=df['mag_err'], fmt='o', linestyle='-', color='b', ecolor='b', capsize=2)
    plt.xlabel('HJD')
    plt.ylabel('Flux')
    plt.title(f'Flux over Time for {os.path.basename(file_path)}')
    plt.grid(True)
    plt.show()

# Loop through each folder in the base directory
for root, dirs, files in os.walk(base_dir):
    for file in files:
        # Check if the file ends with I.pysis
        if file.endswith('I.pysis'):
            file_path = os.path.join(root, file)
            print(f'Plotting file: {file_path}')
            plot_pysis_file(file_path)
            break  # Plot only one file per folder
