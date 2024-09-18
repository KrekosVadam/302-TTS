from abc import ABC, abstractmethod

class StreamStrategy(ABC):
    """
    Stream Strategy abstract class base. Utilises Python built-in
    abstract class base declaration.

    param: ABC (Abstract Base Class): Python built-in abstract class base declaration.
    
    method: stream(text: str): takes a text sample, outputs a chunk of said sample
    """
    @abstractmethod
    def stream(self, text: str, max_words: int):
        """
        Generate speech from the given text chunk.

        param: text (str): Text to be converted to chunks
        param: max_words (int): chunk size (10 = 10 words)
        
        return: None: Return type dependant on concrete method
        """
        pass
