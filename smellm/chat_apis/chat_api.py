from abc import ABC, abstractmethod

# Define the interface (abstract base class)
class ChatAPI(ABC):
    @abstractmethod
    def generate_response(self):
        """Method that must be implemented by any class that 
        inherits from ChatAPI to enable chat completion."""
        pass