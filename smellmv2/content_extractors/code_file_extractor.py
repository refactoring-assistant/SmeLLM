import os
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
        self._validate_file_path(path)
        
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
            raise ValueError(f"File at path {path} has an invalid extension. Expected one of: {', '.join(valid_extensions)}")
    
    @abstractmethod
    def get_valid_extensions(self):
        """Get the list of valid file extensions for this extractor.
        
        Returns:
            list: List of valid file extensions (including the dot).
        """
        pass