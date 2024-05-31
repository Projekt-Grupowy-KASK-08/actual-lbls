import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# Base directory
base_dir = 'C:\\Users\\kasia\\OneDrive\\Pulpit\\pacjenci\\'

# Read the CSV file
df = pd.read_csv(base_dir + 'label_with_file_path.csv')


def artifact_removal(data, vc_threshold=1.8, segment_size=5000):
    clear_indices = []
    last_variance = 1
    segments = int(len(data) / segment_size)

    for i in range(segments - 1):
        segment = data.iloc[i * segment_size:(i + 1) * segment_size]

        variance = stats.variation(segment['2: preprocessed'])
        if (variance / last_variance <= vc_threshold):
            clear_indices.extend(segment.index)
        last_variance = variance

    return data.loc[clear_indices]


def extreme_spike_removal(data, segment_size=5000):
    clear_indices = []
    segments = int(len(data) / segment_size)
    threshold = 6 * np.std(data["2: preprocessed"])

    for i in range(segments):
        segment = data.iloc[i * segment_size:(i + 1) * segment_size]
        spikes = np.where(segment["2: preprocessed"] > threshold)[0]
        if len(spikes) == 0:
            clear_indices.extend(segment.index)

    return data.loc[clear_indices]


def data_without_extreme_spikes(data, segment_size):
    ranges = {
        'start_time': [],
        'end_time': []
    }
    clear_indices = []
    segments = int(len(data) / segment_size)
    threshold = 6 * np.std(data["2: preprocessed"])
    for i in range(segments):
        segment = data.iloc[i * segment_size:(i + 1) * segment_size]
        spikes = np.where(segment["2: preprocessed"] > threshold)[0]
        zero_count = np.sum((segment["2: preprocessed"] >= -3) & (segment["2: preprocessed"] <= 3))
        print(f'Zero count: {zero_count}, Segment length: {len(segment)}')
        if len(spikes) == 0 and zero_count / len(segment) < 0.6:
            ranges['start_time'].append(segment['Time'].iloc[0])
            ranges['end_time'].append(segment['Time'].iloc[-1])
            clear_indices.extend(segment.index)

    return ranges


# Iterate over the rows of the DataFrame
for index, row in df.iterrows():
    # Open csv file of each operation and read it
    csv = pd.read_csv(row['file_path'])
    segment_size = 5000
    # Remove artifacts from the signal
    # csv = artifact_removal(csv, vc_threshold=1.8, segment_size=500)
    ranges = data_without_extreme_spikes(csv, segment_size=1000)
    # Define the size of the segments

    # Define start and end of label
    if row['start'] < csv['Time'].iloc[0]:
        start_time = csv['Time'].iloc[0]
        print("przycięto oznaczenie na początku!!!!!!")
    else:
        start_time = row['start']
    if row['end'] > csv['Time'].iloc[-1]:
        end_time = csv['Time'].iloc[-1]
        print("przycięto oznaczenie na końcu!!!!!!")
    else:
        end_time = row['end']

    # Define class
    label = row['timeserieslabels']
    # Create a new figure and add a subplot
    fig, axs = plt.subplots(2, 1, sharex=True, figsize=(15, 5))

    # Add title and labels
    axs[0].set_title(label)
    axs[0].set_xlabel('Time')
    axs[0].set_ylabel('Signal')
    for start, end in zip(ranges['start_time'], ranges['end_time']):
        axs[0].axvspan(start, end, color='gray', alpha=0.5)
    # Find the indices corresponding to the start and end times
    start_index = csv['Time'].searchsorted(start_time)
    end_index = csv['Time'].searchsorted(end_time)

    color = 'gray'
    if label == "['Skorupa lub prazkowie']":
        color = 'green'
    if label == "['Czesci zewnetrzne galki bladej (5-6 mm przed celem)']":
        color = 'red'
    if label == "['Czesci wewnetrzne galki bladej (2-3 mm przed celem lub do 1 mm za celem)']":
        color = 'yellow'

    # Fill the area between the signal and the x-axis
    print(f'Label: {label}, Start: {start_time}, End: {end_time}')
    print(f'Start index: {start_index}, End index: {end_index}')
    print(
        f'Start value: {csv["2: preprocessed"].iloc[start_index]}, End value: {csv["2: preprocessed"].iloc[end_index]}')
    axs[0].axvspan(csv['Time'].iloc[start_index], csv['Time'].iloc[end_index], facecolor=color, alpha=0.3, label=label)

    # Split the signal into segments
    segments = [csv['2: preprocessed'][i:i + segment_size] for i in range(0, len(csv['2: preprocessed']), segment_size)]
    all_spikes = []
    # Process each segment separately
    for i, segment in enumerate(segments):
        # Define a threshold for this segment
        threshold = 3 * np.std(segment)

        # Find where the signal in this segment exceeds the threshold
        spikes = np.where(segment > threshold)[0]
        all_spikes.append(spikes)

        # Plot the signal for this segment
        axs[0].plot(csv['Time'][i * segment_size:(i + 1) * segment_size], segment, linewidth=0.5)

        # Calculate the start and end indices of the current segment
        start_index = i * segment_size
        end_index = min((i + 1) * segment_size, len(csv['Time']))

        # Plot the threshold
        axs[0].plot([csv['Time'].iloc[start_index], csv['Time'].iloc[end_index - 1]], [threshold, threshold], color='r',
                    linestyle='--', linewidth=0.5)

        # Plot the spikes
        axs[0].plot(csv['Time'].iloc[i * segment_size + spikes], csv['2: preprocessed'].iloc[i * segment_size + spikes],
                    'r.', markersize=2)

    # Plot the distribution of spikes per segment in the second subplot
    num_segments = len(segments)

    # Calculate the midpoint of each segment
    midpoints = [
        (csv['Time'].iloc[i * segment_size] + csv['Time'].iloc[min((i + 1) * segment_size, len(csv['Time'])) - 1]) / 2
        for i in range(num_segments)]

    # Plot the distribution of spikes per segment in the second subplot
    total_time = csv['Time'].iloc[-1] - csv['Time'].iloc[0]
    bar_width = total_time / num_segments
    axs[1].bar(midpoints, [len(spikes) for spikes in all_spikes], width=bar_width)
    axs[1].set_xlabel('Time')
    axs[1].set_ylabel('Number of spikes')
    axs[1].set_title('Number of spikes per segment')

    plt.tight_layout()
    plt.legend()
    plt.show()
