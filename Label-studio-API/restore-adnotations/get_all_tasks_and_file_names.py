from get_all_project_ids import get_all_project_ids
from get_task_id_and_filename_pairs_by_project_id import get_task_id_and_filename_pairs_by_project_id


def get_all_tasks_and_file_names():
    ids = get_all_project_ids()
    files_with_tasks = []

    for project_id in ids:
        files_with_tasks.extend(get_task_id_and_filename_pairs_by_project_id(project_id))

    # print(files_with_tasks)
    return files_with_tasks


"""items = getAllTasksAndFileNames()

# print(items)
for item in items:
    print(item[0])"""
