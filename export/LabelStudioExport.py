import requests
import pandas as pd
import io
from datetime import datetime
from parseLabel import get_label_data

API_KEY = 'bf7e7d843681e97e6a0bc32535cb26a69fbae376'
LABEL_STUDIO_URL = 'http://localhost/dbs/labels/'


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


projects_response = requests.get(
    f'{LABEL_STUDIO_URL}/api/projects/',
    headers={'Authorization': f'Token {API_KEY}'}
)
if projects_response.status_code == 200:
    projects = projects_response.json()['results']
else:
    print("Błąd przy pobieraniu listy projektów:", projects_response.status_code)
    projects = []

all_data = pd.DataFrame()
for project in projects:
    if 'id' in project:  # Sprawdzanie, czy klucz 'id' istnieje w słowniku
        print("Pobieranie danych dla projektu", project['id'])
        project_data = fetch_project_data(project['id'])
        if not project_data.empty:
            all_data = pd.concat([all_data, project_data], ignore_index=True)
        else:
            print(f"Brak danych dla projektu {project['id']}")
    else:
        print("Nieprawidłowa struktura danych projektu:", project)


now = datetime.now()
dt_string = now.strftime("%d-%m-%Y_%H-%M-%S")
file_name = dt_string+".csv"
all_data.to_csv(file_name, index=False)
print("Dane zostały zapisane do pliku " + dt_string + ".csv")
get_label_data(file_name)
print("Wyodrębnione dane zostały zapisane do pliku label.csv")