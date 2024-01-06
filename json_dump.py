import json

API_URL = 'http://localhost:8787'

def get_single_task(id, file_name):
    obj = {
            'id': id,
            'data': {
                'csv': API_URL + "/" + file_name
                }
            }
    return obj

def get_json(files_list):
    tasks = []
    for idx, file in enumerate(files_list):
        tasks.append(get_single_task(idx+1, file))
    with open('../projekt-grupowy/tasks.json', 'w') as outfile:
        json.dump(tasks, outfile, indent=4)

def main():
    files = ['testoweDane.csv', 'testoweDane2.csv']
    get_json(files)

if __name__== '__main__':
    main()

