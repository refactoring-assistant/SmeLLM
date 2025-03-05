import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from content_extractors.code_file_extractor import CodeFileExtractor
import config.constants as constants

class TypeScriptFileExtractor(CodeFileExtractor):
    """Class for extracting content from TypeScript files."""
    
    def get_valid_extensions(self):
        """Get the list of valid TypeScript file extensions.
        
        Returns:
            list: List of valid TypeScript file extensions.
        """
        return [constants.TYPESCRIPT_FILE_EXTENSION, constants.TYPESCRIPT_JSX_FILE_EXTENSION]

    

if __name__ == '__main__':
    tsfe = TypeScriptFileExtractor()
    illegalpath = r'trial-files\LargeClassBadExample'
    pythonpath = r'trial-files\interface_chat_api.py'
    legalpath = r'trial-files\DataClassBadExample.ts'
    zipfile = r'trial-files\trial.zip'
    try:
        content = tsfe.extract_content_single_file(illegalpath)
    except Exception as e:
        print(f"Error: {e}")
        
    try:
        content = tsfe.extract_content_single_file(pythonpath)
    except Exception as e:
        print(f"Error: {e}")
    
    try:
        content = tsfe.extract_content_single_file(legalpath)
        print(content)
    except Exception as e:
        print(f"Error: {e}")
    
    try:
        content_dict = tsfe.extract_content_zip_files(zipfile)
        print(content_dict)
        try:
            tsfe.cleanup_extracted_files()
        except Exception as e:
            print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
        
    