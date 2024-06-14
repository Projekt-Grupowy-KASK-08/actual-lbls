import requests

# Konfiguracja
base_url = 'http://localhost/dbs/labels/api/'
token = 'f6431894b13286720025e5a23b50652095b74cf9'
headers = {
    'Authorization': f'Token {token}',
    'Content-Type': 'application/json'
}


# Funkcja do pobierania wszystkich ID ML backendów
def get_ml_backend_ids():
    ml_backend_ids = []
    url = f'{base_url}/ml'
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        try:
            ml_backends = response.json()
            print("Odpowiedź serwera:", ml_backends)  # Dodano wyświetlanie odpowiedzi serwera
            for ml_backend in ml_backends:
                ml_backend_ids.append(ml_backend['id'])
        except ValueError as e:
            print(f'Błąd dekodowania JSON: {e}')
    else:
        print(f'Błąd podczas pobierania ML backendów: {response.status_code}')
        print(f'Odpowiedź serwera: {response.text}')

    return ml_backend_ids


# Funkcja do usuwania ML backendu według ID
def delete_ml_backend(ml_backend_id):
    url = f'{base_url}/ml/{ml_backend_id}'
    response = requests.delete(url, headers=headers)

    if response.status_code == 204:
        print(f'Usunięto ML backend ID: {ml_backend_id}')
    else:
        print(f'Błąd podczas usuwania ML backendu ID: {ml_backend_id} - Status: {response.status_code}')
        print(f'Odpowiedź serwera: {response.text}')


# Główna funkcja
def main():
    ml_backend_ids = get_ml_backend_ids()
    if not ml_backend_ids:
        print('Nie znaleziono żadnych ML backendów do usunięcia.')
        return

    for ml_backend_id in ml_backend_ids:
        delete_ml_backend(ml_backend_id)


if __name__ == '__main__':
    main()
