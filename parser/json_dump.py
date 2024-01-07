import json
import os, re, sys

API_URL = 'http://localhost:8787'
INPUT_DIR = sys.path[0] + "/data/preprocessed"
OUTPUT_DIR = sys.path[0] + "/data/preprocessed"

def get_single_task(id, patient_name, operation_id, file_name):
    obj = {
            'id': id,
            'data': {
                'csv': API_URL + "/" + patient_name + "/" + operation_id + "/" + file_name
                }
            }
    return obj

def get_json(patient_names_list):
    tasks = []
    for patient_name in patient_names_list:
        patientPath = os.path.join(INPUT_DIR, patient_name)
        for operation_id in os.listdir(patientPath):
            file_names = [f for f in os.listdir(os.path.join(patientPath, operation_id)) if os.path.isfile(os.path.join(os.path.join(patientPath, operation_id), f))]
            for idx, file in enumerate(file_names):
                tasks.append(get_single_task(idx+1, patient_name, operation_id, file))
                with open(OUTPUT_DIR+"/tasks.json", 'w') as outfile:
                    json.dump(tasks, outfile, indent=4)

def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    patientsDirectories = os.listdir(INPUT_DIR)
    print(patientsDirectories)
    patientsNumber = len(patientsDirectories)
    get_json(patientsDirectories)

if __name__== '__main__':
    main()

