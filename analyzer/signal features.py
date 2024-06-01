import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def countSpikes(data):
    threshold = 3 * np.std(data)

    above_threshold = data > threshold

    # Count spikes only at the start of each above-threshold sequence
    spikes = np.diff(above_threshold.astype(int)) == 1

    # Add 1 to the result to account for the first spike if it starts at index 0
    spike_count = np.sum(spikes) + (above_threshold.iloc[0] == True)

    spike_indices = np.where(spikes)[0] + 1  # +1 to correct the index shift due to np.diff
    return spike_count, spike_indices


def average_frequency_of_spikes(data, f=20000):
    spike_count, _ = countSpikes(data)
    return (spike_count / len(data)) * f


# Base directory
file =  '/Users/pawelmanczak/Downloads/pacjenci/extracted_data.csv'

# Read the CSV file
df = pd.read_csv(file)

# Assuming the first row is needed and the columns represent different data points
data = df.iloc[0, :].dropna().astype(float)

print(len(data))

spike_count, spike_indices = countSpikes(data)

plt.figure(figsize=(10, 6))
plt.plot(data, label='Signal')
plt.axhline(y=3 * np.std(data), color='r', linestyle='--', label='Threshold')
plt.scatter(spike_indices, data.iloc[spike_indices], color='red', label='Spikes')
plt.xlabel('Sample Index')
plt.ylabel('Signal Value')
plt.title(f'Signal with Detected Spikes (Count: {spike_count})')
plt.legend()
plt.show()

print(average_frequency_of_spikes(data))
