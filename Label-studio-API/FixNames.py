import os
import re

PATH_TO_PATIENTS = r"C:\DBS archives"


def find_patient(id_operacji):
    for root, dirs, files in os.walk(PATH_TO_PATIENTS):
        for operation_dir in dirs:
            if operation_dir == id_operacji:
                return os.path.basename(root)
    return "Lack_of_patient_name"


def change_polish_characters(text):
    polish_chars_mapping = {
        'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n',
        'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z',
        'Ą': 'A', 'Ć': 'C', 'Ę': 'E', 'Ł': 'L', 'Ń': 'N',
        'Ó': 'O', 'Ś': 'S', 'Ź': 'Z', 'Ż': 'Z'
    }
    return ''.join(polish_chars_mapping.get(char, char) for char in text)


def get_date(patient_name, operation_id):
    if patient_name != "Lack_of_patient_name":
        try:
            with open(os.path.join(PATH_TO_PATIENTS, patient_name, operation_id, "protokoll.txt"), 'r') as file:
                line = file.readline()
            pattern = r'\d{4}[-/]\d{2}[-/]\d{2}'
            result = re.search(pattern, line)
            if result:
                return result.group(0).replace('/', '-')
        except FileNotFoundError:
            return "Lack_of_date"
    return "Lack_of_date"
