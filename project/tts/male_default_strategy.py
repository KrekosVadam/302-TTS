from piper.voice import PiperVoice
import numpy as np
import sounddevice as sd

from .tts_strategy import TTSStrategy

class MaleDefaultStrategy(TTSStrategy):
    """
    Default TTS Strategy class implementing the TTSStrategy interface. 
    This allows for a default voice to be used, no voice clone, etc.

    methods:
        synthesize(text: str):
            Generate speech from a chunk of text. Can be overridden by subclasses 
            for more specific implementations, such as generating male or female voices.
    """
    
    def synthesize(self, text: str):
        """
        Concrete method for generating default speech for the given text chunk.

        Args: text (str): A string representing the segment of text to be converted 
                            into speech.

        return: a list of bytes
        """

        # Empty list
        audio_data = []

        # load voice model
        # Ryan is a standard male voice
        voice = PiperVoice.load("project/voices/en_US-jadon-voice+RT-medium.onnx")

        # Loop through text and create voice then add to list
        for audio_bytes in voice.synthesize_stream_raw(text):
            int_data = np.frombuffer(audio_bytes, dtype=np.int16)
            audio_data.append(int_data)

        # Join
        np.concatenate(audio_data)

        return audio_data
