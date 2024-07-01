import os
import matplotlib.pyplot as plt
from astropy.io import ascii
import pandas as pd

# Directory containing the files
directory = 'Exodata/LightCurves/KMT/2016/blg-2397/'

# Find the file that ends with the letter 'I' before the .pysis file extension
file_to_read = None
for file in os.listdir(directory):
    if file.endswith('I.pysis'):
        file_to_read = file
        break

if file_to_read:
    filepath = os.path.join(directory, file_to_read)

    # Step 1: Read the data from the file
    table = ascii.read(filepath)

    # Step 2: Convert the data to a Pandas DataFrame
    df = table.to_pandas()

    print(df.head())

    # Step 3: Visualize the magnitude data
    plt.figure(figsize=(10, 6))
    plt.plot(df['HJD'], df['mag'], marker='o', linestyle='-', color='b')
    plt.xlabel('HJD')
    plt.ylabel('Magnitude')
    plt.title('Magnitude over Time')
    plt.gca().invert_yaxis()  # Invert y-axis because in astronomy, lower magnitudes are brighter
    plt.grid(True)
    plt.show()
else:
    print("No file ending with 'I.pysis' found in the directory.")
