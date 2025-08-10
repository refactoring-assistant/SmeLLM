from .chat_api import ChatAPI
import openai
from openai import OpenAI
from pydantic import BaseModel, RootModel
from typing import List
import os
from dotenv import load_dotenv
import json

# Load environment variables from the .env file in the smellm/ directory
load_dotenv(os.path.join(os.path.dirname(__file__), "../.env"))


class CodeSmell(BaseModel):
    code_smell: str
    line_numbers: List[int]

class CodeSmellList(BaseModel):
    RootModel: List[CodeSmell]

class OpenAIAPI(ChatAPI):

    def __init__(self, model):
        self.model = model

    def generate_response(self, system, user):
        try:
            client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
            response = client.chat.completions.create(
                model=f"{self.model}",
                messages=[
                    {"role": "developer", "content": system},
                    {"role": "user", "content": user},
                ],
                tools=[openai.pydantic_function_tool(CodeSmellList)]
            )

            arguments_str = response.choices[0].message.tool_calls[0].function.arguments
            if not arguments_str:
                print("Error: No arguments received in the response.")
                return "Error: No arguments received in the response."

            try:
                arguments = json.loads(arguments_str)
                root_model = arguments["RootModel"]
                print(root_model)
            except json.JSONDecodeError as e:
                print("Error decoding JSON arguments:", e)
                return "Error decoding JSON arguments."

            return root_model
        except Exception as e:
            print("Error occurred while generating response:", e)
            return "Error occurred while generating response."
