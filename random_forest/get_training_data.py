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
from sklearn.preprocessing import LabelEncoder

input_csv = r"C:\inzynierka\pacjenci\label_with_file_path.csv"  # zamień na właściwą ścieżkę do pliku


def extract_depth(file_path):
    match = re.search(r'depth-([\d,]+)_', file_path)
    if match:
        return float(match.group(1).replace(',', '.'))
    return None

def save_statistics_in_a_file():
    df = pd.read_csv(input_csv)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_csv = os.path.join(script_dir, 'output_statistics.csv')

    # Tworzenie pliku CSV z nagłówkami kolumn
    with open(output_csv, 'w') as f:
        f.write(
            'file_path,depth,label,spike_count,avg_freq_spikes,freq_coeff,launch_rate,pause_indicator,pause_ratio,mod_launch_rate,std_duration,low_band_power,high_band_power,avg_nl_energy,avg_abs_diff,rms\n')

    # Przetwarzanie każdego pliku CSV i zapisywanie statystyk do pliku wyjściowego
    for index, row in df.iterrows():
        file_path = row['file_path']
        csv = pd.read_csv(file_path)
        label = row['timeserieslabels']
        depth = extract_depth(file_path)

        # Przycinanie danych przez klasyfikator
        # start, end = data_without_extreme_spikes(csv, segment_size=1000)
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

            # Zapis statystyk do pliku CSV
            with open(output_csv, 'a') as f:
                f.write(
                    f'{file_path},{depth},{label},{spike_count},{avg_freq_spikes},{freq_coeff},{launch_rt},{pause_ind},{pause_rat},{mod_launch_rt},{std_duration},{low_band_power},{high_band_power},{avg_nl_energy},{avg_abs_diff},{root_mean_square}\n')
        else:
            print(f"No valid data range found for file {file_path}")

    print(f"Statistics saved to {output_csv}")
    return output_csv


