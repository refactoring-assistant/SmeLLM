import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from process_args.processor import Processor

class ProcessZipFile(Processor):
        
    def content_extraction(self, file_path):
        return self.file_extractor.extract_content_zip_files(file_path)