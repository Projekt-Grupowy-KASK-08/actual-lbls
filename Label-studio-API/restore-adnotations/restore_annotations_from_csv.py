import csv
import json

from constants import API_KEY, BASE_URL
from get_all_tasks_and_file_names import *

csv_file_path = '/Users/pawelmanczak/Downloads/24-05-2024_23-07-17.csv'
output_script_path = 'generate_annotations.sh'
url = BASE_URL + '/tasks'
tasks_id_and_filename_pairs = get_all_tasks_and_file_names()


def find_id_by_filename(files_with_tasks, filename):
    for file_name, file_id in files_with_tasks:
        if file_name == filename:
            return file_id
    return None


with open(csv_file_path, newline='') as csvfile, open(output_script_path, 'w') as script_file:
    reader = csv.DictReader(csvfile)

    script_file.write("#!/bin/bash\n\n")

    for row in reader:
        annotation_id = row['id']
        csv_name = row['csv']
        task_id = find_id_by_filename(tasks_id_and_filename_pairs, csv_name)

        label_data = json.loads(row['label'])

        for label_entry in label_data:
            start_time = label_entry['start']
            end_time = label_entry['end']
            label = label_entry['timeserieslabels'][0]  # todo
            text = row['text']

            curl_command = f"""
            
            
            curl -X POST {url}/{task_id}/annotations \\
     -H "Authorization: Token {API_KEY}" \\
     -H "Content-Type: application/json" \\
     -d '{{
  "result": [
    {{
    "value": {{
        "start": {start_time},
        "end": {end_time},
        "timeserieslabels": [
          "{label}"
        ]
      }},
      "from_name": "label",
      "to_name": "ts",
      "type": "timeserieslabels",
      "origin": "manual"
      
    }}
  ],
  "was_cancelled": false,
  "ground_truth": false
}}'\n\n"""

            script_file.write(curl_command)

print(f"Script saved in {output_script_path}")
