import os
import zipfile
import tempfile
import shutil
from abc import ABC, abstractmethod

class CodeFileExtractor(ABC):
    """Base class for all code file extractors."""
    def extract_content_single_file(self, path):
        """Extract the content of a single code file.
        
        Args:
            path (str): Path to the file.
            
        Returns:
            str: Content of the file.
        """
        if not self.__validate_file_path(path):
            raise ValueError(f"File at path {path} has an invalid extension. Expected one of: {', '.join(self.get_valid_extensions())}")
        
        return self.__extract_single_file(path)
    
    def extract_folder_files(self, path):
        """Extract the content of all code files in a folder.
        
        Args:
            path (str): Path to the folder.
            
        Returns:
            dict: Dictionary where keys are file paths and values are file contents.
        """
        return self.__extract_directory(path)
        
    
    def extract_content_zip_files(self, path):
        """Extract the content of all code files in a zip file.
        
        Args:
            path (str): Path to the zip file.
            
        Returns:
            dict: Dictionary where keys are file paths and values are file contents.
        """
        # Extract the zip file
        try:
            extracted_path = self.__extract_zip_file(path)
        except Exception as e:
            raise ValueError(f"Error extracting zip file at path {path}: {e}")
        content = self.__extract_directory(extracted_path)
        shutil.rmtree(extracted_path)
        return content
        
    @abstractmethod
    def get_valid_extensions(self):
        """Get the list of valid file extensions for this extractor.
        
        Returns:
            list: List of valid file extensions (including the dot).
        """
        pass
    
    def __extract_single_file(self, path):
        """Extract the content of a single code file.
        
        Args:
            path (str): Path to the file.
            
        Returns:
            str: Content of the file.
        """
        with open(path, 'r', encoding='utf-8', errors='replace') as file:
            lines = file.readlines()
    
        # Add line numbers in the specified format
        numbered_lines = [f"(~{i+1}~) {line.rstrip()}" for i, line in enumerate(lines)]
        
        # Join the numbered lines back into a single string
        content_with_numbers = "\n".join(numbered_lines)
    
        return content_with_numbers
    
    def __validate_file_path(self, path):
            """Validate the file path.
            
            Args:
                path (str): Path to the file.
                
            Raises:
                ValueError: If the file does not exist or has an invalid extension.
            """
            if not os.path.exists(path):
                raise ValueError(f"File at path {path} does not exist.")
            
            if not os.path.isfile(path):
                raise ValueError(f"Path {path} is not a file.")
            
            # Check if the file has a valid extension
            valid_extensions = self.get_valid_extensions()
            if not any(path.endswith(ext) for ext in valid_extensions):
                return False
            return True
    
    def __extract_zip_file(self, path):
        """Extract a zip file to a temporary directory.
        
        Args:
            path (str): Path to the zip file.
            
        Returns:
            str: Path to the extracted directory.
        """
        if not zipfile.is_zipfile(path):
            raise ValueError(f"File at path {path} is not a valid zip file.")
        try:
            with zipfile.ZipFile(path, 'r') as zip_ref:
                temp_dir = tempfile.mkdtemp()
                zip_ref.extractall(temp_dir)
        except Exception as e:
            raise ValueError(f"Error extracting zip file at path {path}: {e}")
        
        return temp_dir
    
    def __extract_directory(self, dir_path):
        if not os.path.exists(dir_path):
            raise ValueError(f"Directory at path {dir_path} does not exist.")
        if not os.path.isdir(dir_path):
            raise ValueError(f"Path {dir_path} is not a directory.")
        
        content_dict = {}
        for root, _, files in os.walk(dir_path):
            for file in files:
                file_path = os.path.join(root, file)
                if not self.__validate_file_path(file_path):
                    continue
                content = self.__extract_single_file(file_path)
                relative_path = os.path.relpath(file_path, dir_path)
                content_dict[relative_path] = content
        return content_dict
   