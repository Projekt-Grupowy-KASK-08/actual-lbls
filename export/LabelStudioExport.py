import requests
import pandas as pd
import io
from datetime import datetime
from parseLabel import get_label_data

API_KEY = '1c0d537815c777dd0394938b9b1a6c849cb5de84'
LABEL_STUDIO_URL = 'https://kask.eti.pg.edu.pl/dbs/labels/'
FIRST_ID = 1631
LAST_ID = 1914


def fetch_project_data(project_id):
    response = requests.get(
        f'{LABEL_STUDIO_URL}/api/projects/{project_id}/export?exportType=CSV',
        headers={'Authorization': f'Token {API_KEY}'}
    )
    if response.status_code == 200:
        return pd.read_csv(io.StringIO(response.content.decode('utf-8')))
    else:
        print("Błąd przy pobieraniu danych dla projektu", project_id, ":", response.status_code)
        return pd.DataFrame()


all_data = pd.DataFrame()
for id in range(FIRST_ID, LAST_ID+1):
    print("Pobieranie danych dla projektu", id)
    project_data = fetch_project_data(id)
    if not project_data.empty:
        all_data = pd.concat([all_data, project_data], ignore_index=True)
    else:
        print(f"Brak danych dla projektu {id}")



now = datetime.now()
dt_string = now.strftime("%d-%m-%Y_%H-%M-%S")
file_name = dt_string+".csv"
all_data.to_csv(file_name, index=False)
print("Dane zostały zapisane do pliku " + dt_string + ".csv")
get_label_data(file_name)
print("Wyodrębnione dane zostały zapisane do pliku label.csv")