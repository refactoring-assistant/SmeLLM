import os
import sys

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from ..config.constants import LANGUAGE_EXTENSIONS

def get_file_extension(file_path):
    """
    Returns the file extension of the given file path.
    
    :param file_path: Path to the file.
    :return: File extension as a string.
    """
    _, ext = os.path.splitext(file_path)
    return ext.lower()

def extract_file_content(file_path, language=None):
    """
    Extracts the content of a file if it is of the given language (else skips) and returns it as a dictionary with file name as key and its content as value.

    :param file_path: Path to the file to be read.
    :return: Dictionary with file name as key and its content as value.
    """
    ext = get_file_extension(file_path)
    valid_exts = LANGUAGE_EXTENSIONS.get(language, []) if language else None
    if language is not None and (not valid_exts or ext not in valid_exts):
        return None
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        file_name = os.path.basename(file_path)
        return {file_name: content}

def extract_folder_content(folder_path, language=None):
    """
    Extracts the content of all files if it is of the given language (else skips) in a folder and returns a dictionary with file names as keys and their content as values.

    :param folder_path: Path to the folder to be read.
    :return: Dictionary with file names as keys and their content as values.
    """
    content_dict = {}
    valid_exts = LANGUAGE_EXTENSIONS.get(language, []) if language else None
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            rel_path = os.path.relpath(file_path, folder_path)
            ext = get_file_extension(file_path)
            if language is not None and (not valid_exts or ext not in valid_exts):
                continue
            with open(file_path, 'r', encoding='utf-8') as f:
                content_dict[rel_path] = f.read()
    return content_dict

def extract_zip_content(zip_path, language=None):
    """
    Extracts the content of all files in a zip archive and returns a dictionary with file names as keys and their content as values.

    :param zip_path: Path to the zip archive to be read.
    :return: Dictionary with file names as keys and their content as values.
    """
    import zipfile
    content_dict = {}
    valid_exts = LANGUAGE_EXTENSIONS.get(language, []) if language else None
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for file_info in zip_ref.infolist():
            if not file_info.is_dir():
                rel_path = file_info.filename
                ext = get_file_extension(rel_path)
                if language is not None and (not valid_exts or ext not in valid_exts):
                    continue
                with zip_ref.open(file_info) as file:
                    content_dict[rel_path] = file.read().decode('utf-8')
    return content_dict