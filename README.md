# SmeLLM
The main repository for the tool - SmeLLM: Automatic Code Smell Identification and Refactoring Using LLMs.

### How to run the tool - SmeLLM v2

Based on your Python execution environment, the Python run command can be a alias from `python`, `python3`, `py` and any other alias possible. In this readme, we will be using python3.

**Optional - Create a virtual environment** \
Refer to the [venv docs](https://docs.python.org/3/library/venv.html) to see how to create a virtual environment and activate it.

**Install the required dependencies**
```bash
python3 pip install -r requirements.txt
```

**Set environment variables**
In the `smellmv2/config` folder, create a .env file containing your OpenAI key in the following format
```
OAI_KEY=<your-key>
```
Another way of setting your environment variable can be through a command line argument - set_env
```bash
python3 smellmv2\smellm.py --set_env <KEY=VALUE>
```
Here we enter `KEY` as `OAI_KEY` for OpenAI and `VALUE` as the value of the key to access the OpenAI API.


### Possible Command Line Arguments:
-  -h, --help           Show this help message and exit.
```bash
python3 smellmv2\smellm.py --help
```

-   --list_models           List all available models.
```bash
python3 smellmv2\smellm.py --list_models
```

-   --file <file-path>           Path to process a single code file.
```bash
python3 smellmv2\smellm.py --lang <file-coding-language> --file <file-path>
```

-   --folder <folder-path>          Path to process single folder.
```bash
python3 smellmv2\smellm.py --lang <file-coding-language> --folder <folder-path>
```

-   --zipfile <zipfile-path>          Path to process single zipfile.
```bash
python3 smellmv2\smellm.py --lang <file-coding-language> --zipfile <zipfile-path>
```

-   --model <model-name>          Choose a model to process the code.
```bash
python3 smellmv2\smellm.py --lang <file-coding-language> --[file, folder, zipfile] <path> --model <model-name>
```

-   --output <dir-path>          Save to a particular directory.
```bash
python3 smellmv2\smellm.py --lang <file-coding-language> --[file, folder, zipfile] <path> --output <dir-path>
```

-   --test <test-file-path>         Provide a test file to run tests on the code.
```bash
python3 smellmv2\smellm.py --lang <file-coding-language> --[file, folder, zipfile] <path> --test <test-file-path>
```

**Format of Test File (in Excel)**

| File Name   | Expected Code Smells            |
|-------------|---------------------------------|
| File Name 1 | [List of code smells in file 1] |
| File Name 2 | [List of code smells in file 2] |

**A template excel file is provided as `TEST.xlsx`**
- Keep the file name without extension.

### Supported Languages
- Java
- TypeScript


### Current Folders/Files Information
- `smellmv2/`: The main folder containing the code for SmeLLM.
- `java_single_file_code_smells/`: The folder containing result generated on each of the java code smells.
- `test_output/`: The folder containing output for all the code smells. (Was utilized to enable testing benchmarks)
-  `.xlsx` files: The excel files with benchmark results for the code smells.
- `.zip` files: The zip files containing the code smells for java.