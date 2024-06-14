import numpy as np
import os
import pandas as pd


base_dir = 'C:\\Users\kasia\\OneDrive\\Pulpit\\pacjenci\\'
output_path = 'C:\\Users\kasia\\OneDrive\\Pulpit\\pacjenci_cleaned\\'

def get_longest_range(ranges):
    max_diff=0
    start = 0
    end = 0
    for i in range(len(ranges['end_time'])):
        diff = ranges['end_time'][i] - ranges['start_time'][i]
        if diff > max_diff:
            max_diff = diff
            start = ranges['start_time'][i]
            end = ranges['end_time'][i]
    return start, end

# Calculating treashold based on neighbouring segments
def calculate_treshold(data, segment, segment_size, i):
    left_neighbour_segment = 10
    right_neighbour_segment = 10
    if i < left_neighbour_segment:
        left_neighbour_segment = i
    elif i + right_neighbour_segment > len(segment):
        right_neighbour_segment = len(segment) - i

    threshold = 7 * np.std(
        data.iloc[(i - left_neighbour_segment) * segment_size:(i + 1 + right_neighbour_segment) * segment_size][
            "2: preprocessed"])
    return threshold

def clean_data_and_adjust_label(data, start_label, end_label, segment_size):
    clear_indices = []
    segments = int(len(data) / segment_size)

    empty_space = False
    time_adjustment = 0

    for i in range(segments):
        segment = data.iloc[i * segment_size:(i + 1) * segment_size]
        threshold = calculate_treshold(data, segment, segment_size, i)
        spikes = np.where(segment["2: preprocessed"] >= threshold)[0]
        zero_count = np.sum((segment["2: preprocessed"] >= -3) & (segment["2: preprocessed"] <= 3))

        # When there are no extreme spikes in a segment and when most of the values are not close to zero
        if len(spikes) == 0 and zero_count / len(segment) < 0.6:

            # handling time adjustment
            if empty_space:
                if segment['Time'].iloc[-1] > start_label > segment['Time'].iloc[0]:
                    start_label -= time_adjustment
                if segment['Time'].iloc[-1] > end_label > segment['Time'].iloc[0]:
                    end_label -= time_adjustment
                for idx in segment.index:
                    segment.at[idx, 'Time'] -= time_adjustment

            clear_indices.extend(segment.index)

        else:
            empty_space = True
            start_of_empty_space = segment['Time'].iloc[0]
            end_of_empty_space = segment['Time'].iloc[-1]
            time_adjustment += (end_of_empty_space - start_of_empty_space)

    return data.loc[clear_indices], start_label, end_label


def process_csv_and_clean_data(input_dir, output_dir, label_csv):
    # Odczytanie danych z pliku CSV
    df = pd.read_csv(label_csv)

    # Przygotowanie nowego pliku CSV na wyniki
    output_csv_path = output_dir + 'label_cleaned.csv'
    os.makedirs(output_dir, exist_ok=True)

    results = []

    # Przetwarzanie każdego wiersza w CSV
    for _, row in df.iterrows():
        file_url = row['csv']
        start = row['start']
        end = row['end']
        timeseries_labels = row['timeserieslabels']
        file_path = row['file_path']

        # Odczytanie danych operacji z pliku CSV
        data = pd.read_csv(file_path)

        # Czyszczenie danych
        cleaned_data, new_start, new_end = clean_data_and_adjust_label(data, start, end, segment_size=1000)

        # Zapisanie oczyszczonych danych do nowego pliku
        cleaned_file_path = file_path.replace("pacjenci", "pacjenci_cleaned")
        cleaned_output_dir = os.path.dirname(cleaned_file_path)
        os.makedirs(cleaned_output_dir, exist_ok=True)
        cleaned_data.to_csv(cleaned_file_path, index=False)

        # Przygotowanie nowego wiersza do pliku wynikowego
        new_row = {
            'csv': file_url,
            'start': new_start,
            'end': new_end,
            'timeserieslabels': timeseries_labels,
            'file_path': cleaned_file_path
        }
        results.append(new_row)

        # Zapisanie wyników do nowego pliku CSV
        results_df = pd.DataFrame(results)
        results_df.to_csv(output_csv_path, index=False)


label_csv = base_dir + 'label_with_file_path.csv'

process_csv_and_clean_data(base_dir, output_path, label_csv)