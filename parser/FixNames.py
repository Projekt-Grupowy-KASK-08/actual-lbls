import os
import re
PATH_TO_PATIENTS = 'C:/DBS archives'
def find_patient(id_operacji):
    for root, dirs, files in os.walk(PATH_TO_PATIENTS):
        for dir in dirs:
            if dir == id_operacji:
                return os.path.basename(root)
    return "Lack_of_patient_name"


def get_date(patient_name, operation_id):
    with open(os.path.join(PATH_TO_PATIENTS, patient_name, operation_id, "protokoll.txt"), 'r') as file:
        line = file.readline()
    pattern = r'\d{4}[-/]\d{2}[-/]\d{2}'
    result = re.search(pattern, line)

    if result:
        return result.group(0).replace('/', '-')
    else:
        return "Lack_of_date"


