from abc import ABC, abstractmethod

class TTSStrategy(ABC):
    """
    Abstract Base Class for defining a Text-To-Speech (TTS) strategy. Utilises Python built-in
    abstract class base declaration.

    param: ABC (Abstract Base Class): Python built-in abstract class base declaration.
    
    methods:
        synthesize(text: str):
            Abstract method. Takes a chunck of text (string) as input. 
            Output is returned in the desired format.
    """
    @abstractmethod
    def synthesize(self, text: str):
        """
        Generate speech from the given text chunk.

        param: text (str): chunk of text to be converted to speech.
        
        return: None: Return type depends on concrete method.
        """
        pass
