import requests

base_url = 'http://localhost/dbs/labels/'
token = 'b0a04e88161975f85c20959eabfe373f26f8b2bd'
headers = {
    'Authorization': f'Token {token}',
    'Content-Type': 'application/json'
}


def get_prediction_ids():
    prediction_ids = []
    url = f'{base_url}/api/predictions'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        predictions = response.json()
        for prediction in predictions:
            prediction_ids.append(prediction['id'])
    else:
        print(f'Błąd podczas pobierania predykcji: {response.status_code}')
    return prediction_ids


def delete_prediction(prediction_id):
    url = f'{base_url}/api/predictions/{prediction_id}'
    response = requests.delete(url, headers=headers)

    if response.status_code == 204:
        print(f'Usunięto predykcję ID: {prediction_id}')
    else:
        print(f'Błąd podczas usuwania predykcji ID: {prediction_id} - Status: {response.status_code}')



prediction_ids = get_prediction_ids()
if not prediction_ids:
    print('Nie znaleziono żadnych predykcji do usunięcia.')
else:
    for prediction_id in prediction_ids:
        delete_prediction(prediction_id)

