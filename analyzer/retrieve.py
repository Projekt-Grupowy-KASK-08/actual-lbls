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

    