import os
import sys
from openai import OpenAI
from dotenv import load_dotenv
import json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))


from chat_apis.interface_chat_api import ChatAPI
import config.constants as constants

load_dotenv(constants.ENV_PATH)

class OAI(ChatAPI):
    """
    This class is responsible for handling the OpenAI API calls for the chat completion task.
    """
    MODEL_FILE_NAME = 'oai_models.json'
    
    def __init__(self, model_name="gpt-4o-mini"):
        """
        Initializes the OAI class with the specified model name.

        Args:
            model_name (str): The name of the model to use for chat completion. Default is "gpt-4o-mini".
        
        Raises:
            EnvironmentError: If the OAI_KEY environment variable is not found.
        """
        if not self._validate_model_name(model_name):
            raise ValueError(f"Model name {model_name} is not valid.")
        self.model_name = model_name
        self.OAI_KEY = os.getenv("OAI_KEY")
        if not self.OAI_KEY:
            raise EnvironmentError("OAI_KEY environment variable not found")
        try:
            self.oai_client = OpenAI(api_key=self.OAI_KEY)
        except Exception as e:
            raise ValueError(f"Error with OpenAI API initialization: {e}")
    
    def chat_completion(self, conversations_history=[]):
        """
        Generates a chat completion using the OpenAI API.

        Args:
            conversations_history (list): A list of conversation messages.

        Returns:
            str: The content of the response message.

        Raises:
            ValueError: If there is an error with the OpenAI API or if the conversation history is invalid.
        """
        self._validate_conversation_history(conversations_history)
        try:
            response = self.oai_client.chat.completions.create(
                model=self.model_name,
                messages=conversations_history
            )
        except Exception as e:
            raise ValueError(f"Error with OpenAI API: {e}")
        return response.choices[0].message.content
    
    def _validate_conversation_history(self, conversations_history):
        """
        Validates the conversation history.

        Args:
            conversations_history (list): A list of conversation messages.

        Raises:
            ValueError: If the conversation history is invalid.
        """
        self._validate_conversation_list(conversations_history)
        self._validate_conversation_roles(conversations_history)
    
    def _validate_conversation_roles(self, conversations_history):
        """
        Validates the roles in the conversation history based on the first two roles and the last role.

        Args:
            conversations_history (list): A list of conversation messages.

        Raises:
            ValueError: If the roles in the conversation history are invalid.
        """
        if conversations_history[0].get("role") != "system":
            raise ValueError("The first message must be a system prompt")
        if conversations_history[1].get("role") != "user":
            raise ValueError("The second message must be a user prompt")
        if conversations_history[-1].get("role") != "user":
            raise ValueError("The last message must be a user prompt")
    
    def _validate_conversation_list(self, conversations_history):
        """
        Validates the conversation history list based on basic parameters of length of list.

        Args:
            conversations_history (list): A list of conversation messages.

        Raises:
            ValueError: If the conversation history list is invalid.
        """
        if not conversations_history:
            raise ValueError("conversations_history cannot be empty")
        if not isinstance(conversations_history, list):
            raise ValueError("conversations_history must be a list")
        if len(conversations_history) < 2:
            raise ValueError("conversations_history must contain at least two messages")
        
    def _validate_model_name(self, model_name):
        """
        Validate if the provided model name exists in oai_models.json.
        
        Args:
            model_name (str): The model name to validate.
            
        Returns:
            bool: True if the model name exists, False otherwise.
            
        Raises:
            FileNotFoundError: If the oai_models.json file does not exist.
        """
        current_dir = os.path.dirname(os.path.abspath(__file__))
        models_file_path = os.path.join(current_dir, self.MODEL_FILE_NAME)
        
        # Check if the file exists
        if not os.path.exists(models_file_path):
            raise FileNotFoundError(f"Model configuration file not found at {models_file_path}")
        
        # Read and parse the JSON file
        with open(models_file_path, 'r') as f:
            models_config = json.load(f)
        
        # Check if the model_name exists in the loaded configuration
        for model_key, model_data in models_config.items():
        # Check if the model_name value matches the one we're looking for
            if model_data.get("model_name") == model_name:
                return True
                
        return False
        

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