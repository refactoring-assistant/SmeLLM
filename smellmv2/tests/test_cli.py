import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tempfile
from smellm.cli import validate_paths

class Args:
    def __init__(self, file_path=None, folder_path=None, zip_path=None, eval=None):
        self.file_path = file_path
        self.folder_path = folder_path
        self.zip_path = zip_path
        self.eval = eval

def test_validate_paths_file_exists():
    with tempfile.NamedTemporaryFile() as tmp:
        args = Args(file_path=tmp.name)
        validate_paths(args)
        assert args.file_path == os.path.abspath(tmp.name)

def test_validate_paths_file_not_exists():
    args = Args(file_path="non_existent_file.txt")
    try:
        validate_paths(args)
    except SystemExit as e:
        assert str(e) == "Error: File 'non_existent_file.txt' does not exist."

def test_validate_paths_folder_exists():
    with tempfile.TemporaryDirectory() as tmpdir:
        args = Args(folder_path=tmpdir)
        validate_paths(args)
        assert args.folder_path == os.path.abspath(tmpdir)

def test_validate_folder_not_exists():
    args = Args(folder_path="non_existent_folder")
    try:
        validate_paths(args)
    except SystemExit as e:
        assert str(e) == "Error: Folder 'non_existent_folder' does not exist."

def test_validate_paths_zip_exists():
    with tempfile.NamedTemporaryFile(suffix=".zip") as tmp:
        args = Args(zip_path=tmp.name)
        validate_paths(args)
        assert args.zip_path == os.path.abspath(tmp.name)

def test_validate_paths_zip_not_exists():
    args = Args(zip_path="non_existent_file.zip")
    try:
        validate_paths(args)
    except SystemExit as e:
        assert str(e) == "Error: Zip file 'non_existent_file.zip' does not exist or is not a .zip file."