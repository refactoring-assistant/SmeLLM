import os
import sys
from openai import OpenAI
from dotenv import load_dotenv
import json
import tempfile
import atexit
import time
import re
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))


from chat_apis.interface_chat_api import ChatAPI
import config.constants as constants

load_dotenv(constants.ENV_PATH)

class OAI(ChatAPI):
    """
    This class is responsible for handling the OpenAI API calls for the chat completion task.
    """
    
    def __init__(self, model_name="gpt-4o-mini"):
        if not self.__validate_oai_model_name(model_name):
            raise ValueError(f"Model name {model_name} is not valid.")
        self.model_name = model_name
        # already initialized max_tokens in __validate_oai_model_name
        self.OAI_KEY = os.getenv("OAI_KEY")
        if not self.OAI_KEY:
            raise EnvironmentError("OAI_KEY environment variable not found")
        try:
            self.oai_client = OpenAI(api_key=self.OAI_KEY)
        except Exception as e:
            raise ValueError(f"Error with OpenAI API initialization: {e}")
        self.temp_batch_file = None
    
    def chat_completion(self, conversations_history=[]):

        self.__validate_conversation_history(conversations_history)
        try:
            response = self.oai_client.chat.completions.create(
                model=self.model_name,
                messages=conversations_history
            )
        except Exception as e:
            raise ValueError(f"Error with OpenAI API: {e}")
        return response.choices[0].message.content
    
    def batch_chat_completion(self, file_names, batch_conversations_list=[]):
        batch_file_path = self.__make_batch_file_json(file_names, batch_conversations_list)
        batch_file_id = self.__upload_batch_file(batch_file_path)
        print(f"Batch file uploaded with ID: {batch_file_id}")
        output_file_id = self.__create_batch_request(batch_file_id)
        print(f"Batch processing completed with output file ID: {output_file_id}")
        results = self.__get_batch_results(output_file_id)
        return results
    
    def __validate_conversation_history(self, conversations_history):

        self.__validate_conversation_list(conversations_history)
        self.__validate_conversation_roles(conversations_history)
    
    def __validate_conversation_roles(self, conversations_history):
        if conversations_history[0].get("role") != "system":
            raise ValueError("The first message must be a system prompt")
        if conversations_history[1].get("role") != "user":
            raise ValueError("The second message must be a user prompt")
        if conversations_history[-1].get("role") != "user":
            raise ValueError("The last message must be a user prompt")
    
    def __validate_conversation_list(self, conversations_history):
        if not conversations_history:
            raise ValueError("conversations_history cannot be empty")
        if not isinstance(conversations_history, list):
            raise ValueError("conversations_history must be a list")
        if len(conversations_history) < 2:
            raise ValueError("conversations_history must contain at least two messages")
        
    def __validate_oai_model_name(self, model_name):
        models_file_path = constants.MODELS_LIST
        
        # Check if the file exists
        if not os.path.exists(models_file_path):
            raise FileNotFoundError(f"Model configuration file not found at {models_file_path}")
        
        # Read and parse the JSON file
        with open(models_file_path, 'r') as f:
            models_config = json.load(f)
        
        # Check if the model_name exists in the loaded configuration
        for model_key, model_data in models_config.items():
        # Check if the model_name value matches the one we're looking for
            if model_data.get("model_name") == model_name and model_data.get("api_provider") == "OAI":
                self.max_tokens = model_data.get("output_context_size")
                return True
                
        return False
    
    def __create_safe_custom_id(self, filename, index):
        """
        Create a safe custom ID from filename by removing/replacing invalid characters
        and ensuring uniqueness with index
        """
        # Remove or replace invalid characters (keep only alphanumeric, underscore, hyphen)
        safe_id = re.sub(r'[^\w\-]', '_', filename)
        
        # Ensure it doesn't start with a number or special character
        if safe_id and not safe_id[0].isalpha():
            safe_id = f"file_{safe_id}"
        
        # Add index to ensure uniqueness and limit length
        safe_id = f"{safe_id}_{index}"
        
        # Limit length (custom IDs often have length limits)
        if len(safe_id) > 50:
            safe_id = safe_id[:47] + f"_{index}"
        
        return safe_id
    
    def __get_filename_from_custom_id(self, custom_id):
        """
        Retrieve the original filename from a custom ID
        """
        return self.custom_id_to_filename.get(custom_id)
    
    def __make_batch_file_json(self, file_names, conversations_list):
        self.custom_id_to_filename = {}  # Reset mapping for new batch
        
        # Create temporary file in current directory
        self.temp_batch_file = tempfile.NamedTemporaryFile(
            mode='w', 
            suffix='.jsonl', 
            prefix='batch_', 
            dir=os.getcwd(), 
            delete=False
        )
        
        # Register cleanup function
        atexit.register(self.__cleanup_temp_file)
        
        try:
            for i in range(len(file_names)):
                # Create safe custom ID and store mapping
                safe_custom_id = self.__create_safe_custom_id(file_names[i], i)
                self.custom_id_to_filename[safe_custom_id] = file_names[i]
                
                batch_item = {
                    "custom_id": safe_custom_id,
                    "method": "POST", 
                    "url": "/v1/chat/completions",
                    "body": {
                        "model": self.model_name,
                        "messages": conversations_list[i],
                        "max_tokens": self.max_tokens
                    }
                }
                self.temp_batch_file.write(json.dumps(batch_item) + '\n')
            
            self.temp_batch_file.close()
            return self.temp_batch_file.name
            
        except Exception as e:
            self.temp_batch_file.close()
            self.__cleanup_temp_file()
            raise e
    
    def __cleanup_temp_file(self):
        """Clean up temporary batch file"""
        if self.temp_batch_file and os.path.exists(self.temp_batch_file.name):
            try:
                os.remove(self.temp_batch_file.name)
                print(f"Cleaned up temporary file: {self.temp_batch_file.name}")
            except OSError as e:
                print(f"Error cleaning up temporary file: {e}")

    def __upload_batch_file(self, file_path):
        try:
            # Upload the batch file
            batch_input_file = self.oai_client.files.create(
                file=open(file_path, "rb"),
                purpose="batch"
            )
            
            file_id = batch_input_file.id
            print(f"Batch file uploaded with ID: {file_id}")
            
            # Poll until upload is processed successfully
            max_wait_time = 300  # 5 minutes max wait time
            poll_interval = 5    # Check every 5 seconds
            start_time = time.time()
            
            while time.time() - start_time < max_wait_time:
                try:
                    # Check file status
                    file_status = self.oai_client.files.retrieve(file_id)
                    
                    if file_status.status == "processed":
                        print(f"Batch file {file_id} successfully processed!")
                        return file_id
                    elif file_status.status == "error":
                        raise Exception(f"Batch file upload failed with error: {file_status}")
                    else:
                        print(f"Batch file status: {file_status.status}. Waiting...")
                        time.sleep(poll_interval)
                    
                except Exception as e:
                    print(f"Error checking file status: {e}")
                    time.sleep(poll_interval)
        
            # If we reach here, we've timed out
            raise TimeoutError(f"Batch file upload did not complete within {max_wait_time} seconds")
        
        except Exception as e:
            raise Exception(f"Error uploading batch file: {e}")
        
    def __create_batch_request(self, batch_input_file_id):
        batch = self.oai_client.batches.create(
            input_file_id=batch_input_file_id,
            endpoint="/v1/chat/completions",
            completion_window="24h",
            metadata={
                "description": "batch processing for code smell detection"
            }
        )
        batch_id = batch.id
        print(f"Created batch with ID: {batch_id}")
        poll_counter = 0
        while True:
            batch_status = self.oai_client.batches.retrieve(batch_id)
            poll_counter += 1
            if batch_status.status == "completed":
                print(f"Batch {batch_id} has completed after {poll_counter} polls!")
                return batch_status.output_file_id
            elif batch_status.status == "failed":
                raise Exception(f"Batch {batch_id} failed with error: {batch_status.error}")
            elif batch_status.status == "cancelled":
                raise Exception(f"Batch {batch_id} was cancelled")
            else:
                print(f"Batch {batch_id} status: {batch_status.status}")
                print(f"Batch {batch_id} is still processing... (Poll #{poll_counter})")
                time.sleep(5)

    def __get_batch_results(self, output_file_id):
        try:
            output_file = self.oai_client.files.content(output_file_id)
            
            # Create response dictionary mapping filename to assistant content
            response_dict = {}
            
            # Parse each line of the JSONL output
            for line in output_file.text.strip().split('\n'):
                if line.strip():  # Skip empty lines
                    try:
                        result = json.loads(line)
                        custom_id = result.get('custom_id')
                        
                        # Get the original filename from custom_id
                        filename = self.__get_filename_from_custom_id(custom_id)
                        
                        if filename and result.get('response') and result['response'].get('status_code') == 200:
                            # Extract assistant content from the response
                            body = result['response'].get('body', {})
                            choices = body.get('choices', [])
                            
                            if choices and len(choices) > 0:
                                message = choices[0].get('message', {})
                                assistant_content = message.get('content', '')
                                response_dict[filename] = assistant_content
                            else:
                                print(f"Warning: No choices found for {filename}")
                        else:
                            if filename:
                                print(f"Error in response for {filename}: Status code {result.get('response', {}).get('status_code', 'unknown')}")
                            else:
                                print(f"Warning: Could not map custom_id {custom_id} to filename")
                                
                    except json.JSONDecodeError as e:
                        print(f"Error parsing line: {line[:100]}... Error: {e}")
                    except Exception as e:
                        print(f"Error processing line: {e}")
            
            print(f"Successfully processed {len(response_dict)} responses")
            return response_dict
            
        except Exception as e:
            raise Exception(f"Error retrieving batch results: {e}")

#define main function to test the OAI class
if __name__ == '__main__':
    try:
        oai = OAI("random_model")
    except Exception as e:
        print(f"Error: {e}")
    try:
        oai = OAI()
    except Exception as e:
        print(f"Error: {e}")
    conversations_history = [
        {"role": "system", "content": "Hello, how can I help you today?"},
        {"role": "user", "content": "I need help with a programming problem."},
    ]
    try:
        response = oai.chat_completion(conversations_history)
        print(response)
    except Exception as e:
        print(f"Error: {e}")