
from .cli import parse_arguments
from .processor import parse_dict
from .utils.file_utils import extract_file_content, extract_folder_content, extract_zip_content

def main():
    try:
        args = parse_arguments()

        if args.file_path:
            dict = extract_file_content(args.file_path, args.language)
            parse_dict(args, dict)
        elif args.folder_path:
            dict = extract_folder_content(args.folder_path, args.language)
            parse_dict(args, dict)
        elif args.zip_path:
            dict = extract_zip_content(args.zip_path, args.language)
            parse_dict(args, dict)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
