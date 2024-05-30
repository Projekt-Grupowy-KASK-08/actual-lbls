import csv
import json

URL_FILE_ADDRESS = 'http://localhost/dbs/static//'
PATIENTS_DIRECTORY_PATH = 'C:/semestr 6/actual-lbls/http-server/data/'

def get_label_data(csv_file_path):
    annotations = []
    with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            file_path = row['csv'].replace(URL_FILE_ADDRESS, PATIENTS_DIRECTORY_PATH)
            if row['label']:
                try:
                    label_data = json.loads(row['label'])
                    for entry in label_data:
                        start = entry['start']
                        end = entry['end']
                        timeserieslabels = entry['timeserieslabels']
                        annotations.append(
                            {'csv': file_path, 'start': start, 'end': end, 'timeserieslabels': timeserieslabels})
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON for row {row['id']}: {e}")
            else:
                print(f"Empty 'label' field in row {row['id']}")
    with open("label.csv", mode='w', encoding='utf-8', newline='') as outfile:
        fieldnames = ['csv', 'start', 'end', 'timeserieslabels']
        csvwriter = csv.DictWriter(outfile, fieldnames=fieldnames)
        csvwriter.writeheader()
        for annotation in annotations:
            csvwriter.writerow(annotation)