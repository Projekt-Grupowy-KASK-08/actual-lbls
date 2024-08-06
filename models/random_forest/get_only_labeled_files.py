import pandas as pd
import os
import shutil

input_csv = r"/Users/pawelmanczak/Downloads/pacjenci/label_with_file_path.csv"  # zamień na właściwą ścieżkę do pliku
base_destination_path = r"/Users/pawelmanczak/Downloads/oznaczenia_i_pliki"  # zamień na właściwą ścieżkę docelową

def copy_files_with_labels():
    df = pd.read_csv(input_csv)

    # Filtruj pliki, które mają oznaczenie
    labeled_files = df.dropna(subset=['timeserieslabels'])

    for index, row in labeled_files.iterrows():
        file_path = row['file_path']
        label = row['timeserieslabels']

        if pd.notnull(label):
            # Zachowanie struktury katalogów
            relative_path = os.path.relpath(file_path, os.path.dirname(input_csv))
            destination_path = os.path.join(base_destination_path, relative_path)

            os.makedirs(os.path.dirname(destination_path), exist_ok=True)

            # Kopiowanie pliku
            shutil.copy2(file_path, destination_path)
            print(f"Copied {file_path} to {destination_path}")

    print("All labeled files have been copied.")

copy_files_with_labels()
