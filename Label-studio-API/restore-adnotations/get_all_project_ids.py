import requests

from constants import API_KEY, BASE_URL


def get_all_project_ids(api_url =BASE_URL + "/projects?page_size=10000", api_key = API_KEY):
    headers = {
        "Authorization": f"Token {api_key}"
    }

    project_ids = []

    response = requests.get(api_url, headers=headers)
    data = response.json()
    #print(data)

    if response.status_code == 200:
        for project in data['results']:
            project_ids.append(project['id'])
    else:
        print(f"Error: {response.status_code}")

    return project_ids

#project_ids = getAllProjectIds()
#print(project_ids)
