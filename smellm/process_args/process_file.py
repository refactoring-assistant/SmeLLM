import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from process_args.processor import Processor

class ProcessFile(Processor):
        
    def content_extraction(self, file_path):
        return self.file_extractor.extract_content_single_file(file_path)
        
# define main
if __name__ == '__main__':
    file_path = r'trial-files\LargeClassBadExample.java'
    try:
        pf = ProcessFile(file_path, "java")
        response = pf.process()
        print(response)
    except Exception as e:
        print(f"Error: {e}")