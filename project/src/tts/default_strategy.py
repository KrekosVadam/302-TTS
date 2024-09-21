import time
import numpy as np

from src.tts.tts_strategy import TTSStrategy
from src.tts.BaseVoiceModelStrategy import BaseVoiceModelStrategy

class DefaultStrategy(TTSStrategy):
    """
    Default TTS Strategy class implementing the TTSStrategy interface. 
    This allows for a default voice to be used, no voice clone, etc.

    methods:
        generate_speech(chunk: str, voice: BaseVoiceModelStrategy):
            Generate speech from a chunk of text and voice . Can be overridden by subclasses 
            for more specific implementations, such as generating male or female voices.
    """
    
    def generate_speech(self, chunk: str, voice: BaseVoiceModelStrategy):
        """
        Concrete method for generating default speech for the given text chunk.

        param: chunk (str): A string representing the segment of text to be converted 
                            into speech.
        param: voice (BaseVoiceModelStrategy): The voice model to be used for speech generation.

        return: np.ndarray: ********[FILL IN HERE ONCE DONE]********
        """
        
        print("This function generates default speech.")    
        print(f"Generating audio for chunk: {chunk}")
        time.sleep(0.5)  # Simulate processing time

        return np.random.rand(10000)  # Dummy audio data