import requests

from constants import API_KEY, BASE_URL


def get_task_id_and_filename_pairs_by_project_id(project_id, api_url=BASE_URL + "/tasks/", api_key=API_KEY):
    headers = {
        "Authorization": f"Token {api_key}"
    }

    url = api_url + "?project=" + str(project_id)

    response = requests.get(url, headers=headers)


    if response.status_code == 200:
        data = response.json()

        task_file_pairs = [(str(task['data']['csv']), task['id']) for task in data['tasks']]

        return task_file_pairs
    else:
        print(f"Failed to fetch tasks. Status code: {response.status_code}")
    return []


#print(get_task_id_and_filename_pairs_by_project_id(284))
