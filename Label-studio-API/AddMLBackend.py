import requests

# Konfiguracja
base_url = 'http://localhost/dbs/labels/api'
token = '07df1e9f0377286a6c6d6e4e5021de1af5736dd8'
headers = {
    'Authorization': f'Token {token}',
    'Content-Type': 'application/json'
}

ml_backend_url = 'http://ml-backend:9090'  # Adres ML Backend

FIRTS_PROJECT_ID = 1
LAST_PROJECT_ID = 6


def add_ml_backend_to_project(project_id):
    url = f'{base_url}/ml'
    data = {
        'project': project_id,
        'url': ml_backend_url,
        'title': 'My ML Backend',
        'description': 'Automated ML backend for project'
    }
    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 201:
        print(f'Dodano ML backend do projektu ID: {project_id}')
    else:
        print(f'Błąd podczas dodawania ML backend do projektu ID: {project_id} - Status: {response.status_code}')
        print(f'Odpowiedź serwera: {response.text}')


for project_id in range(FIRTS_PROJECT_ID, LAST_PROJECT_ID + 1):
    add_ml_backend_to_project(project_id)
