import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tempfile

from smellm.utils import extract_file_content, extract_folder_content, extract_zip_content

def test_extract_file_content():
    with tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8') as tmpfile:
        tmpfile.write("This is a test file content.")
        tmpfile_path = tmpfile.name

    content = extract_file_content(tmpfile_path)

    assert content == "This is a test file content."

    os.remove(tmpfile_path)

def test_extract_folder_content():
    with tempfile.TemporaryDirectory() as tmpdir:
        file1_path = os.path.join(tmpdir, "file1.txt")
        file2_path = os.path.join(tmpdir, "file2.txt")

        with open(file1_path, 'w', encoding='utf-8') as f:
            f.write("Content of file 1")
        with open(file2_path, 'w', encoding='utf-8') as f:
            f.write("Content of file 2")

        content_dict = extract_folder_content(tmpdir)

        assert content_dict["file1.txt"] == "Content of file 1"
        assert content_dict["file2.txt"] == "Content of file 2"

def test_extract_folder_content_deep():
    with tempfile.TemporaryDirectory() as tmpdir:
        subdir = os.path.join(tmpdir, "subdir")
        os.makedirs(subdir)

        subsubdir = os.path.join(subdir, "subsubdir")
        os.makedirs(subsubdir)

        file1_path = os.path.join(tmpdir, "file1.txt")
        file2_path = os.path.join(subdir, "file2.txt")
        file3_path = os.path.join(subsubdir, "file3.txt")

        with open(file1_path, 'w', encoding='utf-8') as f:
            f.write("Content of file 1")
        with open(file2_path, 'w', encoding='utf-8') as f:
            f.write("Content of file 2")
        with open(file3_path, 'w', encoding='utf-8') as f:
            f.write("Content of file 3")

        content_dict = extract_folder_content(tmpdir)

        assert content_dict["file1.txt"] == "Content of file 1"
        assert content_dict["file2.txt"] == "Content of file 2"
        assert content_dict["file3.txt"] == "Content of file 3"

def test_extract_folder_same_file_name_in_different_folders():
    with tempfile.TemporaryDirectory() as tmpdir:
        subdir1 = os.path.join(tmpdir, "subdir1")
        os.makedirs(subdir1)

        subdir2 = os.path.join(tmpdir, "subdir2")
        os.makedirs(subdir2)

        file_path1 = os.path.join(subdir1, "file.txt")
        file_path2 = os.path.join(subdir2, "file.txt")

        with open(file_path1, 'w', encoding='utf-8') as f:
            f.write("Content of file in subdir1")
        with open(file_path2, 'w', encoding='utf-8') as f:
            f.write("Content of file in subdir2")

        content_dict = extract_folder_content(tmpdir)

        assert content_dict["file.txt"] == "Content of file in subdir1"
        assert content_dict["file.txt"] == "Content of file in subdir2"

def test_extract_zip_content():
    import zipfile

    with tempfile.TemporaryDirectory() as tmpdir:
        file1_path = os.path.join(tmpdir, "file1.txt")
        file2_path = os.path.join(tmpdir, "file2.txt")

        with open(file1_path, 'w', encoding='utf-8') as f:
            f.write("Content of file 1")
        with open(file2_path, 'w', encoding='utf-8') as f:
            f.write("Content of file 2")

        zip_path = os.path.join(tmpdir, "test.zip")
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            zipf.write(file1_path, arcname="file1.txt")
            zipf.write(file2_path, arcname="file2.txt")

        content_dict = extract_zip_content(zip_path)

        assert content_dict["file1.txt"] == "Content of file 1"
        assert content_dict["file2.txt"] == "Content of file 2"
