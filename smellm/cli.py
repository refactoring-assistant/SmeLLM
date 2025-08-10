import argparse
import json

import sys
import os

from .config import models
from .config.constants import LANGUAGE_EXTENSIONS
from .config.code_smells import CODE_SMELLS


def validate_paths(args):
    """
    Validates the file, folder, zip paths (and evaluation file if provided) provided in the arguments and converts them to absolute paths.

    :param args: The parsed command-line arguments containing paths.
    :return: None
    """
    if args.file_path:
        if not os.path.isfile(args.file_path):
            sys.exit(f"Error: File '{args.file_path}' does not exist.")
        args.file_path = os.path.abspath(args.file_path)

    if args.folder_path:
        if not os.path.isdir(args.folder_path):
            sys.exit(f"Error: Folder '{args.folder_path}' does not exist.")
        args.folder_path = os.path.abspath(args.folder_path)

    if args.zip_path:
        if not (
            os.path.isfile(args.zip_path) and args.zip_path.lower().endswith(".zip")
        ):
            sys.exit(
                f"Error: Zip file '{args.zip_path}' does not exist or is not a .zip file."
            )
        args.zip_path = os.path.abspath(args.zip_path)

    if args.eval:
        if (
            not os.path.isfile(args.eval)
            and args.eval.lower().endswith("csv")
            or args.eval.lower().endswith("xlsx")
        ):
            sys.exit(
                f"Error: Evaluation file '{args.eval}' does not exist or is not a .csv/.xlsx file."
            )
        print(f"Evaluation file: {args.eval}")
        args.eval = os.path.abspath(args.eval)


def parse_arguments():
    """
    Parses command-line arguments for the SmeLLM tool.

    :return: Parsed arguments containing language, model, and paths.
    """
    parser = argparse.ArgumentParser(
        description="SmeLLM: Detect code smells using Large Language Models"
    )

    parser.add_argument(
        "-l",
        "--language",
        help="Specify which language to use to filter files",
        choices=list(LANGUAGE_EXTENSIONS.keys()),
    )

    parser.add_argument(
        "-m",
        "--model",
        help="Specify the model to use for code smell detection",
        choices=[m["name"] for m in models.MODELS],
        required=True,
    )

    parser.add_argument(
        '-fs',
        '--few-shot',
        help="Specify the code smell to use few-shot prompting for",
        choices=[smell["id"] for smell in CODE_SMELLS],
        required=False
    )

    parser.add_argument(
        "-e",
        "--eval",
        type=str,
        help="Run an evaluation of the model on a test .csv/.xlsx file",
    )

    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default="out/",
        help="(optional arg) Path to save the output files",
    )

    parser.add_argument(
        "-lm", "--list-models", action="store_true", help="List all available models"
    )

    source_path = parser.add_mutually_exclusive_group(required=True)
    source_path.add_argument("--file-path", type=str, help="Path to a specific file.")
    source_path.add_argument("--folder-path", type=str, help="Path to a folder.")
    source_path.add_argument("--zip-path", type=str, help="Path to a zip archive.")

    args = parser.parse_args()

    if args.list_models:
        list_available_models()
        sys.exit(0)

    validate_paths(args)

    print(f"Using model: {args.model}")
    print(f"Using language: {args.language if args.language else 'default'}")

    return args


def list_available_models(self):
    """Display all available models and exit."""

    try:
        with open(self.models_file_path, "r") as f:
            models_config = json.load(f)

        print("Available models:")
        print("-" * 40)

        # Sort models alphabetically for better display
        model_names = [
            model_data.get("model_name") for _, model_data in models_config.items()
        ]

        for i, model_name in enumerate(model_names, 1):
            print(f"{i}. {model_name}")

        print("-" * 40)
        print(f"Total available models: {len(model_names)}")

    except Exception as e:
        print(f"Error listing models: {e}")
        sys.exit(1)
