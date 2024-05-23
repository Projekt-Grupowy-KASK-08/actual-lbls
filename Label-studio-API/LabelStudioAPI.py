import os
from FixNames import get_date, change_polish_characters, find_patient
import re
LABEL_STUDIO_URL = 'http://localhost/dbs/labels/'
FILE_SERVER_URL = 'http://localhost/dbs/static/'
OUTPUT_DIR = r"C:\semestr 6\actual-lbls\Label-studio-API"  # path where ProjectParameters.txt is and to save the script
INPUT_DIR = r"C:\semestr 6\actual-lbls\http-server\data"  # path to the directory that contains patients directories
PROJECT_ID_OFFSET = 45  # id ze sciezki url ostatnio utworzonego projektu (lewy gorny rog)
TOKEN = "bf7e7d843681e97e6a0bc32535cb26a69fbae376"


def get_data_for_project(id_chart, patient_name, operation_id, file_name, f_p, last):
    match = re.match(r'depth(?P<depth>-?\d+,\d+)_kanal(?P<kanal>\w+)\.csv', file_name)
    depth = "Lack_of_depth"
    chanel = "Lack_of_chanel"
    if match:
        depth = match.group('depth')
        chanel = match.group('kanal')
    else:
        print("Nie znaleziono odpowiadających wzorców.")
    f_p.write("\n")
    f_p.write("{\n\"id\": "+str(id_chart)+",\n")
    f_p.write("\"data\": {")
    f_p.write("\"csv\": \""+FILE_SERVER_URL + "/" + patient_name + "/" + operation_id + "/" + file_name + "\",")
    f_p.write("\"text\": \"" + "Depth: " + depth + " mm " + " Channel: " + chanel + "\"")
    if last:
        f_p.write("}\n},")
    else:
        f_p.write("}\n}")

def get_project_script(patient_names_list):
    with open(OUTPUT_DIR+'/ProjectParameters.txt', 'r') as source_file:
        parameters = source_file.read()
        project_id = 0
    f_p = open(OUTPUT_DIR + "/CreateProjects.sh", "w")
    for patient_name in patient_names_list:  # loop through patient directories
        patient_path = os.path.join(INPUT_DIR, patient_name)
        patient_name = change_polish_characters(patient_name)
        for operation_id in os.listdir(patient_path):  # loop through operation directories
            if check_if_directory_is_not_empty(os.path.join(patient_path, operation_id)):  # if directory is not empty
                # "create project" command BEGIN
                f_p.write("curl -v -k -H Content-Type:application/json -H 'Authorization: Token "+TOKEN+"' -X POST '" + LABEL_STUDIO_URL +\
                          "/api/projects' --data '{ \n\"title\": \"")

                f_p.write(patient_name+" "+str(get_date(find_patient(operation_id), operation_id)))
                f_p.write("\",")
                f_p.write("\n")
                f_p.write(parameters)
                f_p.write("\n")
                f_p.write("}'")
                f_p.write("\n")
                f_p.write("\n")
                # "create project" command END
                project_id += 1
                # "create import for project" command BEGIN
                f_p.write("curl -H 'Content-Type: application/json' -H 'Authorization: Token "+TOKEN+"' -X POST '"\
                          + LABEL_STUDIO_URL + "/api/projects/"+str(PROJECT_ID_OFFSET+project_id)+"/import' -d '[")
                chart_id = 0
                file_names = [f for f in os.listdir(os.path.join(patient_path, operation_id)) if
                              os.path.isfile(os.path.join(os.path.join(patient_path, operation_id), f))]  #  get all files inside patient/operation
                for idx, file in enumerate(file_names):
                    chart_id += 1
                    last = True
                    if idx == len(file_names)-1:
                        last = False
                    get_data_for_project(chart_id, patient_name, operation_id, file, f_p, last)
                f_p.write("\n")
                f_p.write("]'")
                f_p.write("\n")
                f_p.write("\n")
                # "create import for project" command END
    f_p.close()


def check_if_directory_is_not_empty(path):
    if os.listdir(path):
        return True
    else:
        print("folder " + str(path) + " is empty, skipping")
        return False


if not os.path.exists(OUTPUT_DIR):
    print('output directory ' + OUTPUT_DIR + "doesn't exist")
if not os.path.exists(INPUT_DIR):
    print('input directory ' + INPUT_DIR + "doesn't exist")
else:
    patientsDirectories = os.listdir(INPUT_DIR)
    get_project_script(patientsDirectories)



