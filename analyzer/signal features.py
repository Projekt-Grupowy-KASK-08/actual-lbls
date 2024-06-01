import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def countSpikes(data):
    threshold = 2 * np.std(data['2: preprocessed'])

    above_threshold = data['2: preprocessed'] > threshold

    # Count spikes only at the start of each above-threshold sequence
    spikes = np.diff(above_threshold.astype(int)) == 1

    # Add 1 to the result to account for the first spike if it starts at index 0
    spike_count = np.sum(spikes) + (above_threshold.iloc[0] == True)

    spike_indices = np.where(spikes)[0] + 1  # +1 to correct the index shift due to np.diff
    return spike_count, spike_indices


np.random.seed(0)
data = pd.DataFrame({
    '2: preprocessed': np.random.randn(100)
})

spike_count, spike_indices = countSpikes(data)

plt.figure(figsize=(10, 6))
plt.plot(data['2: preprocessed'], label='Signal')
plt.axhline(y=2 * np.std(data['2: preprocessed']), color='r', linestyle='--', label='Threshold')
plt.scatter(spike_indices, data['2: preprocessed'].iloc[spike_indices], color='red', label='Spikes')
plt.xlabel('Sample Index')
plt.ylabel('Signal Value')
plt.title(f'Signal with Detected Spikes (Count: {spike_count})')
plt.legend()
plt.show()
