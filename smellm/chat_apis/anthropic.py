from .chat_api import ChatAPI
import anthropic

class Anthropic(ChatAPI):

    def __init__(self, model):
        self.model = model

    def generate_response(self, system, user):
        client = anthropic.Anthropic()
        response = client.messages.create(
            model=self.model,
            system=system,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": user
                        }
                    ]
                }
            ]
        )
        return response.content
