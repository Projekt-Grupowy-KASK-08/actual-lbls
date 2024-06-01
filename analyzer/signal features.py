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


"""
    Calculate the average frequency of spikes in the data.
    
    f = Number of spikes / time
"""


def average_frequency_of_spikes(data, f=20000):
    spike_count, _ = countSpikes(data)
    return (spike_count / len(data)) * f


"""

    
    Rf = Number of intervals between 33ms and 66ms / number of intervals
    
"""


def calculate_intervals(spike_indices, f=20000):
    # Calculate time intervals between spikes
    intervals = np.diff(spike_indices) / f * 1000  # Convert to milliseconds
    return intervals


def frequency_coefficient(intervals):
    # Count intervals in the range 33 < ti < 66
    valid_intervals = (intervals > 33) & (intervals < 66)
    N33_66 = np.sum(valid_intervals)
    N_total = len(intervals)

    if N_total == 0:
        return 0

    Rf = N33_66 / N_total
    return Rf


"""
    Launch rate
    Rb = Number of intervals shorter 33ms / number of intervals
"""


def launch_rate(intervals):
    valid_intervals = intervals < 33
    N0_33 = np.sum(valid_intervals)
    N_total = len(intervals)

    if N_total == 0:
        return 0

    Rb = N0_33 / N_total
    return Rb


file = '/Users/pawelmanczak/Downloads/pacjenci/extracted_data.csv'

df = pd.read_csv(file)
data = df.iloc[0, :].dropna().astype(float)

spike_count, spike_indices = countSpikes(data)
intervals = calculate_intervals(spike_indices)
Rf = frequency_coefficient(intervals)

print("Współczynnik częstosci " + str(Rf))
print("Srednia cczęstotliowść występowania impulsów nerwowych " + str(average_frequency_of_spikes(data)))
print("Współczynnik wystrzeliwania " + str(launch_rate(intervals)))

#spike_indices = np.array([0, 2000, 4000, 8000, 13000, 20000])
#print(calculate_intervals(spike_indices))

"""plt.figure(figsize=(10, 6))
plt.plot(data, label='Signal')
plt.axhline(y=3 * np.std(data), color='r', linestyle='--', label='Threshold')
plt.scatter(spike_indices, data.iloc[spike_indices], color='red', label='Spikes')
plt.xlabel('Sample Index')
plt.ylabel('Signal Value')
plt.title(f'Signal with Detected Spikes (Count: {spike_count})')
plt.legend()
plt.show()"""
