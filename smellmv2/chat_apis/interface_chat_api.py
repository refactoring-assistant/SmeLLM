from abc import ABC, abstractmethod

# Define the interface (abstract base class)
class ChatAPI(ABC):
    @abstractmethod
    def chat_completion(self):
        """Method that must be implemented by any class that inherits from ChatAPI to enable chat completion."""
        pass
    