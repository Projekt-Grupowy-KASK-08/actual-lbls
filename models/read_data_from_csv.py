import re
import pandas as pd
import os

# próbkowanie danych to 20khz
# czyli 2s nagrania to 40 000 próbek

# assuming "/" is folder the separator, probably it won't work on windows
csv_file_path = '/Users/pawelmanczak/Downloads/pacjenci/Sloma Pawel/466417777/depth-10,0_kanalCentral.csv'
label_file_path = '/Users/pawelmanczak/Downloads/pacjenci/label.csv'
csv_path_base = '/Users/pawelmanczak/Downloads/pacjenci/'


def check_file_exists(file_path) -> bool:
    return os.path.isfile(file_path)


def extract_depth(url):
    match = re.search(r'depth[-]?\d+,\d+', url)
    if match:
        return match.group(0)
    return None


def extract_path_from_name(url):
    # Find the start of the relevant path
    start = url.find("preprocessed//") + len("preprocessed//")
    return url[start:]


def joinPath(path_base, path):
    return os.path.join(path_base, path)


def extract_time_range(csv_file, start, end):
    df = pd.read_csv(csv_file)
    filtered_df = df[(df['Time'] >= start) & (df['Time'] <= end)]
    return filtered_df['2: preprocessed'].values


# Load label data
label_data = pd.read_csv(label_file_path)
extracted_data = []

for index, row in label_data.iterrows():
    file_path = joinPath(csv_path_base, extract_path_from_name(row["csv"]))

    # we do not have all files locally
    if not check_file_exists(file_path):
        continue

    data = extract_time_range(csv_file=file_path, start=row['start'], end=row['end'])
    extracted_data.append(data)

# Convert the extracted data to a DataFrame
extracted_df = pd.DataFrame(extracted_data)

# Save the extracted data to a CSV file
extracted_output_file = '/Users/pawelmanczak/Downloads/pacjenci/extracted_data.csv'
extracted_df.to_csv(extracted_output_file, index=False)

print(f"Extracted data saved to {extracted_output_file}")

for row in extracted_data:
    print(len(row))
