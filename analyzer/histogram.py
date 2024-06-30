import pandas as pd
import matplotlib.pyplot as plt
import os
from signal_features import countSpikes, data_without_extreme_spikes

"""
    This script shows histogram of preprocessed values in the signal and saves the plot as a PNG file.
"""
# Base directory
base_dir = 'C:\\Users\\kasia\\OneDrive\\Pulpit\\pacjenci\\'


def plot_csv(file_path):
    # Open csv file of each operation and read it
    csv = pd.read_csv(file_path)

    segment_size = 10000

    # Create a new figure and add subplots
    fig, axs = plt.subplots(2, 1, figsize=(14, 7))

    # Find the range without extreme spikes
    start, end = data_without_extreme_spikes(csv, segment_size=1000, ax_to_plot_threshold=axs[0])

    filtered_csv = csv[(csv['Time'] >= start) & (csv['Time'] <= end)]


    # Plot the filtered data
    axs[0].plot(filtered_csv['Time'], filtered_csv['2: preprocessed'], linewidth=0.5, alpha=0.5)

    start_time = csv['Time'].iloc[0]
    end_time = csv['Time'].iloc[-1]

    # Add title and labels
    axs[0].set_title(file_path)
    axs[0].set_xlabel('Time')
    axs[0].set_ylabel('Signal')

    # Split the signal into segments
    segments = [filtered_csv['2: preprocessed'][i:i + segment_size] for i in
                range(0, len(filtered_csv['2: preprocessed']), segment_size)]

    all_spikes = []

    # Process each segment separately
    for i, segment in enumerate(segments):
        # Find where the signal in this segment exceeds the threshold
        _, spikes = countSpikes(segment)
        all_spikes.append(spikes)

        # Plot the spikes
        axs[0].plot(filtered_csv['Time'].iloc[i * segment_size + spikes],
                    filtered_csv['2: preprocessed'].iloc[i * segment_size + spikes],
                    'r.', markersize=2)

    # Plot the histogram of preprocessed values
    axs[1].hist(abs(filtered_csv['2: preprocessed']), bins=100, color='blue', alpha=0.7)
    axs[1].set_title('Histogram of Preprocessed Values')
    axs[1].set_xlabel('Preprocessed Signal Value')
    axs[1].set_ylabel('Frequency')
    axs[1].set_xlim(0, 500)
    #axs[1].set_yscale('log')

    # Adjust layout
    plt.tight_layout()
    png_filename = "png\\" + os.path.basename(file_path).replace('.csv', '.png')
    plt.savefig(png_filename)
    #plt.show()


"""
# Recursively find all CSV files in the base directory inside pacjent/operacja folders
csv_files = []
for root, dirs, files in os.walk(base_dir):
    # Check if the directory structure matches pacjent/operacja
    path_parts = os.path.relpath(root, base_dir).split(os.sep)
    if len(path_parts) == 2:  # Ensure we are only looking two levels deep (pacjent/operacja)
        for file in files:
            if file.endswith('.csv'):
                csv_files.append(os.path.join(root, file))


# Iterate over all found CSV files
for file_path in csv_files:
    plot_csv(file_path)
 """
plot_csv(r"C:\Users\kasia\OneDrive\Pulpit\pacjenci\Sloma Pawel/466417777/depth-10,0_kanalCentral.csv")
plot_csv(r"C:\Users\kasia\OneDrive\Pulpit\pacjenci\Sloma Pawel/466417777/depth-9,7_kanalCentral.csv")
print("-------zewnetrzne---------")
plot_csv(r"C:\Users\kasia\OneDrive\Pulpit\pacjenci\Sloma Pawel/466417777/depth-7,9_kanalCentral.csv")
plot_csv(r"C:\Users\kasia\OneDrive\Pulpit\pacjenci\Sloma Pawel/466417777/depth-7,6_kanalCentral.csv")
plot_csv(r"C:\Users\kasia\OneDrive\Pulpit\pacjenci\Sloma Pawel/466417777/depth-7,3_kanalCentral.csv")
print("------wewnetrzne---------")
plot_csv(r"C:\Users\kasia\OneDrive\Pulpit\pacjenci\Wolf Krzysztof/546253247/depth-2,0_kanalCentral.csv")
plot_csv(r"C:\Users\kasia\OneDrive\Pulpit\pacjenci\Wolf Krzysztof/546253247/depth-1,5_kanalCentral.csv")