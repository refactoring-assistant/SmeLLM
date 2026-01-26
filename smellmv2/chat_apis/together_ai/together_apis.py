import os
import sys
import json
from together import Together
from dotenv import load_dotenv

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from chat_apis.interface_chat_api import ChatAPI
import config.constants as constants

load_dotenv(constants.ENV_PATH)


class TOGETHER(ChatAPI):
    """
    This class is responsible for handling the Together AI API calls for the chat completion task.
    """
    
    def __init__(self, model_name=None):
        if not self.__validate_together_model_name(model_name):
            raise ValueError(f"Model name {model_name} is not valid.")
        self.model_name = model_name
        # max_tokens set in validation function
        self.TOGETHER_KEY = os.getenv("TOGETHER_KEY")
        if not self.TOGETHER_KEY:
            raise EnvironmentError("TOGETHER_KEY environment variable not found")
        try:
            self.together_client = Together(api_key=self.TOGETHER_KEY)
        except Exception as e:
            raise ValueError(f"Error with Together AI API initialization: {e}")
        
        # Initialize mapping for custom IDs to file names (for batch processing)
        self.custom_id_to_filename = {}
    
    def chat_completion(self, conversations_history=[]):
        """
        Perform chat completion using Together AI API.
        
        Args:
            conversations_history: List of conversation messages with roles and content
            
        Returns:
            str: The assistant's response content
        """
        self.__validate_conversation_history(conversations_history)
        
        try:
            # Convert conversation history to Together AI format
            messages = self.__convert_messages_format(conversations_history)
            
            # Create completion request
            response = self.together_client.chat.completions.create(
                model=self.model_name,
                messages=messages,
                max_tokens=self.max_tokens
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            raise ValueError(f"Error with Together AI API: {e}")
    
    def batch_chat_completion(self, file_names, batch_conversations_list=[]):
        """
        Perform batch chat completion using Together AI API.
        Note: Together AI may not have native batch API, so we process sequentially.
        
        Args:
            file_names: List of file names
            batch_conversations_list: List of conversation histories for each file
            
        Returns:
            dict: Dictionary mapping file names to response content
        """
        response_dict = {}
        
        for i, conversations_history in enumerate(batch_conversations_list):
            file_name = file_names[i] if i < len(file_names) else f"file_{i}"
            print(f"Processing file {i + 1}/{len(batch_conversations_list)}: {file_name}")
            
            try:
                response = self.chat_completion(conversations_history)
                response_dict[file_name] = response
            except Exception as e:
                print(f"Error processing {file_name}: {e}")
                response_dict[file_name] = f"Error: {e}"
        
        return response_dict
    
    def __convert_messages_format(self, conversations_history):
        """
        Convert conversation history to Together AI format.
        Together AI uses the same format as OpenAI (messages with role and content).
        Together AI supports system messages, so we can use them directly.
        
        Args:
            conversations_history: List of messages with role and content
            
        Returns:
            list: Messages in Together AI format
        """
        messages = []
        for msg in conversations_history:
            role = msg.get("role")
            content = msg.get("content")
            messages.append({"role": role, "content": content})
        
        return messages
    
    def __validate_conversation_history(self, conversations_history):
        """Validate the conversation history format."""
        self.__validate_conversation_list(conversations_history)
        self.__validate_conversation_roles(conversations_history)
    
    def __validate_conversation_roles(self, conversations_history):
        """Validate that conversation roles are correct."""
        if conversations_history[0].get("role") != "system":
            raise ValueError("The first message must be a system prompt")
        if conversations_history[1].get("role") != "user":
            raise ValueError("The second message must be a user prompt")
        if conversations_history[-1].get("role") != "user":
            raise ValueError("The last message must be a user prompt")
    
    def __validate_conversation_list(self, conversations_history):
        """Validate that conversation history is a non-empty list."""
        if not conversations_history:
            raise ValueError("conversations_history cannot be empty")
        if not isinstance(conversations_history, list):
            raise ValueError("conversations_history must be a list")
        if len(conversations_history) < 2:
            raise ValueError("conversations_history must contain at least two messages")
    
    def __validate_together_model_name(self, model_name):
        """
        Validate that the model name exists in the models configuration.
        
        Args:
            model_name: The model name to validate
            
        Returns:
            bool: True if valid, False otherwise
        """
        models_file_path = constants.MODELS_LIST
        
        # Check if the file exists
        if not os.path.exists(models_file_path):
            raise FileNotFoundError(f"Model configuration file not found at {models_file_path}")
        
        # Read and parse the JSON file
        with open(models_file_path, 'r') as f:
            models_config = json.load(f)
        
        # Check if the model_name exists in the loaded configuration
        for model_key, model_data in models_config.items():
            # Check if the model_name value matches and API provider is TOGETHER
            if model_data.get("model_name") == model_name and model_data.get("api_provider") == "TOGETHER":
                self.max_tokens = model_data.get("output_context_size")
                return True
                
        return False


if __name__ == '__main__':
    # Test the Together AI implementation
    try:
        together = TOGETHER("random_model")
    except Exception as e:
        print(f"Error: {e}")
    
    try:
        # This will fail if model is not in models_list.json with TOGETHER provider
        together = TOGETHER("openai/gpt-oss-20b")
    except Exception as e:
        print(f"Error: {e}")
    
    conversations_history = [
        {"role": "system", "content": "Hello, how can I help you today?"},
        {"role": "user", "content": "I need help with a programming problem."},
    ]
    try:
        response = together.chat_completion(conversations_history)
        print(response)
    except Exception as e:
        print(f"Error: {e}")

