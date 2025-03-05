import os
import zipfile
import tempfile
import shutil
from abc import ABC, abstractmethod

class CodeFileExtractor(ABC):
    """Base class for all code file extractors."""
    def __init__(self):
        self.extracted_path = None
    
    def extract_content_single_file(self, path):
        """Extract the content of a single code file.
        
        Args:
            path (str): Path to the file.
            
        Returns:
            str: Content of the file.
        """
        if not self._validate_file_path(path):
            raise ValueError(f"File at path {path} has an invalid extension. Expected one of: {', '.join(self.get_valid_extensions())}")
        
        return self._extract_single_file(path)
    
    def extract_content_zip_files(self, path):
        """Extract the content of all code files in a zip file.
        
        Args:
            path (str): Path to the zip file.
            
        Returns:
            dict: Dictionary where keys are file paths and values are file contents.
        """
        # Extract the zip file
        try:
            self.extracted_path = self._extract_zip_file(path)
        except Exception as e:
            raise ValueError(f"Error extracting zip file at path {path}: {e}")
        
        # Get the content of all code files
        content_dict = {}
        for root, _, files in os.walk(self.extracted_path):
            for file in files:
                file_path = os.path.join(root, file)
                if not self._validate_file_path(file_path):
                    continue
                content = self._extract_single_file(file_path)
                relative_path = os.path.relpath(file_path, self.extracted_path)
                content_dict[relative_path] = content
        
        return content_dict
    
    def cleanup_extracted_files(self):
        """Delete the extracted files from a zip file.
        
        Args:
            path (str): Path to the extracted directory.
        """
        if not self.extracted_path:
            raise ValueError("No extracted files to clean up.")
        shutil.rmtree(self.extracted_path)
        
    @abstractmethod
    def get_valid_extensions(self):
        """Get the list of valid file extensions for this extractor.
        
        Returns:
            list: List of valid file extensions (including the dot).
        """
        pass
    
    def _extract_single_file(self, path):
        """Extract the content of a single code file.
        
        Args:
            path (str): Path to the file.
            
        Returns:
            str: Content of the file.
        """
        with open(path, 'r') as file:
            content = file.read()
        return content
    
    def _validate_file_path(self, path):
            """Validate the file path.
            
            Args:
                path (str): Path to the file.
                
            Raises:
                ValueError: If the file does not exist or has an invalid extension.
            """
            if not os.path.exists(path):
                raise ValueError(f"File at path {path} does not exist.")
            
            # Check if the file has a valid extension
            valid_extensions = self.get_valid_extensions()
            if not any(path.endswith(ext) for ext in valid_extensions):
                return False
            return True
    
    def _extract_zip_file(self, path):
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
    
   