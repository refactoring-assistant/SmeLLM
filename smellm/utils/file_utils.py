import os
import json

def extract_file_content(file_path):
    """
    Extracts the content of a file and returns it as a string.

    :param file_path: Path to the file to be read.
    :return: Content of the file as a string.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def extract_folder_content(folder_path):
    """
    Extracts the content of all files in a folder and returns a dictionary with file names as keys and their content as values.

    :param folder_path: Path to the folder to be read.
    :return: Dictionary with file names as keys and their content as values.
    """
    content_dict = {}
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            content_dict[file] = extract_file_content(file_path)
    return content_dict

def extract_zip_content(zip_path):
    """
    Extracts the content of all files in a zip archive and returns a dictionary with file names as keys and their content as values.

    :param zip_path: Path to the zip archive to be read.
    :return: Dictionary with file names as keys and their content as values.
    """
    import zipfile
    content_dict = {}
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for file_info in zip_ref.infolist():
            if not file_info.is_dir():
                with zip_ref.open(file_info) as file:
                    content_dict[file_info.filename] = file.read().decode('utf-8')
    return content_dict

def read_json(path):
    """
    Reads a JSON file and returns its content as a Python object.
    
    :param path: Path to the JSON file.
    :return: Content of the JSON file as a Python object.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"The file {path} does not exist.")
    
    if not path.endswith('.json'):
        raise ValueError("The provided path is not a JSON file.")
    
    json_data = []
    with open(path, "r") as f:
        json_data = json.load(f)
    return json_data