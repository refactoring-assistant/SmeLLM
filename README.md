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

**If you want to process a file**
```bash
python3 smellmv2\smellm.py --lang <file-coding-language> --file <file-path>
```

**If you want to process a folder**
```bash
python3 smellmv2\smellm.py --lang <file-coding-language> --folder <folder-path>
```

**If you want to process a zipfile**
```bash
python3 smellmv2\smellm.py --lang <file-coding-language> --zipfile <zipfile-path>
```

**If you want to check the list of models available to use**
```bash
python3 smellmv2\smellm.py --list_models
```

**If you want to process a file, folder or zipfile with a specific model**
```bash
python3 smellmv2\smellm.py --lang <file-coding-language> --[file, folder, zipfile] <path> --model <model-name>
```

**To get help on how to use the tool in terminal**

```bash
python3 smellmv2\smellm.py --help
```

### Supported Languages
- Java
- TypeScript