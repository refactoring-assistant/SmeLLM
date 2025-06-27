import os
import sys
import time
import statistics
from abc import ABC, abstractmethod

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from content_extractors.java.java_file_extractor import JavaFileExtractor
from content_extractors.typescript.typescript_file_extractor import TypeScriptFileExtractor
from chat_apis.prompt_engineering import Prompt
from chat_apis.oai.oai_apis import OAI
from chat_apis.claude.claude_apis import ANTHROPIC
from utils.config_util import get_model_details


class Processor(ABC):
    def __init__(self, file_path, file_type, model_name="gpt-4o-mini"):
        self.model_name = model_name
        # TODO: Cleanup this part because model details accessed many places.
        model_details = get_model_details(self.model_name)
        if not model_details:
            raise ValueError(f"Model details not found for model: {self.model_name}")
        self.api_type = model_details.get("api_provider")
        self.conversation_histories = []
        self.relative_paths = []
        self.file_time = []
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
                file_paths = relative_path.split("\\")
                file_name = file_paths[-1]
                formatted_user_input = f"{file_name} : {file_content}"
                prompt_generator = Prompt(user_input=formatted_user_input, prompt_format=self.api_type)
                self.conversation_histories.append(prompt_generator.get_conversation_start())
                
        except Exception as e:
            raise ValueError(f"Error in generating prompts: {e}")
    
    def process(self):
        start_time = time.time()
        try:  
            match self.api_type:
                case "OAI":
                    client = OAI(self.model_name)
                case "ANTHROPIC":
                    client = ANTHROPIC(self.model_name)
                case _:
                    raise ValueError(f"Invalid API type: {self.api_type}")
                
            response_dict = self.__process_input(client)
            return response_dict
        except Exception as e:
            raise ValueError(f"Error: {e}")
        finally:
            end_time = time.time()
            print(f"Time taken: {end_time - start_time:.2f} seconds")

    def calculate_time_stats(self):
        '''Calculate time statistics for processing files'''
        if not self.file_time:
            return {"average_time": 0, "max_time": 0, "min_time": 0}
        
        average_time = statistics.mean(self.file_time)
        max_time = max(self.file_time)
        min_time = min(self.file_time)
        median_time = statistics.median(self.file_time)
        
        return {
            "average_time": average_time,
            "median_time": median_time,
            "max_time": max_time,
            "min_time": min_time
        }
    
    def __process_input(self, client):
        response_dict = {}
        for conversation_index in range(len(self.conversation_histories)):
            file_start_time = time.time()
            print(f"Processing file {conversation_index + 1}: {self.relative_paths[conversation_index]}")
            response = client.chat_completion(conversations_history=self.conversation_histories[conversation_index])
            response_dict[self.relative_paths[conversation_index]] = response
            file_end_time = time.time()
            file_time = file_end_time - file_start_time
            self.file_time.append(file_time)
        print(f"Processed {len(self.relative_paths)} files")
        return response_dict
        
    @abstractmethod
    def content_extraction(self, file_path):
        '''Abstract method to extract content from file'''
        pass