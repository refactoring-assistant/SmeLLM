from abc import ABC, abstractmethod

# Define the interface (abstract base class)
class ChatAPI(ABC):
    @abstractmethod
    def chat_completion(self):
        """Method that must be implemented by any class that inherits from ChatAPI to enable chat completion."""
        pass
    
    @abstractmethod
    def batch_chat_completion(self, file_names, batch_conversations_list=[]):
        """Method that must be implemented by any class that inherits from ChatAPI to enable batch chat completion."""
        pass