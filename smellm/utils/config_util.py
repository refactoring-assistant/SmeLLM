import os
import sys
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from config.constants import MODELS_LIST
from config.constants import ENV_PATH

def get_model_details(model_name):
    try:
        # Read and parse the JSON file
        with open(MODELS_LIST, 'r') as f:
            models_config = json.load(f)
        
        for _, model_data in models_config.items():
            if model_data.get("model_name") == model_name:
                return model_data
    
    except Exception as e:
        print(f"Error accessing models list: {e}")
        
def update_api_key(key_name, key_value):
    """
    Updates or adds an API key in the .env file.
    
    Args:
        key_name (str): Name of the API key (e.g., 'OAI_KEY')
        key_value (str): Value of the API key
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        env_content = {}
        
        # Check if .env file exists
        if os.path.exists(ENV_PATH):
            # Read existing content
            with open(ENV_PATH, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#') and '=' in line:
                        k, v = line.split('=', 1)
                        env_content[k.strip()] = v.strip()
        else:
            # Ensure the directory exists
            os.makedirs(os.path.dirname(ENV_PATH), exist_ok=True)
        
        # Update or add the key
        env_content[key_name] = key_value
        
        # Write back to file
        with open(ENV_PATH, 'w') as f:
            for k, v in env_content.items():
                f.write(f"{k}={v}\n")
                
        print(f"API key '{key_name}' has been {'updated' if os.path.exists(ENV_PATH) else 'added'}")
        return True
        
    except Exception as e:
        print(f"Error updating API key: {e}")
        return False
