import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from signal_features import countSpikes, average_frequency_of_spikes, calculate_intervals, frequency_coefficient, launch_rate, pause_indicator, pause_ratio, modified_launch_rate, standard_deviation_of_duration,data_without_extreme_spikes, average_absolute_difference, rms

# Base directory
base_dir = 'C:\\Users\\kasia\\OneDrive\\Pulpit\\pacjenci\\'

# Read the CSV file
df = pd.read_csv(base_dir + 'label_with_file_path.csv')

# Iterate over the rows of the DataFrame
for index, row in df.iterrows():
    # Open csv file of each operation and read it
    csv = pd.read_csv(row['file_path'])
    all_csv = pd.read_csv(row['file_path'])

    # Define class
    label = row['timeserieslabels']

    if label == "['Czesci wewnetrzne galki bladej (2-3 mm przed celem lub do 1 mm za celem)']":
        segment_size = 10000

        # Create a new figure and add a subplot
        fig, axs = plt.subplots(2, 1, sharex=True, figsize=(14, 7))

        # Plot all data as an outline
        axs[0].plot(csv['Time'], csv['2: preprocessed'], linewidth=0.5, alpha=0.5, color="gray")

        _, csv = data_without_extreme_spikes(csv, segment_size=1000, ax_to_plot_threshold=axs[0])
        ranges_clean_data, csv = data_without_extreme_spikes(csv, segment_size=1000)

        # Define start and end of label
        """
        if row['start'] < csv['Time'].iloc[0]:
            start_time = csv['Time'].iloc[0]
            print("przycięto oznaczenie na początku!!!!!!")
        else:
            start_time = row['start']
        if row['end'] > csv['Time'].iloc[-1]:
            end_time = csv['Time'].iloc[-1]
            print("przycięto oznaczenie na końcu!!!!!!")
        else:
            end_time = row['end']"""

        start_time = row['start']
        end_time = row['end']

        # Add title and labels
        axs[0].set_title(label)
        axs[0].set_xlabel('Time')
        axs[0].set_ylabel('Signal')

        # Shadow clean data
        for start, end in zip(ranges_clean_data['start_time'], ranges_clean_data['end_time']):
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

        # Fill the area between label witj color
        axs[0].axvspan(csv['Time'].iloc[start_index], csv['Time'].iloc[end_index], facecolor=color, alpha=0.3, label=label)

        # Split the signal into segments
        segments = [csv['2: preprocessed'][i:i + segment_size] for i in range(0, len(csv['2: preprocessed']), segment_size)]

        all_spikes = []
        all_frequency = []
        frequency_coefficients = []
        launch_rates = []
        pause_indicators = []
        pause_ratios = []
        modified_launch_rates = []
        standard_deviations = []
        low_band_powers = []
        high_band_powers = []
        nonlinear_energies = []
        absolute_differences = []
        rms_values = []

        # Process each segment separately
        for i, segment in enumerate(segments):

            # Find where the signal in this segment exceeds the threshold
            _, spikes = countSpikes(segment)
            all_spikes.append(spikes)

            f = average_frequency_of_spikes(segment, f=segment_size)
            all_frequency.append(f)

            intervals = calculate_intervals(spikes)
            frequency_coefficients.append(frequency_coefficient(intervals))
            launch_rates.append(launch_rate(intervals))
            pause_indicators.append(pause_indicator(intervals))
            pause_ratios.append(pause_ratio(intervals))
            modified_launch_rates.append(modified_launch_rate(intervals))
            standard_deviations.append(standard_deviation_of_duration(intervals))
            absolute_differences.append(average_absolute_difference(segment))
            rms_values.append(rms(segment))

            # Plot the signal for this segment
            axs[0].plot(csv['Time'][i * segment_size:(i + 1) * segment_size], segment, linewidth=0.5)

            # Calculate the start and end indices of the current segment
            start_index = i * segment_size
            end_index = min((i + 1) * segment_size, len(csv['Time']))

            # Plot the spikes
            axs[0].plot(csv['Time'].iloc[i * segment_size + spikes], csv['2: preprocessed'].iloc[i * segment_size + spikes],
                        'r.', markersize=2)

        # Calculate the midpoint of each segment
        num_segments = len(segments)
        midpoints = [
            (csv['Time'].iloc[i * segment_size] + csv['Time'].iloc[min((i + 1) * segment_size, len(csv['Time'])) - 1]) / 2
            for i in range(num_segments)]

        # Plot the statistics in the fourth subplot
        axs[1].plot(midpoints, frequency_coefficients, label='Frequency Coefficient', color='purple')
        axs[1].plot(midpoints, launch_rates, label='Launch Rate', color='orange')
        axs[1].plot(midpoints, pause_indicators, label='Pause Indicator', color='green')
        axs[1].plot(midpoints, pause_ratios, label='Pause Ratio', color='red')
        axs[1].plot(midpoints, modified_launch_rates, label='Modified Launch Rate', color='blue')
        #axs[1].plot(midpoints, standard_deviations, label='Standard Deviation', color='brown')
        axs[1].plot(midpoints, absolute_differences, label='Absolute Difference', color='magenta')
        axs[1].plot(midpoints, rms_values, label='RMS', color='yellow')
        axs[1].set_xlabel('Time')
        axs[1].set_ylabel('Value')
        axs[1].set_title('Segment Statistics')
        axs[1].legend()

        plt.tight_layout()
        plt.show()
