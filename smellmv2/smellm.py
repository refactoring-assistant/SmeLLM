import argparse
import os
import sys
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

import config.constants as constants
from process_args.process_file import ProcessFile
from process_args.process_zipfile import ProcessZipFile
from process_args.process_folder import ProcessFolder
from output.save_data import SaveData
from utils.config_util import update_api_key

class SmeLLM:
    def __init__(self):
        """Initialize the SmeLLM class."""
        self.models_file_path = constants.MODELS_LIST
        self.__validate_model_path_exists()
        self.supported_languages = constants.SUPPORTED_LANGUAGES
        self.parser = argparse.ArgumentParser(
            description="SmeLLM: Detect code smells using Large Language Models"
        )
        self.parser.add_argument(
            "--list_models",
            action="store_true",
            help="List all available models"
        )
        self.parser.add_argument(
            "--set_env",
            type=str,
            metavar="KEY=VALUE",
            help="Set or update an environment variable in the .env file (format: KEY=VALUE)"
        )
        self.parser.add_argument(
            "--lang", 
            type=str, 
            required=False,
            help=f"Programming language (supported: {', '.join(self.supported_languages)})"
        )
        self.group = self.parser.add_mutually_exclusive_group(required=False)
        self.group.add_argument(
            "--file", 
            type=str,
            help="Path to a single code file"
        )
        self.group.add_argument(
            "--folder", 
            type=str,
            help="Path to a folder containing code files"
        )
        self.group.add_argument(
            "--zipfile", 
            type=str,
            help="Path to a ZIP archive containing code files"
        )
        self.parser.add_argument(
        "--model",
        type=str,
        default="gpt-4o-mini",  # Default model
        help="(optional arg) Model to use for code smell detection (default: gpt-4o-mini)"
        )
        
        
    def parse_arguments(self):
        """Parse command line arguments.
        
        The method accepts:
        1. --lang (required): Specifies the programming language
        2. One of the following (required):
           - --file: Path to a single file
           - --folder: Path to a directory containing code files
           - --zipfile: Path to a ZIP archive containing code files
        3. --model (optional): Specifies the model to use for code smell detection
        4. --list_models: Lists all available models (exits if this arg is called)
           
        Returns:
            argparse.Namespace: The parsed command line arguments
            
        Raises:
            SystemExit: If arguments are invalid or help is requested
        """
        
        # Parse arguments
        args = self.parser.parse_args()
        
        if args.list_models:
            self.__list_available_models()
            sys.exit(0)
        
        if args.set_env:
            self.__update_env_variable(args)
            sys.exit(0)
        
        self.__validate_args_paths(args)
            
        return args
    
    def run(self):
        """Run the SmeLLM tool with the provided arguments."""
        try:
            args = self.parse_arguments()
            
            print(f"Language: {args.lang}")
            
            if args.file:
                print(f"Processing file: {args.file}")
                processor = ProcessFile(args.file, args.lang, args.model)
            elif args.folder:
                print(f"Processing folder: {args.folder}")
                processor = ProcessFolder(args.folder, args.lang, args.model)
            elif args.zipfile:
                print(f"Processing ZIP file: {args.zipfile}")
                processor = ProcessZipFile(args.zipfile, args.lang, args.model)
            
            processed_data = processor.process()
            
            save_data = SaveData()
            saved_dir = save_data.save_file(processed_data)
            print(f"Processed data saved to: {saved_dir}")
        except Exception as e:
            print(f"Error: {e}")
            
    def __validate_args_paths(self, args):
        """Validate the paths provided in the arguments.
        
        Args:
            args (argparse.Namespace): The parsed command line arguments.
            
        Raises:
            SystemExit: If the paths are invalid
        """
        # Validate language
        
        self.__validate_language_arg(args)
        self.__validate_processing_input_args(args)
        self.__validate_model_arg(args)
            
    def __validate_language_arg(self, args):
        if not args.lang:
            self.parser.error("Language argument is required")
        if args.lang not in self.supported_languages:
            self.parser.error(f"Unsupported language: {args.lang}. Supported languages are: {', '.join(self.supported_languages)}")
            
    def __validate_processing_input_args(self, args):
        if not any([args.file, args.folder, args.zipfile]):
            self.parser.error("One of --file, --folder, or --zipfile is required")
        # Validate the paths and convert to absolute paths
        if args.file:
            args.file = os.path.abspath(args.file)
            if not os.path.isfile(args.file):
                self.parser.error(f"File does not exist: {args.file}")

        elif args.folder:
            args.folder = os.path.abspath(args.folder)
            if not os.path.isdir(args.folder):
                self.parser.error(f"Folder does not exist: {args.folder}")

        elif args.zipfile:
            args.zipfile = os.path.abspath(args.zipfile)
            if not os.path.isfile(args.zipfile):
                self.parser.error(f"ZIP file does not exist: {args.zipfile}")
                
    def __validate_model_arg(self, args):
        if args.model:
        # Read and parse the JSON file
            try:
                with open(self.models_file_path, 'r') as f:
                    models_config = json.load(f)
                
                # Check if the model_name exists in the loaded configuration
                for model_key, model_data in models_config.items():
                # Check if the model_name value matches the one we're looking for
                    if model_data.get("model_name") == args.model:
                        return
                self.parser.error(f"Model Name not present in list: {args.model}")
            except Exception as e:
                self.parser.error(f"Error validating model: {args.model}")
            
    def __list_available_models(self):
        """Display all available models and exit."""
        
        try:
            # Read and parse the JSON file
            with open(self.models_file_path, 'r') as f:
                models_config = json.load(f)
            
            print("Available models:")
            print("-" * 40)
            
            # Sort models alphabetically for better display
            model_names = [model_data.get("model_name") for _, model_data in models_config.items()]
            
            for i, model_name in enumerate(model_names, 1):
                print(f"{i}. {model_name}")
                
            print("-" * 40)
            print(f"Total available models: {len(model_names)}")
        
        except Exception as e:
            print(f"Error listing models: {e}")
            sys.exit(1)
                
    
    def __validate_model_path_exists(self):
        """Validate if the models file path exists."""
        
        if not os.path.exists(self.models_file_path):
            raise FileNotFoundError(f"Model configuration file not found at {self.models_file_path}")

    def __update_env_variable(self, args):
        if '=' not in args.set_env:
            raise ValueError("Environment variable must be in the format KEY=VALUE")
    
        key, value = args.set_env.split('=', 1)
        key = key.strip()
        value = value.strip()
        
        if not key:
            raise ValueError("Key cannot be empty")
        
        update_api_key(key, value)
        
# If the script is executed directly
if __name__ == "__main__":
    smellm = SmeLLM()
    smellm.run()