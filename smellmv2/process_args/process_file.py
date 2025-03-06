import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from content_extractors.java.java_file_extractor import JavaFileExtractor
from content_extractors.typescript.typescript_file_extractor import TypeScriptFileExtractor
from chat_apis.prompt_engineering import Prompt
from chat_apis.oai.oai_apis import OAI

class ProcessFile():
    def __init__(self, file_path, file_type, model_name="gpt-4o-mini"):
        self.model_name = model_name
        match file_type:
            case "java":
                self.file_extractor = JavaFileExtractor()
            case "typescript":
                self.file_extractor = TypeScriptFileExtractor()
            case _:
                raise ValueError(f"Invalid file type: {file_type}")
        try:
            file_content = self.file_extractor.extract_content_single_file(file_path)
        except Exception as e:
            raise ValueError(f"Error in extracting file: {e}")
        try:
            formatted_user_input = f"{file_path} : {file_content}"
            prompt_generator = Prompt(formatted_user_input)
            self.conversation_history = prompt_generator.get_conversation_start()
        except Exception as e:
            raise ValueError(f"Error in generating prompts: {e}")
        
    def process(self, api="OAI"):
        try:  
            match api:
                case "OAI":
                    oai = OAI(self.model_name)
                    response = oai.chat_completion(conversations_history=self.conversation_history)
                    return response
                case _:
                    raise ValueError(f"Invalid API type: {api}")
            
        except Exception as e:
            raise ValueError(f"Error: {e}")
        
# define main
if __name__ == '__main__':
    file_path = r'trial-files\LargeClassBadExample.java'
    try:
        pf = ProcessFile(file_path, "java")
        response = pf.process()
        print(response)
    except Exception as e:
        print(f"Error: {e}")