import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

import config.constants as constants

class Prompt():
    def __init__(self, user_input, prompt_format = "OAI"):
        match prompt_format:
            case "OAI":
                self.__create_prompts(user_input)
            case "ANTHROPIC":
                self.__create_prompts(user_input)
            case _:
                raise ValueError(f"Invalid prompt format: {prompt_format}")
            
    def get_conversation_start(self):
        return [self.system_prompt, self.user_prompt]
    
    def __create_prompts(self, user_input):
        self.system_prompt = {"role": "system", "content": constants.SYSTEM_PROMPT}
        self.user_prompt = {"role": "user", "content": constants.USER_PROMPT + user_input}
            

if __name__ == '__main__':
    prompt = Prompt("Hello, how are you?")
    print(prompt.get_conversation_start())