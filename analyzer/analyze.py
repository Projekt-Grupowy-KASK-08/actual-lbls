import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import median_abs_deviation

# Base directory
base_dir = 'D:\\STUDIA\\Projekt Grupowy\\actual-lbls\\pacjenci\\'

# Read the CSV file
df = pd.read_csv(base_dir + 'label_with_file_path.csv')




# Iterate over the rows of the DataFrame
for index, row in df.iterrows():
    # Open csv file of each operation and read it
    csv = pd.read_csv(row['file_path'])
    start_time = row['start']
    end_time = row['end']
    label = row['timeserieslabels']

    # Define the size of the segments
    # frequency of the signal is the same for all recordings, so it should be the same to get objective results
    segment_size = 5000 

    # Create a new figure and add a subplot
    fig, axs = plt.subplots(2, 1, sharex=True)
    # axs[0].plot(csv['Time'], csv['2: preprocessed'], label=row['file_path'])
    # axs[0].set_xlabel('Time')
    # axs[0].set_ylabel('Signal', color='blue')
    # axs[0].tick_params('y', colors='blue')

    # Add title and labels
    axs[0].set_title(label)
    axs[0].set_xlabel('Time')
    axs[0].set_ylabel('Signal')


    # Find the indices corresponding to the start and end times
    start_index = csv['Time'].searchsorted(start_time)
    end_index = csv['Time'].searchsorted(end_time)

    # Fill the area between the signal and the x-axis
    print(f'Label: {label}, Start: {start_time}, End: {end_time}')
    print(f'Start index: {start_index}, End index: {end_index}')
    print(f'Start value: {csv["2: preprocessed"].iloc[start_index]}, End value: {csv["2: preprocessed"].iloc[end_index]}')
    axs[0].axvspan(csv['Time'].iloc[start_index], csv['Time'].iloc[end_index], facecolor='red', alpha=0.3, label=label)

    # Split the signal into segments
    segments = [csv['2: preprocessed'][i:i+segment_size] for i in range(0, len(csv['2: preprocessed']), segment_size)]
    all_spikes = []

    # Process each segment separately
    for i, segment in enumerate(segments):
        # Define a threshold for this segment
        # threshold = np.median(segment) + 4 * median_abs_deviation(segment)
        threshold = 3 * np.std(segment)

        # Find where the signal in this segment exceeds the threshold
        spikes = np.where(segment > threshold)[0]
        all_spikes.append(spikes)

        # Plot the signal for this segment
        axs[0].plot(csv['Time'][i*segment_size:(i+1)*segment_size], segment)

        # Calculate the start and end indices of the current segment
        start_index = i * segment_size
        end_index = min((i + 1) * segment_size, len(csv['Time']))

        # Plot the threshold
        axs[0].plot([csv['Time'].iloc[start_index], csv['Time'].iloc[end_index - 1]], [threshold, threshold], color='r', linestyle='--')
        
        # Plot the spikes
        axs[0].plot(csv['Time'].iloc[i*segment_size + spikes], csv['2: preprocessed'].iloc[i*segment_size + spikes], 'r.')

    # Plot the distribution of spikes per segment in the second subplot
    num_segments = len(segments)

    # Calculate the midpoint of each segment
    midpoints = [(csv['Time'].iloc[i*segment_size] + csv['Time'].iloc[min((i+1)*segment_size, len(csv['Time'])) - 1]) / 2 for i in range(num_segments)]

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

    