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
    return path_base + path


def extract_time_range(csv_file, start, end):
    df = pd.read_csv(csv_file)
    filtered_df = df[(df['Time'] >= start) & (df['Time'] <= end)]
    return filtered_df['2: preprocessed'].values


label_data = pd.read_csv(label_file_path)
extracted_data = []

for index, row in label_data.iterrows():
    print()
    print(extract_path_from_name(row["csv"]))
    print(joinPath(csv_path_base, extract_path_from_name(row["csv"])))

    # we do not have all files locally
    if not check_file_exists(joinPath(csv_path_base, extract_path_from_name(row["csv"]))):
        continue

    data = extract_time_range(
        csv_file=joinPath(csv_path_base, extract_path_from_name(row["csv"])),
        start=row['start'],
        end=row['end'])
    extracted_data.append(data)


extracted_df = pd.DataFrame(extracted_data)
print(extracted_df)

for row in extracted_data:
    #print(row)
    print(len(row))

