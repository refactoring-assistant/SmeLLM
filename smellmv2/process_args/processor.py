import os
import sys
from abc import ABC, abstractmethod

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from content_extractors.java.java_file_extractor import JavaFileExtractor
from content_extractors.typescript.typescript_file_extractor import TypeScriptFileExtractor
from chat_apis.prompt_engineering import Prompt
from chat_apis.oai.oai_apis import OAI


class Processor(ABC):
    def __init__(self, file_path, file_type, model_name="gpt-4o-mini"):
        self.model_name = model_name
        self.conversation_histories = []
        self.relative_paths = []
        match file_type:
            case "java":
                self.file_extractor = JavaFileExtractor()
            case "typescript":
                self.file_extractor = TypeScriptFileExtractor()
            case _:
                raise ValueError(f"Invalid file type: {file_type}")
        try:
            zipfile_content = self.content_extraction(file_path)
        except Exception as e:
            raise ValueError(f"Error in extracting zipfile: {e}")
        try:
            for relative_path, file_content in zipfile_content.items():
                self.relative_paths.append(relative_path)
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
                    response_dict = {}
                    for conversation_index in range(len(self.conversation_histories)):
                        response = oai.chat_completion(conversations_history=self.conversation_histories[conversation_index])
                        response_dict[self.relative_paths[conversation_index]] = response
                    return response_dict
                case _:
                    raise ValueError(f"Invalid API type: {api}")
            
        except Exception as e:
            raise ValueError(f"Error: {e}")
        
    @abstractmethod
    def content_extraction(self, file_path):
        '''Abstract method to extract content from file'''
        pass