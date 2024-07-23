import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os
from astropy.io import ascii
from scipy.ndimage import gaussian_filter1d
import torch

def readKMT2(filepath, target_rows=6428, threshold=0.1):
    data = pd.read_csv(filepath, sep=r'\s+', header=None)
    data = data.apply(pd.to_numeric, errors='coerce')
    data = data.dropna(subset=[data.columns[0], data.columns[3]])
    data['x_diff'] = data[data.columns[0]].diff().abs()
    gap_indices = data[data['x_diff'] > threshold].index
    split_dataframes = np.split(data, gap_indices)
    total_rows = sum(df.shape[0] for df in split_dataframes)
    padded_dataframes = []

    if total_rows < target_rows:
        loop_count = 0
        while total_rows < target_rows:
            loop_count += 1
            for df in split_dataframes:
                noise = np.random.normal(0, 1e-8, size=(df.shape[0], 2))
                new_values = df[[data.columns[0], data.columns[3]]].values + noise
                new_df = pd.DataFrame(new_values, columns=[data.columns[0], data.columns[3]])
                padded_dataframes.append(df[[data.columns[0], data.columns[3]]])
                padded_dataframes.append(new_df)
                total_rows += new_df.shape[0]
                if total_rows >= target_rows:
                    break
        combined_dataframe = pd.concat(padded_dataframes, ignore_index=True)
        combined_dataframe = combined_dataframe.iloc[:target_rows]
    else:
        combined_dataframe = pd.concat(split_dataframes, ignore_index=True)
        combined_dataframe = combined_dataframe.iloc[:target_rows]

    magnitudes = combined_dataframe[data.columns[3]].values
    for i in range(1, len(magnitudes) - 1):
        if abs(magnitudes[i] - magnitudes[i-1]) > 0.3 and abs(magnitudes[i] - magnitudes[i+1]) > 0.3:
            avg_neighbor_magnitude = (magnitudes[i-1] + magnitudes[i+1]) / 2
            if magnitudes[i] > avg_neighbor_magnitude:
                magnitudes[i] = avg_neighbor_magnitude + 0.1
            else:
                magnitudes[i] = avg_neighbor_magnitude - 0.1
    combined_dataframe[data.columns[3]] = magnitudes

    data_tensor = torch.tensor(combined_dataframe[[data.columns[0], data.columns[3]]].values, dtype=torch.float32)
    return data_tensor

directory = 'Exodata/PSPL/KMT/2023'
output_csv = 'output.csv'
output_data = []

# Iterate over files in directory
for path, folders, files in os.walk(directory):
    for filename in files:
        if filename.endswith("I.pysis") or "I.pysis" in filename:
            filepath = os.path.join(path, filename)
            print(f"Processing file: {filepath}")
            data_tensor = readKMT2(filepath)
            # x = data_tensor[:, 0].numpy()
            # y = data_tensor[:, 1].numpy()

            # plt.figure(figsize=(10, 6))
            # plt.plot(x, y, 'b.')
            # plt.xlabel('HJD')
            # plt.ylabel('Mag')
            # plt.title(f"{path}")
            # plt.grid(True)

            # Add row to output data
            folder_suffix = path[-4:]
            output_data.append(['KMT', f'KMT-{folder_suffix}', filepath, 'PSPL', 1])

# Create DataFrame and save to CSV
output_df = pd.DataFrame(output_data, columns=['Survey', 'Source', 'Filepath', 'Model', 'Value'])
output_df.to_csv(output_csv, index=False)
print(f"Data saved to {output_csv}")
