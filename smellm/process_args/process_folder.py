import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from process_args.processor import Processor

class ProcessFolder(Processor):

    def content_extraction(self, file_path):
        return self.file_extractor.extract_folder_files(file_path)