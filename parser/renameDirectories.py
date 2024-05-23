import os


def change_polish_characters(text):
    polish_chars_mapping = {
        'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n',
        'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z',
        'Ą': 'A', 'Ć': 'C', 'Ę': 'E', 'Ł': 'L', 'Ń': 'N',
        'Ó': 'O', 'Ś': 'S', 'Ź': 'Z', 'Ż': 'Z'
    }
    return ''.join(polish_chars_mapping.get(char, char) for char in text)


def rename_folders(root_directory):
    for dir_name in os.listdir(root_directory):
        dir_path = os.path.join(root_directory, dir_name)
        if os.path.isdir(dir_path):
            new_name = change_polish_characters(dir_name)
            if new_name != dir_name:
                new_path = os.path.join(root_directory, new_name)
                os.rename(dir_path, new_path)
                print(f"Folder '{dir_path}' renamed to '{new_path}'")


root_directory = r"D:\preprocessed"
rename_folders(root_directory)
