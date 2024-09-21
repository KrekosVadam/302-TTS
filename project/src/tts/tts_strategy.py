from abc import ABC, abstractmethod

from src.tts.BaseVoiceModelStrategy import BaseVoiceModelStrategy

class TTSStrategy(ABC):
    """
    Abstract Base Class for defining a Text-To-Speech (TTS) strategy. Utilises Python built-in
    abstract class base declaration.

    param: ABC (Abstract Base Class): Python built-in abstract class base declaration.
    
    methods:
        generate_speech(chunk: str, voice: BaseVoiceModelStrategy):
            Abstract method. Takes a chunck of text (string) and voice model as input. 
            Output is returned in the desired format.
    """
    @abstractmethod
    def generate_speech(self, chunk: str, voice: BaseVoiceModelStrategy):
        """
        Generate speech from the given text chunk.

        param: chunk (str): chunk of text to be converted to speech.
        param: voice (BaseVoiceType): voice model to use to generate speech.
        
        return: None: Return type depends on concrete method.
        """
        pass
