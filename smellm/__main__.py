import os
import sys

from cli import parse_arguments


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

from process_args.process_file import ProcessFile
from process_args.process_zipfile import ProcessZipFile
from process_args.process_folder import ProcessFolder
from output.save_data import SaveData
from output.test_output import TestOutput

def main():
    try:
        args = parse_arguments()

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

        save_data = SaveData(args.output)
        saved_dir = save_data.save_file(processed_data)
        print(f"Processed data saved to: {saved_dir}")

        if args.test:
            tester = TestOutput(saved_dir, args.test)
            tester.test()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
