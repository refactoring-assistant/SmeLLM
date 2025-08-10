from .chat_apis import openai, anthropic
from .config.prompts import ZERO_SHOT_SYSTEM_PROMPT
from .config import models
import json
from concurrent.futures import ThreadPoolExecutor
import datetime
import os

def parse_dict(args, files_dict):
    print(f"args: {args}")
    # Ensure output path ends with a trailing slash
    output_path = args.output if args.output.endswith('/') else args.output + '/'

    # Create the output directory if it doesn't exist
    os.makedirs(output_path, exist_ok=True)

    current_date_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"{output_path}{current_date_time}.json"
    try:
        # Initialize the JSON file with an empty list
        with open(output_file, "w") as f:
            json.dump([], f)

        def process_file(file_name, content):
            print(f"Processing file: {file_name}")
            response = zero_shot_process_file(args, file_name, content)
            if response is None:
                print(f"Error: No response received for {file_name}")
                return
            try:
                # Check if the response is already a list
                if isinstance(response, list):
                    data = response
                else:
                    data = json.loads(response)

                for entry in data:
                    entry["file_name"] = file_name

                # Append the response to the JSON file
                with open(output_file, "r+") as f:
                    existing_data = json.load(f)
                    existing_data.extend(data)
                    f.seek(0)
                    json.dump(existing_data, f, indent=2)
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON for {file_name}: {e}")
            except Exception as e:
                print(f"An error occurred while processing {file_name}: {e}")

        # Use ThreadPoolExecutor to process files in parallel
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(process_file, file_name, content) for file_name, content in files_dict.items()]
            for future in futures:
                future.result()  # Wait for all tasks to complete
    except Exception as e:
        print(f"An error occurred while initializing the output file: {e}")

def send_to_model(system_prompt, content, model):
    model = next((m for m in models.MODELS if m['name'] == model), None)
    if model['provider'] == 'openai':
        api = openai.OpenAIAPI(model['name'])
        response = api.generate_response(system_prompt, content)
    elif model['provider'] == 'anthropic':
        api = anthropic.Anthropic(model['name'])
        response = api.generate_response(system_prompt, content)
    
    return response

# def create_few_shot_system_prompt(code_smell_id):
#     code_smell_obj = next((smell for smell in CODE_SMELLS if smell["id"] == code_smell_id), None)
#     if not code_smell_obj:
#         raise ValueError(f"Code smell id '{code_smell_id}' not found.")
#     examples = code_smell_obj.get("examples", [])

def zero_shot_process_file(args, file_name, content):
    response = send_to_model(ZERO_SHOT_SYSTEM_PROMPT, content, args.model)
    return response

# def few_shot_process_file(args, file_name, content):
#     system_prompt = create_few_shot_system_prompt()
#     response = send_to_model(system_prompt, content, args.model)
#     generate_report(file_name, response)
#     print(f"Processed {file_name}: {response}")

#     return examples