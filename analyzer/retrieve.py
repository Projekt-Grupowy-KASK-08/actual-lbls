import pandas as pd
import os


# Base directory
base_dir = 'C:\\Users\kasia\\OneDrive\\Pulpit\\pacjenci\\'

# Read the CSV file
df = pd.read_csv(base_dir + 'label.csv')

# Iterate over the rows of the DataFrame
for index, row in df.iterrows():
    # Extract the URL and parse it to get the file path
    url = row['csv']
    file_path = url.split('//')[-1]

    # Check if the file exists in the pacjenci directory
    full_path = os.path.join(base_dir, file_path)
    if os.path.exists(full_path):
        print(f'File exists: {full_path}')
        df.loc[index, 'file_path'] = full_path
    else:
        print(f'File does not exist: {full_path}')

# Save the updated DataFrame to a new CSV file
df.to_csv(base_dir + 'label_with_file_path.csv', index=False)

# dodaj tylko bezwzględną ścieżkę do pliku
"""import pandas as pd
import re
import os

input_csv = r"C:\inzynierka\pacjenci\label.csv"  # zamień na właściwą ścieżkę do pliku
output_csv = r"C:\inzynierka\pacjenci\edited_label_with_file_path.csv"  # zamień na właściwą ścieżkę do pliku wyjściowego

def edit_file_paths(file_path):
    # Remove the specified part of the URL
    edited_path = re.sub(r"https://kask.eti.pg.edu.pl/dbs/static/preprocessed//", "/", file_path)
    # Replace name with initials
    edited_path = re.sub(r"(\w+)\s(\w+)/", lambda m: f"/{m.group(1)[0]}{m.group(2)[0]}/", edited_path)
    return edited_path

def edit_csv_file(input_csv, output_csv):
    df = pd.read_csv(input_csv)

    # Edit the file paths
    df['csv'] = df['csv'].apply(edit_file_paths)

    # Save to a new CSV file
    df.to_csv(output_csv, index=False)
    print(f"Edited CSV saved to {output_csv}")

# Run the function
edit_csv_file(input_csv, output_csv)"""


    