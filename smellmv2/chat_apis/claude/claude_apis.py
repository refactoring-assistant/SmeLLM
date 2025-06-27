import os
import sys
import anthropic
from dotenv import load_dotenv
import json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))


from chat_apis.interface_chat_api import ChatAPI
import config.constants as constants

load_dotenv(constants.ENV_PATH)



class ANTHROPIC(ChatAPI):

    def __init__(self, model_name=None):

        if not self.__validate_anthropic_model_name(model_name):
            raise ValueError(f"Model name {model_name} is not valid.")
        self.model_name = model_name
        self.max_tokens = 2048
        self.CLAUDE_KEY = os.getenv("CLAUDE_KEY")
        if not self.CLAUDE_KEY:
            raise EnvironmentError("CLAUDE_KEY environment variable not found")
        try:
            self.anthropic_client = anthropic.Anthropic(api_key=self.CLAUDE_KEY)
        except Exception as e:
            raise ValueError(f"Error with Anthropic Claude API initialization: {e}")
    
    def chat_completion(self, conversations_history=[]):

        self.__validate_conversation_history(conversations_history)
        try:
            response = self.anthropic_client.messages.create(
                model=self.model_name,
                max_tokens=self.max_tokens,
                system=conversations_history[0].get("content"),
                messages=conversations_history[1:]
            )
        except Exception as e:
            raise ValueError(f"Error with Anthropic API: {e}")
        return response.content[0].text
    
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
                self.max_tokens = model_data.get("input_context_size", 1000)
                return True
                
        return False
        

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

