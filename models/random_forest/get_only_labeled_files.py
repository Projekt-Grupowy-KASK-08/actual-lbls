import pandas as pd
import os

input_csv = r"C:\inzynierka\pacjenci\label_with_file_path.csv"
base_destination_path = r"C:\inzynierka\oznaczenia_i_pliki"
output_csv = r"C:\inzynierka\oznaczenia_i_pliki\processed_files_labels.csv"


def get_initials(name):
    parts = name.split()
    initials = ''.join([part[0].upper() for part in parts if part])
    return initials


def copy_files_with_labels():
    df = pd.read_csv(input_csv)
    labeled_files = df.dropna(subset=['timeserieslabels'])
    processed_files_info = []

    for index, row in labeled_files.iterrows():
        file_path = row['file_path']
        start = row['start']
        end = row['end']
        label = row['timeserieslabels']

        if pd.notnull(label):
            data = pd.read_csv(file_path)
            filtered_data = data[(data['Time'] >= start) & (data['Time'] <= end)][['Time', '2: preprocessed']]
            relative_path = os.path.relpath(file_path, os.path.dirname(input_csv))

            # Zamień imię i nazwisko na inicjały w ścieżce docelowej
            path_parts = relative_path.split(os.sep)
            name_part = path_parts[0]
            initials = get_initials(name_part)
            path_parts[0] = initials
            new_relative_path = os.path.join(*path_parts)

            destination_path = os.path.join(base_destination_path, new_relative_path)

            os.makedirs(os.path.dirname(destination_path), exist_ok=True)
            filtered_data.to_csv(destination_path, index=False)
            print(f"Processed {file_path} and saved to {destination_path}")
            relative_destination_path = os.path.relpath(destination_path, base_destination_path)
            processed_files_info.append({'file_path': relative_destination_path, 'label': label})

    processed_files_df = pd.DataFrame(processed_files_info)
    processed_files_df.to_csv(output_csv, index=False)
    print(f"All labeled files have been processed and saved. Summary saved to {output_csv}.")


copy_files_with_labels()
