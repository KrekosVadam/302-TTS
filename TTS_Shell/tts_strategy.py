from abc import ABC, abstractmethod

class TTSStrategy(ABC):
    """
    Abstract Base Class for defining a Text-To-Speech (TTS) strategy. Utilises Python built-in
    abstract class base declaration.

    Args:
        ABC (Abstract Base Class): Python built-in abstract class base declaration.
    
    Methods:
        generate_audio(chunk: str):
            Abstract method. Takes a chunck of text (string) as input. 
            Output is returned in the desired format.
    """
    @abstractmethod
    def generate_audio(self, chunk: str):
        """
        Generate audio from the given text chunk.

        Args:
            chunk (str): Text to be converted to speech.

        Returns:
            None: Return type depends on concrete method.
        """
        pass
