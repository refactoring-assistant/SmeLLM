import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from content_extractors.java.java_file_extractor import JavaFileExtractor
from content_extractors.typescript.typescript_file_extractor import TypeScriptFileExtractor
from chat_apis.prompt_engineering import Prompt
from chat_apis.oai.oai_apis import OAI

class ProcessFolder():
    def __init__(self, file_path, file_type, model_name="gpt-4o-mini"):
        self.model_name = model_name
        self.conversation_histories = []
        match file_type:
            case "java":
                self.file_extractor = JavaFileExtractor()
            case "typescript":
                self.file_extractor = TypeScriptFileExtractor()
            case _:
                raise ValueError(f"Invalid file type: {file_type}")
        try:
            folder_content = self.file_extractor.extract_folder_files(file_path)
        except Exception as e:
            raise ValueError(f"Error in extracting folder: {e}")
        try:
            for relative_path, file_content in folder_content.items():
                formatted_user_input = f"{relative_path} : {file_content}"
                prompt_generator = Prompt(formatted_user_input)
                self.conversation_histories.append(prompt_generator.get_conversation_start())
        except Exception as e:
            raise ValueError(f"Error in generating prompts: {e}")

    def process(self, api="OAI"):
        try:  
            match api:
                case "OAI":
                    oai = OAI(self.model_name)
                    response_list = []
                    for conversation_history in self.conversation_histories:
                        response = oai.chat_completion(conversations_history=conversation_history)
                        response_list.append(response)
                    return response_list
                case _:
                    raise ValueError(f"Invalid API type: {api}")
            
        except Exception as e:
            raise ValueError(f"Error: {e}")