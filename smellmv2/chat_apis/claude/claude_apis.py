import os
import sys
import time
import anthropic
from anthropic.types.message_create_params import MessageCreateParamsNonStreaming
from anthropic.types.messages.batch_create_params import Request
from dotenv import load_dotenv
import json
import re
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))


from chat_apis.interface_chat_api import ChatAPI
import config.constants as constants

load_dotenv(constants.ENV_PATH)



class ANTHROPIC(ChatAPI):

    def __init__(self, model_name=None):

        if not self.__validate_anthropic_model_name(model_name):
            raise ValueError(f"Model name {model_name} is not valid.")
        self.model_name = model_name
        # max tokens set in validation function
        self.CLAUDE_KEY = os.getenv("CLAUDE_KEY")
        if not self.CLAUDE_KEY:
            raise EnvironmentError("CLAUDE_KEY environment variable not found")
        try:
            self.anthropic_client = anthropic.Anthropic(api_key=self.CLAUDE_KEY)
        except Exception as e:
            raise ValueError(f"Error with Anthropic Claude API initialization: {e}")
        
        # Initialize mapping for custom IDs to file names
        self.custom_id_to_filename = {}
    
    def chat_completion(self, conversations_history=[]):

        self.__validate_conversation_history(conversations_history)
        try:
            response = self.anthropic_client.messages.create(
                model=self.model_name,
                max_tokens=self.max_tokens,
                system=conversations_history[0].get("content"),
                messages=conversations_history[1:],
                timeout=600.0
            )
        except Exception as e:
            raise ValueError(f"Error with Anthropic API: {e}")
        return response.content[0].text
    
    def batch_chat_completion(self, file_names, batch_conversations_list=[]):
        message_batch = self.__create_batch_request(file_names, batch_conversations_list)
        print(f"Created batch with ID: {message_batch.id}")
        self.__poll_batch_completion(message_batch)
        results = self.__get_batch_results(message_batch)
        
        return results


    def __poll_batch_completion(self, message_batch):
        start_time = time.time()
        print(f"Waiting for batch {message_batch.id} to complete...")
        
        poll_count = 0
        while True:
            poll_count += 1
            batch_status = self.anthropic_client.messages.batches.retrieve(message_batch.id)
            
            if batch_status.processing_status == "ended":
                print(f"Batch {message_batch.id} has completed! (Polled {poll_count} times)")
                break
            elif batch_status.processing_status == "failed":
                print(f"Batch {message_batch.id} failed! (Polled {poll_count} times)")
                exit(1)
            elif batch_status.processing_status == "cancelled":
                print(f"Batch {message_batch.id} was cancelled! (Polled {poll_count} times)")
                exit(1)
            
            # Print status update periodically
            if poll_count % 10 == 0:
                print(f"Status: {batch_status.processing_status} (Poll #{poll_count})")
            
            time.sleep(5)

        end_time = time.time()
        processing_time = end_time - start_time
        
        print(f"\n{'='*60}")
        print(f"BATCH PROCESSING COMPLETE")
        print(f"Processing time: {processing_time:.2f} seconds")

    
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
        
    def __validate_anthropic_model_name(self, model_name):

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
            if model_data.get("model_name") == model_name and model_data.get("api_provider") == "ANTHROPIC":
                self.max_tokens = model_data.get("output_context_size")
                return True
                
        return False
    
    def __create_batch_request(self, file_names, batch_conversations_list):
        requests = []
        self.custom_id_to_filename = {}  # Reset mapping for new batch
        
        for i in range(len(file_names)):
            # Create safe custom ID and store mapping
            safe_custom_id = self.__create_safe_custom_id(file_names[i], i)
            self.custom_id_to_filename[safe_custom_id] = file_names[i]
            
            request = Request(
                custom_id=safe_custom_id,
                params=MessageCreateParamsNonStreaming(
                    model=self.model_name,
                    max_tokens=self.max_tokens,
                    system=batch_conversations_list[i][0].get("content"),
                    messages=[batch_conversations_list[i][1]]
                )
            )
            requests.append(request)
        
        return self.anthropic_client.messages.batches.create(requests=requests)
    
    def __get_batch_results(self, message_batch):
        try:
            results = self.anthropic_client.messages.batches.results(message_batch.id)
            filename_to_content = {}
        
            for i, result in enumerate(results, 1):            
                # Extract custom_id
                custom_id = getattr(result, 'custom_id', 'Unknown')
                
                # Get original filename from custom_id
                original_filename = self.__get_filename_from_custom_id(custom_id)
                
                # Extract result type
                if hasattr(result, 'result'):
                    message = result.result.message
                    
                    # Extract content from message
                    if hasattr(message, 'content') and message.content:
                        content = message.content[0].text
                        if original_filename:
                            filename_to_content[original_filename] = content
                        else:
                            print(f"Warning: Could not map custom_id {custom_id} to filename")

            return filename_to_content
            
        except Exception as e:
            print(f"Error retrieving batch results: {e}")
            exit(1)

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
    

if __name__ == '__main__':
    try:
        claude = ANTHROPIC("random_model")
    except Exception as e:
        print(f"Error: {e}")
    try:
        claude = ANTHROPIC("claude-sonnet-4-20250514")
    except Exception as e:
        print(f"Error: {e}")
    conversations_history = [
        {"role": "system", "content": "Hello, how can I help you today?"},
        {"role": "user", "content": "I need help with a programming problem."},
    ]
    try:
        response = claude.chat_completion(conversations_history)
        print(response)
    except Exception as e:
        print(f"Error: {e}")

