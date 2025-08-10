import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tempfile

from smellm.utils.file_utils import extract_file_content, extract_folder_content, extract_zip_content, get_file_extension

def test_extract_supported_file_content():
    with tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8', suffix=".java") as tmpfile:
        tmpfile.write("This is a test file content.")
        tmpfile_path = tmpfile.name

    content = extract_file_content(tmpfile_path, language="java")

    rel_file_path = os.path.relpath(tmpfile_path, os.path.dirname(tmpfile_path))

    assert content[rel_file_path] == "This is a test file content."

    os.remove(tmpfile_path)

def test_extract_unsupported_file_content():
    with tempfile.NamedTemporaryFile(delete=False, mode='w', encoding='utf-8', suffix=".txt") as tmpfile:
        tmpfile.write("This is a test file content.")
        tmpfile_path = tmpfile.name

    content = extract_file_content(tmpfile_path, language="java")

    assert content is None

    os.remove(tmpfile_path)


def test_extract_folder_content():
    with tempfile.TemporaryDirectory() as tmpdir:
        file1_path = os.path.join(tmpdir, "file1.java")
        file2_path = os.path.join(tmpdir, "file2.java")

        with open(file1_path, 'w', encoding='utf-8') as f:
            f.write("Content of file 1")
        with open(file2_path, 'w', encoding='utf-8') as f:
            f.write("Content of file 2")

        content_dict = extract_folder_content(tmpdir)

        assert content_dict[os.path.relpath(file1_path, tmpdir)] == "Content of file 1"
        assert content_dict[os.path.relpath(file2_path, tmpdir)] == "Content of file 2"

def test_extract_folder_contents_with_unsupported_files():
    with tempfile.TemporaryDirectory() as tmpdir:
        file1_path = os.path.join(tmpdir, "file1.java")
        file2_path = os.path.join(tmpdir, "file2.txt")
        
        with open(file1_path, 'w', encoding='utf-8') as f:
            f.write("Content of file 1")
        with open(file2_path, 'w', encoding='utf-8') as f:
            f.write("Content of file 2")

        content_dict = extract_folder_content(tmpdir, language="java")
        
        assert content_dict[os.path.relpath(file1_path, tmpdir)] == "Content of file 1"
        assert os.path.relpath(file2_path, tmpdir) not in content_dict

def test_extract_folder_content_deep():
    with tempfile.TemporaryDirectory() as tmpdir:
        subdir = os.path.join(tmpdir, "subdir")
        os.makedirs(subdir)

        subsubdir = os.path.join(subdir, "subsubdir")
        os.makedirs(subsubdir)

        file1_path = os.path.join(tmpdir, "file1.java")
        file2_path = os.path.join(subdir, "file2.java")
        file3_path = os.path.join(subsubdir, "file3.java")

        with open(file1_path, 'w', encoding='utf-8') as f:
            f.write("Content of file 1")
        with open(file2_path, 'w', encoding='utf-8') as f:
            f.write("Content of file 2")
        with open(file3_path, 'w', encoding='utf-8') as f:
            f.write("Content of file 3")

        content_dict = extract_folder_content(tmpdir)

        assert content_dict[os.path.relpath(file1_path, tmpdir)] == "Content of file 1"
        assert content_dict[os.path.relpath(file2_path, tmpdir)] == "Content of file 2"
        assert content_dict[os.path.relpath(file3_path, tmpdir)] == "Content of file 3"

def test_extract_folder_same_file_name_in_different_folders():
    with tempfile.TemporaryDirectory() as tmpdir:
        subdir1 = os.path.join(tmpdir, "subdir1")
        os.makedirs(subdir1)

        subdir2 = os.path.join(tmpdir, "subdir2")
        os.makedirs(subdir2)

        file_path1 = os.path.join(subdir1, "file.java")
        file_path2 = os.path.join(subdir2, "file.java")

        with open(file_path1, 'w', encoding='utf-8') as f:
            f.write("Content of file in subdir1")
        with open(file_path2, 'w', encoding='utf-8') as f:
            f.write("Content of file in subdir2")

        content_dict = extract_folder_content(tmpdir)

        assert content_dict[os.path.relpath(file_path1, tmpdir)] == "Content of file in subdir1"
        assert content_dict[os.path.relpath(file_path2, tmpdir)] == "Content of file in subdir2"

def test_extract_zip_content():
    import zipfile

    with tempfile.TemporaryDirectory() as tmpdir:
        file1_path = os.path.join(tmpdir, "file1.java")
        file2_path = os.path.join(tmpdir, "file2.java")

        with open(file1_path, 'w', encoding='utf-8') as f:
            f.write("Content of file 1")
        with open(file2_path, 'w', encoding='utf-8') as f:
            f.write("Content of file 2")

        zip_path = os.path.join(tmpdir, "test.zip")
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            zipf.write(file1_path, arcname="file1.java")
            zipf.write(file2_path, arcname="file2.java")

        content_dict = extract_zip_content(zip_path)

        assert content_dict[os.path.relpath(file1_path, tmpdir)] == "Content of file 1"
        assert content_dict[os.path.relpath(file2_path, tmpdir)] == "Content of file 2"

def test_get_file_extension():
    with tempfile.NamedTemporaryFile(delete=False, suffix='.java') as tmpfile:
        tmpfile_path = tmpfile.name
        
    ext = get_file_extension(tmpfile_path)
    assert ext == '.java'
    
    os.remove(tmpfile_path)
