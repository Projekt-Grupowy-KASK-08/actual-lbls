Module to restore annotations saved in csv file to server.

restore_annotations_from_csv.py - script creating curl file to add annotations into Label Studio.
get_all_project_ids.py - script to get all project ids from Label Studio, needed to get all tasks.
get_task_id_and_filename_pairs_by_project_id.py - script to get data we need from tasks (file name and id).
get_all_tasks_and_file_names.py - script using two above scripts and returning all tasks with file names.
constraints.py - file consts

generated file:
generate_annotations.sh - if you run this it will send requests to Label Studio API to add annotations to tasks.

how to use:
1. Set path to csv in restore_annotations_from_csv.py
2. Run restore_annotations_from_csv.py
3. Run generate_annotations.sh

that's it, annotations should be restored.

