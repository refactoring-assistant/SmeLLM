import os
import sys
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from config.constants import MODELS_LIST

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