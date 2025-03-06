import argparse
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

import config.constants as constants
from process_args.process_file import ProcessFile
from process_args.process_zipfile import ProcessZipFile
from process_args.process_folder import ProcessFolder

class SmeLLM:
    def __init__(self):
        """Initialize the SmeLLM class."""
        self.supported_languages = constants.SUPPORTED_LANGUAGES
        self.parser = argparse.ArgumentParser(
            description="SmeLLM: Detect code smells using Large Language Models"
        )
        self.parser.add_argument(
            "--lang", 
            type=str, 
            required=True,
            help=f"Programming language (supported: {', '.join(self.supported_languages)})"
        )
        self.group = self.parser.add_mutually_exclusive_group(required=True)
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
           
        Returns:
            argparse.Namespace: The parsed command line arguments
            
        Raises:
            SystemExit: If arguments are invalid or help is requested
        """
        
        # Parse arguments
        args = self.parser.parse_args()
        
        self.__validate_args_paths(args)
            
        return args
    
    def run(self):
        """Run the SmeLLM tool with the provided arguments."""
        args = self.parse_arguments()
        
        print(f"Language: {args.lang}")
        
        if args.file:
            print(f"Processing file: {args.file}")
            ProcessFile(args.file, args.lang)
        elif args.folder:
            print(f"Processing folder: {args.folder}")
            ProcessFolder(args.folder, args.lang)
        elif args.zipfile:
            print(f"Processing ZIP file: {args.zipfile}")
            ProcessZipFile(args.zipfile, args.lang)
            
    def __validate_args_paths(self, args):
        """Validate the paths provided in the arguments.
        
        Args:
            args (argparse.Namespace): The parsed command line arguments.
            
        Raises:
            SystemExit: If the paths are invalid
        """
        # Validate language
        if args.lang not in self.supported_languages:
            self.parser.error(f"Unsupported language: {args.lang}. Supported languages are: {', '.join(self.supported_languages)}")
        
        # Validate the paths and convert to absolute paths
        if args.file:
            args.file = os.path.abspath(args.file)
            if not os.path.isfile(args.file):
                self.parser.error(f"File does not exist: {args.file}")

        if args.folder:
            args.folder = os.path.abspath(args.folder)
            if not os.path.isdir(args.folder):
                self.parser.error(f"Folder does not exist: {args.folder}")

        if args.zipfile:
            args.zipfile = os.path.abspath(args.zipfile)
            if not os.path.isfile(args.zipfile):
                self.parser.error(f"ZIP file does not exist: {args.zipfile}")
        
        # TODO: Add validation logic for models

# If the script is executed directly
if __name__ == "__main__":
    smellm = SmeLLM()
    smellm.run()