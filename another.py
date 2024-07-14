
import matplotlib.pyplot as plt
import numpy as np

def plot_data_without_error(data_file):
    # Load data from file
    data = np.loadtxt(data_file)

    # Extract columns from the data
    time = data[:, 0]  # Assuming the first column is time
    magnitude = data[:, 1]  # Assuming the second column is magnitude

    # Plotting without error bars
    plt.plot(time, magnitude, 'o', markersize=5)
    plt.xlabel('Time')
    plt.ylabel('Magnitude')
    plt.title('Data Plot without Error Bars')
    plt.grid(True)
    plt.show()

# Example usage:
data_file = 'Exodata/WFIRST/ulwdc1_015_W149.txt'  # Replace with your actual data file path
plot_data_without_error(data_file)
