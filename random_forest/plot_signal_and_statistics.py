import pandas as pd
import re
import os
import matplotlib.pyplot as plt
from signal_features import (
    data_without_extreme_spikes, countSpikes, average_frequency_of_spikes, calculate_intervals,
    frequency_coefficient, launch_rate, pause_indicator, pause_ratio,
    modified_launch_rate, standard_deviation_of_duration, signal_power,
    average_nonlinear_energy, average_absolute_difference, rms
)

input_csv = r"C:\inzynierka\pacjenci\label_with_file_path.csv"  # zamień na właściwą ścieżkę do pliku

def extract_depth(file_path):
    match = re.search(r'depth-([\d,]+)_', file_path)
    if match:
        return float(match.group(1).replace(',', '.'))
    return None

def display_plots(file_path, filtered_data, preprocessed_data, statistics, spike_indices, label):
    # Create a figure with subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), gridspec_kw={'width_ratios': [3, 1]})

    # Plot the clipped signal
    ax1.plot(filtered_data['Time'], preprocessed_data, label='Clipped Signal')
    ax1.scatter(filtered_data['Time'].iloc[spike_indices], preprocessed_data.iloc[spike_indices], color='red', s=10, label='Spikes')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Signal')
    ax1.set_title(f'{label} \nClipped Signal for {file_path}')
    ax1.legend()

    # Display statistics next to the plot
    textstr = '\n'.join([f'{key}: {value:.2f}' for key, value in statistics.items()])
    ax2.axis('off')
    ax2.text(0.1, 0.5, textstr, transform=ax2.transAxes, fontsize=10,
             verticalalignment='center', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    plt.show()

df = pd.read_csv(input_csv)

script_dir = os.path.dirname(os.path.abspath(__file__))

for index, row in df.iterrows():
    file_path = row['file_path']
    csv = pd.read_csv(file_path)
    label = row['timeserieslabels']
    depth = extract_depth(file_path)

    # Przycinanie danych przez klasyfikator
    start = row['start']
    end = row['end']

    # Filtrowanie danych pomiędzy start a end
    if start is not None and end is not None:
        filtered_data = csv[(csv['Time'] >= start) & (csv['Time'] <= end)]
        preprocessed_data = filtered_data['2: preprocessed']

        # Wywoływanie funkcji do obliczania statystyk
        spike_count, spike_indices = countSpikes(preprocessed_data)
        avg_freq_spikes = average_frequency_of_spikes(preprocessed_data)
        intervals = calculate_intervals(spike_indices)
        freq_coeff = frequency_coefficient(intervals)
        launch_rt = launch_rate(intervals)
        pause_ind = pause_indicator(intervals)
        pause_rat = pause_ratio(intervals)
        mod_launch_rt = modified_launch_rate(intervals)
        std_duration = standard_deviation_of_duration(intervals)
        low_band_power, high_band_power = signal_power(preprocessed_data)
        avg_nl_energy = average_nonlinear_energy(preprocessed_data)
        avg_abs_diff = average_absolute_difference(preprocessed_data)
        root_mean_square = rms(preprocessed_data)

        # Przygotowanie słownika ze statystykami
        statistics = {
            'Spike Count': spike_count,
            'depth': depth,
            'Avg Freq Spikes': avg_freq_spikes,
            'Freq Coeff': freq_coeff,
            'Launch Rate': launch_rt,
            'Pause Indicator': pause_ind,
            'Pause Ratio': pause_rat,
            'Mod Launch Rate': mod_launch_rt,
            'Std Duration': std_duration,
            'Low Band Power': low_band_power,
            'High Band Power': high_band_power,
            'Avg NL Energy': avg_nl_energy,
            'Avg Abs Diff': avg_abs_diff,
            'RMS': root_mean_square
        }

        # Wyświetlanie wykresów
        display_plots(file_path, filtered_data, preprocessed_data, statistics, spike_indices, label)
    else:
        print(f"No valid data range found for file {file_path}")

