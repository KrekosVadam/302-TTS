import time
import numpy as np
from TTS_Shell.tts_strategy import TTSStrategy

class DefaultStrategy(TTSStrategy):
    """
    Default TTS Strategy class implementing the TTSStrategy interface. 
    This allows for a default voice to be used, no voice clone, etc.

    Methods:
        generate_speech(chunk: str):
            Generate speech from a chunk of text. Can be overridden by subclasses 
            for more specific implementations, such as generating male or female voices.
    """
    
    def generate_speech(self, chunk: str):
        """
        Concrete method for generating default speech for the given text chunk.

        Args:
            chunk (str): A string representing the segment of text to be converted 
                         into speech.

        Returns:
            np.ndarray: ********[FILL IN HERE ONCE DONE]********
        """
        
        print("This function generates default speech.")    
        print(f"Generating audio for chunk: {chunk}")
        time.sleep(0.5)  # Simulate processing time

        return np.random.rand(10000)  # Dummy audio data

class MaleVoiceStrategy(DefaultStrategy):
    def generate_speech(self, chunk: str):
        print("Generating male voice.")
        # Add male voice here
        return super().generate_speech(chunk)

class FemaleVoiceStrategy(DefaultStrategy):
    def generate_speech(self, chunk: str):
        print("Generating female voice.")
        # Add female voice here
        return super().generate_speech(chunk)